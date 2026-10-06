import random
random.seed(0)

from rbst import *

'''
A dynamic sequence is implemented using a list, as well as your RBST data structure.
The output of the RBST must match the one from the list.
'''

def print_list(arr):
    for x in arr:
        print(x, end= ' ')
    print()

n = 100
# Create a random list of numbers 1...n
arr = [i + 1 for i in range(n)]
random.shuffle(arr)


# Create the same sequence with RBST.
T = RBST()
for i, x in enumerate(arr):
    # T.insert_normal(x, i+1)
    T.insert(x, i+1) # Uncomment this (and comment out insert_normal) when testing for insert.

# Check if the output is correct.
print("Printing the sequence stores as a list.")
print_list(arr)

print("Printing the sequence stores in the RBST.")
tin = [x for x in T.inorder()]
print_list(tin)

# Insert a bunch of 100s at 10 random locations, both in the list as well as the RBST.
for i in range(10):
    rank = random.randint(1, n + i)
    arr.insert(rank - 1, 100)
    # T.insert_normal(100, rank)
    T.insert(100, rank)

print("\nPrinting the sequence stores as a list.")
print_list(arr)

print("Printing the sequence stores in the RBST.")
tin = [x for x in T.inorder()]
print_list(tin)


# Insert 5 200s at the beginning.
for i in range(5):
    arr.insert(0, 200)
    # T.insert_normal(200, 1)
    T.insert(200, 1)

print("\nPrinting the sequence stores as a list.")
print_list(arr)

print("Printing the sequence stores in the RBST.")
tin = [x for x in T.inorder()]
print_list(tin)


# Insert 5 300s at the end.
for i in range(5):
    arr.append(300)
    # T.insert_normal(300, len(T)+1)
    T.insert(300, len(T)+1)

print("\nPrinting the sequence stores as a list.")
print_list(arr)

print("Printing the sequence stores in the RBST.")
tin = [x for x in T.inorder()]
print_list(tin)

# Uncomment these to test select.
print("\nPrinting the sequence using the select operation.")
for i in range(1, len(T) + 1):
    x = T.select(i)
    print(str(x.data), end=' ')
print()

"""
# Uncommennt these to test split.
# Do a couple of splits in the middle
s = T.split(50)
print("\nSplitting T at rank 50")
print("Printing the left side of the split.")
tin = [x for x in s[0].inorder()]
print_list(tin)
print("Printing the right side of the split.")
tin = [x for x in s[1].inorder()]
print_list(tin)

r = s[0].split(25)
print("\nSplitting left side at rank 25")
print("Printing the left side of the second split.")
tin = [x for x in r[0].inorder()]
print_list(tin)
print("Printing the right side of the second split.")
tin = [x for x in r[1].inorder()]
print_list(tin)

# Do splits at the beginning and the end.
print("\nSplitting the above left side again on the last index.")
u = r[0].split(len(r[0]))
print("Printing the left side of the third split.")
tin = [x for x in u[0].inorder()]
print_list(tin)
print("Printing the right side of the third split.")
tin = [x for x in u[1].inorder()]
print_list(tin)

v = u[0].split(1)
print("\nSplitting the above left side again on the first index.")
print("Printing the left side of the fourth split.")
tin = [x for x in v[0].inorder()]
print_list(tin)
print("Printing the right side of the fourth split.")
tin = [x for x in v[1].inorder()]
print_list(tin)

w = u[0].split(0)
print("\nSplitting the above right side again on index 0.")
print("Printing the left side of the fifth split.")
tin = [x for x in w[0].inorder()]
print_list(tin)
print("Printing the right side of the fifth split.")
tin = [x for x in w[1].inorder()]
print_list(tin)
"""

