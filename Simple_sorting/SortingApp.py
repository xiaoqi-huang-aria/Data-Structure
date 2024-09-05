import SortingArray
import random


capacity = 20
nb_of_experiments = 6


print("######## GENERATING UNSORTED ARRAY ########")

my_array = SortingArray.SortingArray(capacity)

for i in range(capacity):
    my_array.insert(random.randint(1, 100))
my_array.display()

print("\n######## BUBBLE SORT ########")

sorted_array, nb_comps, nb_swaps = my_array.bubbleSort()
print(sorted_array)
print("#comparisons: ", nb_comps, "   #swaps", nb_swaps)

print("\n######## SELECTION SORT ########")

sorted_array, nb_comps, nb_swaps = my_array.selectionSort()
print(sorted_array)
print("#comparisons: ", nb_comps, "   #swaps", nb_swaps)

print("\n######## INSERTION SORT ########")

sorted_array, nb_comps, nb_swaps = my_array.insertionSort()
print(sorted_array)
print("#comparisons: ", nb_comps, "   #swaps", nb_swaps)

print("\n######## PERFORMANCE EXPERIMENTS ########")

for i in range(nb_of_experiments):
    my_array = SortingArray.SortingArray(capacity)
    bub_comps, sel_comps, ins_comps = [], [], []
    bub_swaps, sel_swaps, ins_swaps = [], [], []
    for i in range(capacity):
        my_array.insert(random.randint(1, 100))
    sorted_array, nb_comps, nb_swaps = my_array.bubbleSort()
    bub_comps.append(nb_comps)
    bub_swaps.append(nb_swaps)
    sorted_array, nb_comps, nb_swaps = my_array.selectionSort()
    sel_comps.append(nb_comps)
    sel_swaps.append(nb_swaps)
    sorted_array, nb_comps, nb_swaps = my_array.insertionSort()
    ins_comps.append(nb_comps)
    ins_swaps.append(nb_swaps)

print("\t-- #comparisons --")
print("BUB>", sum(bub_comps)/len(bub_comps))
print("SEL>", sum(sel_comps)/len(sel_comps))
print("INS>", sum(ins_comps)/len(ins_comps))
print("\t-- #swaps --")
print("BUB>", sum(bub_swaps)/len(bub_swaps))
print("SEL>", sum(sel_swaps)/len(sel_swaps))
print("INS>", sum(ins_swaps)/len(ins_swaps))
