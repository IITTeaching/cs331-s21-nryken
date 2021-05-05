from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if pivot_fn == pivot_first:
        pivot_first(lst, low, high)
    if pivot_fn == pivot_random:
        pivot_random(lst, low, high)
    if pivot_fn == pivot_median_of_three:
        pivot_median_of_three(lst, low, high)
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    iLow = low
    iHigh = high
    pivot_val = lst[low]
    toBig = False
    toSmall = False

    while low != high:

        if lst[low] < pivot_val:
            low += 1
        else:
            toBig = True
        
        if lst[high] > pivot_val:
            high -= 1
        else:
            toSmall = True

        if toBig and toSmall:

            temp = lst[low]
            lst[low] = lst[high]
            lst[high] = temp

            toBig = False
            toSmall = False

    if lst[0] > lst[low]:
        lst[0] = lst[low]
        lst[low] = pivot_val
            
    if low - iLow > 1:
        pivot_first(lst, iLow, low - 1)
    if iHigh - low > 1:
        pivot_first(lst, low + 1, iHigh)
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    iLow = low
    iHigh = high
    pivot_loc = random.randrange(low, high)
    pivot_val = lst[pivot_loc]
    toBig = False
    toSmall = False

    while low != high:

        if lst[low] < pivot_val:
            low += 1
        else:
            toBig = True

        if lst[high] > pivot_val:
            high -= 1
        else:
            toSmall = True

        if toBig and toSmall:

            temp = lst[low]
            lst[low] = lst[high]
            lst[high] = temp

            toBig = False
            toSmall = False

    if pivot_loc < low and pivot_val > lst[low]:
        lst[pivot_loc] = lst[low]
        lst[low] = pivot_val

    elif pivot_loc > low and pivot_val < lst[low]:
        lst[pivot_loc] = lst[low]
        lst[low] = pivot_val

            
    if low - iLow > 1:
        pivot_random(lst, iLow, low - 1)
    if iHigh - low > 1:
        pivot_random(lst, low + 1, iHigh)
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    iLow = low
    iHigh = high
    median = [lst[low], lst[(low + high) // 2], lst[high]]
    median.remove(min(median))
    median.remove(max(median))
    pivot_val = median[0]
    toBig = False
    toSmall = False

    while low != high:

        if lst[low] < pivot_val:
            low += 1
        else:
            toBig = True

        if lst[high] > pivot_val:
            high -= 1
        else:
            toSmall = True

        if toBig and toSmall:

            temp = lst[low]
            lst[low] = lst[high]
            lst[high] = temp

            toBig = False
            toSmall = False
            
    if low - iLow > 1:
        pivot_median_of_three(lst, iLow, low - 1)
    if iHigh - low > 1:
        pivot_median_of_three(lst, low + 1, iHigh)
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
