from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from google.api_core.exceptions import Conflict

# Path to your service account key JSON file
service_account_file = 'my_poc_sa.json'
# Create credentials object
credentials = service_account.Credentials.from_service_account_file(service_account_file)
# Initialize BigQuery client with credentials
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

date_fields = { 'clients' : ['DOB','Created_time'],
                'Account' : ['Created_at']}
timestamp_fields = { 'clients' : ['Created_time'],
               'Account' : ['Created_at']}

# Function to create a dataset in BigQuery
def create_bq_dataset(dataset_id, location="EU"):
    # Construct a full Dataset ID
    full_dataset_id = f"{client.project}.{dataset_id}"  
    # Construct a DatasetReference and a Dataset object
    dataset = bigquery.Dataset(full_dataset_id)
    # Specify the geographic location where the dataset should reside
    dataset.location = location
    # Create the dataset in BigQuery
    try:
        dataset = client.create_dataset(dataset, timeout=30)  # Timeout in seconds
        print(f"Dataset {dataset_id} created in project {client.project} at location {location}.")
    except Conflict:
        print(f"Dataset {dataset_id} already exists in project {client.project}.")

def table_exists(dataset_id, table_id):
    try:
        client.get_table(f"{dataset_id}.{table_id}")
        return True
    except:
        return False

# Function to create a BigQuery table and upload data from DataFrame
def create_table_and_upload_data(dataset_id, table_id, dataframe):
    # Construct the full table ID
    full_table_id = f"{client.project}.{dataset_id}.{table_id}"
    print(f"table - {table_id}")
    
    # Check if the table already exists
    if table_exists(dataset_id, table_id):
        print(f"Table {full_table_id} already exists.")
        client.delete_table(full_table_id)
        print(f"Table {full_table_id} deleted successfully.")
    
    # Define the schema for the table based on the DataFrame columns
    schema = []
    for column_name, dtype in zip(dataframe.columns, dataframe.dtypes):
        # Map pandas dtypes to BigQuery types
        if pd.api.types.is_integer_dtype(dtype):
            bq_type = "INT64"
        elif pd.api.types.is_float_dtype(dtype):
            bq_type = "FLOAT64"
        elif pd.api.types.is_bool_dtype(dtype):
            bq_type = "BOOL"
        elif pd.api.types.is_datetime64_any_dtype(dtype):   
            bq_type = "TIMESTAMP"
        else:
            bq_type = "STRING"
        print(f"{column_name} : {bq_type} ")
        schema.append(bigquery.SchemaField(column_name, bq_type))
        

    # Create a BigQuery table with the specified schema
    table = bigquery.Table(full_table_id, schema=schema)
    table = client.create_table(table)  # API request
    print(f"Created table {full_table_id}")

    # Define the job configuration for uploading data
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"  # Append to table if exists
    )
    
    # Upload the DataFrame to the BigQuery table
    load_job = client.load_table_from_dataframe(dataframe, full_table_id, job_config=job_config)
    
    # Wait for the job to complete
    load_job.result()
    print(f"Uploaded {dataframe.shape[0]} rows to {full_table_id}")

def data_transformation(table_id, dataframe):
    for df_column in dataframe.columns.tolist():
        if table_id in list(date_fields.keys()):
            if df_column in date_fields[table_id]:
                dataframe[df_column] = pd.to_datetime(dataframe[df_column], format='%d-%m-%Y %H:%M:%S', errors='coerce')

# # Replace with your desired dataset ID
# dataset_id = "my_poc_test_ds1"

# # Read xls with multiple sheets into a dictionary with dataframes
# my_poc_xls = pd.read_excel('my_poc.xlsx',sheet_name=None)

# date_fields = { 'clients' : ['DOB','Created_time'],
#                 'Account' : ['Created_at']}
# timestamp_fields = { 'clients' : ['Created_time'],
#                'Account' : ['Created_at']}



# # Call the function to create the dataset
# create_bq_dataset(dataset_id, location="EU")  # You can specify different locations such as "EU"
