# Overview #

## The Island Perimeter Problem ##
Prime Game is a competitive game where the winner is determined based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

Here are the key concepts and resources necessary to complete this project successfully.

### Concepts Needed: ###
#### Prime Numbers ####
- Understanding what prime numbers are.
- Efficient algorithms for identifying prime numbers within a range.

#### Seive of Erastosthenes: ####
- An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.

#### Game Theory: ####
- Basic principles of competitive games where players take turns and the concept of optimal play.
- Understanding win conditions and strategies that lead to a win or loss.

#### Dynamic Programming/Memoization ####
- Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.

#### Python Programming: ####
- Loops and conditional statements for implementing game logic and algorithms.
- Arrays and lists for storing the integers and tracking removed numbers.

## Reference Materials/Resources ##
#### Prime Numbers and Sieve of Eratosthenes: ####
- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers): Introduction to prime numbers. 
- [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/): A step-by-step guide to implementing the sieve algorithm in Python.
#### Game Theory Basics: ####
- [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp): A simple explanation of game theory and strategic decision-making.
#### Dynamic Programming: ####
- [What Is Dynamic Programming With Python Examples](https://skerritt.blog/dynamic-programming/): An introduction to dynamic programming with Python examples.



## Folder Details ###
- **Date Created:** Wed Dec 11 2024 11:33am
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
- **Released:** Mon Dec 09 2024 - 6am.
  - **1st Deadline:** Fri Dec 13 2024 - 6am.
  - **Duration:** 96hrs (4 days)
  - **Completed:** TBD.


## Files  ###
*This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|----------------------------------------------------|---------------------------------------|
| 1. | [0-prime_game.py](https://github.com/thecypherzen/alx-interview/tree/main/0x09-island_perimeter/0-prime_game.py) | Maria and Ben are playing a game. Given a set of consecutive integers `starting from 1 up to and including n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.<br/> They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is. <br/> **Example** <br/><br/>`x = 3, nums = [4, 5, 1]`<br/>First round: `4`<ul><li>Maria picks `2` and removes `2`, `4`, leaving `1`, `3`</li> <li>Ben picks `3` and removes `3`, leaving `1` </li> <li> Ben wins because there are no prime numbers left for Maria to choose </li> </ul><br/> Second round: `5` <ul> <li>Maria picks 2 and removes 2, 4, leaving 1, 3, 5</li> <li> Ben picks 3 and removes 3, leaving 1, 5 </li> <li> Maria picks 5 and removes 5, leaving 1</li>  <li>Maria wins because there are no prime numbers left for Ben to choose</li></ul><br/> Third round: `1`<ul><li>Ben wins because there are no prime numbers for Maria to choose</li></ul> |
