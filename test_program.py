
set_a = {1,2,8,2}
set_b = {"abc","xyz"}
set_b.update(set_a)
print(set_b)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

var = {"name":"Anand","city":"chennai","company":"Nissan"}
print(var.values())

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

