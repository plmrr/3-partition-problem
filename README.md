# Problem
The 3-partition problem is a strongly NP-complete problem in computer science. The problem is to decide whether a given multiset of integers can be partitioned into triplets that all have the same sum. More precisely:

- The input to the problem is a multiset S of n = 3m  positive integers. The sum of all integers is mT. 
- The output is whether or not there exists a partition of S into m triplets S1, S2, …, Sm such that the sum of the numbers in each one is equal to T. The S1, S2, …, Sm must form a partition of S in the sense that they are disjoint and they cover S.
The 3-partition problem remains strongly NP-complete under the restriction that every integer in S is strictly between T/4 and T/2.
Solving 3-partition problem using gurobi solver and simulated annealing
[Source](https://en.wikipedia.org/wiki/3-partition_problem)

# Example
Solving problem for example data using simulated annealing & Gurobi solver

Input: [55, 17, 33, 44, 23, 15, 54, 31, 7, 53, 40, 28]

Output: [[53, 40, 7], [23, 33, 44], [54, 15, 31], [28, 17, 55]]
