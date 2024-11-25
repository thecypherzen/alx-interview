# Overview #

## Must Know for Pascal's Triangle ##
To successfully implement the Pascal's triangle in Python, it's necessary to revise the following Python concepts.

### Lists and List Comprehensions: ###

- Understand how to create, access, modify, and iterate over lists.
- Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.

### Functions:# 
- Know how to define and call functions.
- Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.

### Loops:
- Use for and while loops to iterate through sequences.
- Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.

### Conditional Statements:
- Apply if, elif, and else conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).

### Recursion (Optional):
- While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
- Recognize base cases and recursive cases for a function that generates the triangle’s rows.

### Arithmetic Operations:
- Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.

### Indexing and Slicing:
- Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.


### Memory Management:
- Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.

### Error and Exception Handling (Optional):
- Use try-except blocks as needed to handle potential errors, such as invalid input types or values.

### Efficiency and Optimization:
- Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
- Evaluate and apply optimizations to improve the performance of the solution.

## My Approach ##
- I used the iterative approac because the recursive approach for this would not yield any significant benefit to the efficiency of the solution and could possible load the stack more than the iterative solution
- I also used a memoized cache of rows in order to re-use them once they've been generated before.
- I didn't revisit the code to make it more efficient, so pardon me if you find some inefficient stuff in the solution - I'd fix it on a live project

## Reference Materials ##
The following can be used for referencing these areas, curated for optimized understanding:
- [What is Pascal’s triangle](https://www.cuemath.com/algebra/pascals-triangle/)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?feature=shared&v=0iMtlus-afo)
- [What are Python Algorithms](https://builtin.com/data-science/python-algorithms)
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=1qw5ITr3k9E)

## Folder Details ###
- **Date Created:** Mon Nov. 25 2024 5:47pm
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
- **Released:** Mon Sept 30 2024 - 6am.
  - **1st Deadline** Fri Oct 4 2024 - 6am.
  - **Duration:** 96hrs (4 days)
  - **Completed:** Mon Nov 25 2024 - 7:20pm


## Files  ###
*This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|----------------------------------------------------|---------------------------------------|
| 1. | [0-pascal_triangle.py](https://github.com/thecypherzen/alx-interview/tree/main/0x00-pascal_triangle/0-pascal_triangle.py) | A function that generates a list of lists that represent Pascal's triangle of size n. |
| 2. | [main_0.py](https://github.com/thecypherzen/alx-interview/tree/main/0x00-pascal_triangle/main_0.py) | Test for pascal's triangle implementation. | 
