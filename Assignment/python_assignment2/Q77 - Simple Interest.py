
#Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

P = int(input('Enter total principle amount:'))
R = float(input('Enter rate of interest:'))
T = int(input('Enter the time duration in years:'))
SI = (P*R*T)/100
print(SI)