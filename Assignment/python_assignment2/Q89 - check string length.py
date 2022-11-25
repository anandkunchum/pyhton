#Q89. Write a Python program to find words which are greater than given length k.

lst = ["Anand","Kumar","Raju","iNeuron","Solution","Implement"]
max_len = int(input('Enter expected max length of the word:'))
print('Below are the words length greater than ',max_len,' :')
for item in lst:
    if len(item) > max_len:
        print(item)

