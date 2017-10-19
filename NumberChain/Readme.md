# NumberChain

**About**
 
My attempt (hopefully I'll get around to completing this) at this interesting number chain problem.

The idea is to form the biggest chain using the numbers from 1 - 100 such that for any pair of adjacent numbers, one of them is a factor of the other. 

Problem first encountered here : https://fivethirtyeight.com/features/pick-a-number-any-number/

***Observations***

These are unconfirmed observations based on smaller sets, further research required:

1. Prime numbers whose first multiple is outside the set is always excluded (except for one of them, which is always paired with 1)
2. Solution usually has a 1 paired with a prime number at one end of the path
3. It's possible to speculate then that it's impossible to form a cycle with such a chain of numbers
4. Prime numbers can only connect to their multiples (This might seem obvious, but this fact should be helpful when it comes to generating solutions in a cheesy manner)
