# Recursive Selection Sort Program

This Python script implements a simple selection sort algorithm, which sorts a list of integers provided by the user. The code uses recursion for both finding the minimum index in the unsorted portion of the list and sorting the list in-place.

## Overview

This program consists of three main components:
1. **`minIndex`** - A function that finds the minimum element index in a list from a given starting index.
2. **`selection_sort`** - A recursive selection sort function.
3. **`main`** - A function that takes user input, processes it into a list, and outputs the sorted result.

## Functions

### `minIndex(lst, startIndex)`
This function recursively finds the index of the minimum element in `lst` starting from `startIndex`.
- **Parameters**:
  - `lst`: List of integers to search through.
  - `startIndex`: Index to start searching from.
- **Returns**: The index of the minimum element in the specified range of the list.

### `selection_sort(lst, startIndex=0)`
This function implements the selection sort algorithm recursively.
- **Parameters**:
  - `lst`: List of integers to sort.
  - `startIndex`: Starting index for sorting.
- **Returns**: The list sorted in-place.

### `main()`
Prompts the user to input a list of integers, sorts it, and displays the original and sorted lists.
- **Input**: A comma-separated string of numbers (e.g., `3,100,-5,3`).
- **Output**: Original and sorted list.

## How to Use

1. **Run the Program**:
   - Execute the program in a Python environment. You’ll be prompted to input a list of numbers.
   - Example input: `1,5,3,7,9`

2. **View the Output**:
   - The program displays the list before and after sorting.

## Example Run
```bash
$ python recur_sort.py
Type a sequence of numbers (example: 3,100,-5,3): 
8,3,5,2,9,1

Input list:
[8, 3, 5, 2, 9, 1]
Sorted list:
[1, 2, 3, 5, 8, 9]

