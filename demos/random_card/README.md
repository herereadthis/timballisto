# Random card from the street

Imagine if once a day, you picked up a random card off the street. What is the expected number of days it will take before you have a complete deck?

Without getting into too much detail, this question is a variation of the coupon collector's problem and is related to harmonic numbers: n * H<sub>n</sub>, or `52 * H_52 = 236`. [Here is the solution](http://www.wolframalpha.com/input/?i=52+*+H_52)

Run a simulation to see if the average number from X trials will match 236.

```bash
python3 demo.py
```