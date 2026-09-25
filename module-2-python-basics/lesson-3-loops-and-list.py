"""
Module 2 — Lesson 3: Loops & Lists
Student: John Brian O. Pecson
Date: 9/25/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
- This topic talks about list and loops. Lists are like multiple variables, kind of like a file organizer with many information inside.
Loops are repeated lines of code that runs with a condition.

============================================
KEY VOCABULARY
============================================
- list: a collection of variables
- for loop: a loop that goes through one line or item at a time
- while loop: runs on a condition like while the condition is true, the block of code will continue running
- index: a position of a certain variable in a list
- iteration: 
- condition: An expression that is checked as True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
scores = [12, 8, 15, 10]

total = 0

for score in scores:
    print("Points scored:", score)
    total = total + score

print("Total points:", total)




"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
- I always tend to forget that the index starts at 0 and not at 1, and I keep forgetting and thinking that 1 is the first one.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
