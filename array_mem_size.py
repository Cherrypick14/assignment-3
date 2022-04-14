#   a program to determine the memory size of an array

import numpy as np

def array_mem_size():
   arr_store = np.array(list(map(int, input("Enter a number of elements: ").strip().split())))
   return f"array size is: {arr_store.size} \ntotal memory occupied: {arr_store.size * arr_store.itemsize}"

print(array_mem_size())