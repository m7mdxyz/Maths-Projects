# Transportation Problem Solver

A console application in C++ that solves the **Transportation Problem** using the **North-West Corner Method**. This project was completed as a course assignment for **MATH 329: Operations Research**.

---

## The Problem

The Transportation Problem is a classic linear programming problem aimed at finding the most cost-effective way to distribute goods from various sources to different destinations. The goal is to minimize the total shipping cost while satisfying all supply and demand constraints.

---

## The Solution

This program implements the **North-West Corner Method** to find an initial **Basic Feasible Solution (BFS)**. The method is a systematic, step-by-step algorithm that begins at the top-left cell of the transportation tableau (the "north-west corner") and allocates as much as possible to that cell before moving to the next one.

The application prompts the user to input the number of sources, destinations, and the corresponding supply, demand, and cost data. It then calculates and displays the total cost of the initial solution.

---
