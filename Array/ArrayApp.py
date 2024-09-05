import UnsortedArray
import SortedArray
import random

capacity = 20


print("######## UNSORTED ARRAY ########")

my_array = UnsortedArray.UnsortedArray(capacity)

my_array.display()
for i in range(capacity+1):
    my_array.insert(random.randint(1, 100))
my_array.display()
my_array.delete(my_array.getElementAt(19))
my_array.display()
my_array.delete(my_array.getElementAt(12))
my_array.display()
my_array.delete(101)


print("######## SORTED ARRAY ########")

my_array = SortedArray.SortedArray(capacity)

my_array.display()
for i in range(20):
    v = random.randint(1, 100)
    print("inserting", v)
    my_array.insert(v)
my_array.display()
v = my_array.getElementAt(10)
print("deleting", v)
my_array.delete(v)
my_array.display()
v = 101
print("deleting", v)
my_array.delete(v)
v = random.randint(1, 100)
print("deleting", v)
my_array.delete(v)
for i in range(my_array.get_size() // 2):
    v = my_array.getElementAt(0)
    print("deleting", v)
    my_array.delete(v)
for i in range(my_array.get_size()):
    v = my_array.getElementAt(my_array.get_size() - 1)
    print("deleting", v)
    my_array.delete(v)
my_array.display()