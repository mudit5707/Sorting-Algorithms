# Sorting-Algorithms
A Python implementation of classic sorting algorithms with a command-line interface for comparison and experimentation.

📊 Sorting Algorithms in Python

This repository contains implementations of several classic sorting algorithms written in Python.
The program allows the user to choose a sorting technique at runtime via the command line.

🧠 Algorithms Implemented

Bubble Sort

Insertion Sort

Selection Sort

Merge Sort

Each algorithm is implemented from scratch to highlight its logic and behavior.

⚙️ Program Structure

Each sorting algorithm is implemented as a separate function.

A higher-order function (CustomSort) accepts a list and a sorting function as arguments.

The sorting method is selected at runtime using command-line arguments.

This design demonstrates:

functional abstraction

algorithm comparison

modular code structure

▶️ How to Run

Ensure Python 3 is installed.

Run the program from the terminal:

python sorting.py "[list]" sorting_method

Example:
python sorting.py "[5, 3, 8, 1, 2]" merge

Output:
[1, 2, 3, 5, 8]

🔍 Available Sorting Methods
Method Name	Algorithm Used
bubble	Bubble Sort
insertion	Insertion Sort
selection	Selection Sort
merge	Merge Sort

If an invalid method is provided, the program exits with an error message.

🧪 Notes on Implementation

Bubble Sort performs a single pass through the list per function call.

Merge Sort follows a recursive divide-and-merge strategy.

Selection Sort uses a recursive approach with a helper function to locate the minimum element.

Insertion Sort performs in-place sorting using shifting.

⚠️ Limitations

Input is parsed using eval, which assumes trusted input.

Some algorithms mutate the input list.

Merge Sort uses list popping from the front, which is not optimal for large lists.

These choices were made for clarity and learning purposes.

🚀 Possible Improvements

Replace eval with safer input parsing

Optimize Merge Sort using indices instead of list popping

Add timing comparisons between algorithms

Extend to support custom comparator functions

📚 Language Used

Python 3
