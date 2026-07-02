# Intro to CP & Complexity

**Category:** Basics  
**Difficulty:** <span style="color: #059669; font-weight: 600;">● Very Easy</span>

---

This topic covers the fundamentals of Competitive Programming, the metrics we use to judge algorithm efficiency, and how to analyze code complexity.

## What is Competitive Programming?

Competitive programming is a mind sport that combines two distinct but equally important skills:

1. **Designing algorithms**: Requiring problem-solving abilities and mathematical thinking.
2. **Implementing them**: Writing the code correctly and efficiently under tight time pressure.

![What is CP](../images/intro-to-cp/intro-1.png)

In competitive programming, you are given a problem statement accompanied by strict execution time and memory limits. Your goal is to write a program that solves the problem correctly and within these bounds.

Once submitted, your solution is judged automatically by an online system. It is either accepted or it is not — there is no partial credit, and no "almost correct" solutions.

## Why Competitive Programming?

Engaging in competitive programming offers several key benefits:

- **Tech Career Preparation**: Technical interviews at top technology companies test exactly these problem-solving and implementation skills.
- **Mathematical Growth**: It builds mathematical maturity and refines your ability to reason under constraints.
- **Problem-Solving Mindset**: You are not just learning a list of algorithms; you are building a structured way of thinking.

As Antti Laaksonen states in the *Competitive Programmer's Handbook*:
> “It takes a long time to become a good competitive programmer, but it is also an opportunity to learn a lot.”

## The Competition Ladder

The competitive programming landscape is structured like a ladder, scaling from local challenges to international arenas.

![The Competition Ladder](../images/intro-to-cp/intro-2.svg)

## The Online Judge

In competitive programming, you submit your code through a web interface. The online judge compiles your code and runs it against a set of hidden test cases. You never get to see these test cases; you must think of edge cases and verify your solution’s correctness on your own before submitting.

Every submission returns exactly one of the following verdicts:

| Verdict | Meaning |
|---|---|
| Accepted | Correct output, within time limit |
| Wrong Answer | Incorrect output on at least one case |
| Time Limit Exceeded | Correct logic, too slow |
| Runtime Error | Crash — division by zero, out of bounds, etc. |
| Compilation Error | Code didn’t compile |

## Your First Problem

To understand how to read problem constraints and construct solutions, we begin by analyzing a starter problem.

![Your First Problem](../images/intro-to-cp/intro-3.png)

## Algorithms & Data Structures

Every solution in competitive programming is composed of an algorithm working in tandem with one or more data structures. If you modify one, the entire performance of your solution changes. An algorithm is only as fast as the data structures it runs on.

- **Algorithm**: A step-by-step method to solve a problem. It must be both correct and efficient. Think of it as *the recipe* — it defines what actions to perform and in what order.
- **Data Structure**: A concrete way to organize and store data so that operations can be performed efficiently. It is *the container*, and its shape determines which operations are cheap and which are expensive.
