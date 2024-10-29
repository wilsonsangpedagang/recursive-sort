def minIndex(lst, startIndex):
    # base case: only one element to consider
    if startIndex == len(lst) - 1:
        return startIndex

    # Find minimum of remaining elements recursively
    k = minIndex(lst,startIndex + 1)

    # Return the minimum of all
    if lst[startIndex] < lst[k]:
        return startIndex
    else:
        return k

a = [2,4,1,5,3]
startIndex = 0

print(minIndex(a,startIndex))


def selection_sort(lst, startIndex=0):
    n = len(lst)

    # when starting index and size of list are the same, return;
    # because there is nothing to sort
    if startIndex == len(lst):
        return

    # find the index of minimum element
    # from startIndex to the end
    k = minIndex(lst, startIndex)

    # Swapping the corresponding elements
    # when the found index and the current minimum
    # index are not the same
    if lst[startIndex] != lst[k]:
        lst[k], lst[startIndex] = lst[startIndex], lst[k]
    # Recursively calling selection sort function for the
    # remaining elements
    selection_sort(lst, startIndex + 1)

    ## main():
    # demonstrates the selection sort algorithm by sorting a
    # list of integers given by user

selection_sort(a)
print(a)


def main():
    input_string = input("Type a sequence of numbers (example: 3,100,-5,3): \n")
    if input_string == '':
        values = []
    else:
        values = input_string.split(",")

    # change each element from str to int
    for i in range(len(values)):
        values[i] = int(values[i])

    print('Input list:\n', values)
    minIndex(values,startIndex)
    selection_sort(values,startIndex)
    print('Sorted list:\n', values)


if __name__ == '__main__':
    main()


