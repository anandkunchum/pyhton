
var_str = "Anand"
print(var_str[0])


string = "Big Data iNeuron"
list_words = string.split(" ")
print(list_words[2])


print(list_words[2][-1 : : -1])

print(string[-1 : : -1])

var_str = ""

var_str = "'iNeuron's Big Data Course'"
print(var_str)

lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])

#Q38. Take a list as an input from the user and find the length of the list.

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input()
    lst.append(ele)
print(lst)
print(len(lst))

#Q39. Add the word "Big" in the 3rd index of the given list.
lst = ["Welcome", "to", "Data", "course"]
lst[2] = "Big"
print(lst)