import bq_functions as bq
import pandas as pd


# Read xls with multiple sheets into a dictionary with dataframes
my_poc_xls = pd.read_excel('my_poc.xlsx',sheet_name=None)

# Replace with your Google Cloud project, dataset, and table details
project_id = 'my-poc-437704'
dataset_id = 'my_poc_test_ds'
bq.service_account_file = 'my_poc_sa.json'

bq.create_bq_dataset(dataset_id)

for table in list(my_poc_xls.keys()):
        bq.data_transformation(table,my_poc_xls[table])
        bq.create_table_and_upload_data(dataset_id, table, my_poc_xls[table])
