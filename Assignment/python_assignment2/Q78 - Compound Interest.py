#Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

P = int(input('Enter total principle amount:'))
R = float(input('Enter rate of interest:'))
t = int(input('Enter the time duration in years:'))
A = P * ((1+ R/100) ** t)
print('Total compound interest :',round(A))