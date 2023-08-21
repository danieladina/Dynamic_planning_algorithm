# Linear search: Complexity: O(n)
def sequential_search(L, x):
    for e in L:
        if e == x:
            return True
    # if we got here the search failed
    return False


# Binary search: Complexity: O(log(n))
def binary_search(L, x):
    ''' search for x in L, which MUST BE SORTED !! '''
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == x:
            return True
        else:
            if L[mid] < x:  # go to right half
                left = mid + 1
            else:  # go to left half
                right = mid - 1

    return False  # if we got here the search failed

# Selection sort (version 1) is not the most effective type of sorting. Complexity: O(n^2)
def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)

    return sorted_L

# Selection sort (version 2) is not the most effective type of sorting. Complexity: O(n^2)
def selection_sort2(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        maximum = max(L)
        L.remove(maximum)
        sorted_L = [maximum, sorted_L]

    return sorted_L

'''
more complex sort algorithms:
Bubble sort, 
Merge sort, Quicksort, and Bucket Sort.
'''

# Merge sort is the more effective type of sorting. Complexity: O(n*log(n))
def merge_sort(L):
    '''
    1. Divide: continuously break down the larger problem into smaller parts.
    2. Conquer: solve each of the smaller parts by utilising a function that’s called recursively.
    3. Combine: merge all solutions for all smaller parts into a single unified solution, which becomes the solution to the starting problem.
    Complexity: O(n*log(n))
    :param L: unsorted list
    :return: sorted list
    '''
    if len(L) > 1:
        q = len(L) // 2  # Finding the middle of the array
        p = L[:q]  # left partition after dividing the array elements into 2 halves
        r = L[q:]  # right partition after dividing the array elements into 2 halves
        left_partition = merge_sort(p)
        right_partition = merge_sort(r)
        return merge(left_partition, right_partition)
    return L


def merge(L1, L2):
    '''
    Merge two sorted lists into one sorted list
    :param L1: first sorted list
    :param L2: second sorted list
    :return: sorted list
    '''
    merge_list = []
    i = j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merge_list.append(L1[i])
            i += 1
        else:
            merge_list.append(L2[j])
            j += 1
    merge_list.extend(L1[i:])
    merge_list.extend(L2[j:])
    return merge_list

def run_merge_sort():
    unsorted_list = [2, 4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


import random

def generate_random_list(n):
    ''' returns a list of size n with random integers between 0 and 999999
        Uses random.randint(a,b) which randomly picks an integer between a and b
    '''
    return [random.randint(0, 999999) for i in range(n)]  # a short way to generate the list


### TESTS ###
# Time measurements
import time  # the library time
'''
print("********************")
print("Search Algorithms - Starting the test of the time measurements:")
print("Note: we test your search functions on 3 RANDOM lists with 1000000 * i items each, where i = (1,2,4)")
print("********************")


for i in [1, 2, 4]:
    num_elems = 1000000 * i
    print("*** number of elements:", num_elems, "***")

    L = [i for i in range(num_elems)]  # a short way to generate the list [0,1,2,...,num_elems-1]

    # linear search
    start = time.time()
    res = sequential_search(L, -1)  # res must be False, this is worst case running time
    end = time.time()
    print("Linear search time:", end - start)

    # binary search
    start = time.time()
    res = binary_search(L, -1)  # res must be False, this is worst case running time
    end = time.time()
    print("Binary search time:", end - start)
    print()  # just a new lin



print("********************")
print("Starting the test of correct algorithms:")
print("Note: we test your function on 3 RANDOM lists with 7 items each")
for i in range(3):
    print("********************")
    L = [random.randint(1, 100) for j in range(7)]
    print("Testing the following list:", L)
    if sorted(L) == selection_sort2(L[:]):  # pass a copy of L to selection_sort2
        print("CORRECT: Very good, the sorted list is:", sorted(L))
    else:
        print("WRONG: your answer is:", selection_sort(L[:]), ", but the correct answer is:", sorted(L))

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")
'''

print("********************")
print("Sort Algorithms - Starting the test of the time measurements:")
print("Note: we test your sort functions on 3 RANDOM lists with 1000 * i items each, where i = (1,2,4)")
print("********************")
for n in [1000, 2000, 4000]:
    lst = generate_random_list(n)

    start = time.time()
    lst2 = selection_sort(lst)  # lst2 not used
    end = time.time()

    print("Number of elements in the list: ", n)
    print("Time measured for selection_sort: ", end - start, " seconds")

    start = time.time()
    lst3 = merge_sort(lst)  # lst3 not used
    end = time.time()

    print("Time measured for merge_sort: ", end - start, " seconds")
    print()  # just a new line


print("********************")
print("Note: we test your sort functions on one RANDOM list with 20000 items")
print("********************")
n = 20000
lst = generate_random_list(n)

start = time.time()
lst2 = selection_sort(lst) # lst2 not used
end = time.time()

print("Number of elements in the list: ", n)
print("Time measured for selection_sort: ",  end-start, " seconds")

start = time.time()
lst3 = merge_sort(lst) # lst3 not used
end = time.time()

print("Time measured for merge_sort: ",  end-start, " seconds")
print() # just a new line
