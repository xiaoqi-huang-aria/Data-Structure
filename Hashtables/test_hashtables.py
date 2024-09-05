import random
from KVItem import KVItem
from DictionaryAsList import DictionaryAsDoubleList
from ChainHashtable import ChainHashtable

def test_dict(mydict):
    print(mydict)
    print("***Inserting items***")
    for i in range(20):
        k = random.randint(1,20)
        v = random.randint(1,100)
        print("Putting", k, v)
        mydict.put(k, v)
    print(mydict)
    print("***Finding values***")
    i = 0
    while (i < 2):
        k = random.randint(1,20)
        v = mydict.get(k)
        if (v != None):
            i += 1
            print("Found", k, v)
    print("***Removing values***")
    i = 0
    while (i < 2):
        k = random.randint(1,20)
        v = mydict.remove(k)
        if (v != None):
            i += 1
            print("Removed", k, v)
    print(mydict)
    print("***Clearing all values***")
    mydict.clear()
    print(mydict)


def main():
    #mydict = DictionaryAsDoubleList()
    mydict = ChainHashtable(7)
    test_dict(mydict)


main()
