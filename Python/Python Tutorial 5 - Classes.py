#Classes example

# blueprint
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

    
p1 = Person("John", 36)
p1.age = 40
# print(p1.name)
# print(p1.age)

#dictionary
dict_name = {}
lst = ['name 1', 'name 2', 'name 3']
lst2 = ['hafiz', 'john', 'sean']

# dict_name["name 1"] = "hafiz"
for i in range(len(lst)):
    dict_name[lst[i]] = lst2[i]

print(dict_name)
