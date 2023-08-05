# sequences

This is a simple Mathematical Module which is simple to use.  The module provides many of the most famous **sequences** from the On-Line Encyclopedia of International Sequences (OEIS) as Python Functions that returns a **list** of the first 'n' terms of that sequence. Help text is included for each function so that the user gets an idea of what to expect as the output to each function.

## Examples of Functions provided

- whole(n)
    > 0, 1, 2, 3, ..., n
- square(n)
    > 0, 1, 4, 9, ..., pow(n, 2)
- prime(n)
    > 2, 3, 5, 7, 11, ...
- fibonacci(n)
    > 0, 1, 1, 2, 3, ..., sum([F(n-1), F(n-2)])
- tribonacci(n)
    > 0, 1, 1, 2, 4, ..., sum([T(n-1), T(n-2), T(n-3)])
- recaman(n)
    > 0, 1, 3, 6, 2, ... \
    > T(n) = 0 if n == 0 \
    > T(n) = T(n-1) - n if positive and not already in sequence \
    > T(n) = T(n-1) + n otherwise

 And many more... Each function contains help text that can be accessed through help() in python to know more about it.

## Updates (0.0.5)
Minor bug fixes

## Updates (0.0.6)
Added many new sequences like:
- catalan(n)
    > 1, 1, 2, 5, 14, ..., comb(2n, n) / (n+1)
- aronson(n)
    > 1, 4, 11, 16, 24, ... \
    > formally, these numbers are obtained from the index of english letter "T" or "t" in the sentence: "T is the first, fourth, eleventh, sixteenth, ... letter in this sentence." ignoring spaces and punctuation marks
- cantral_polygon(n)
    > 1, 2, 4, 7, 11, ..., (pow(n, 2) + n + 2) / 2

## Reach out to me
If you face issues, contact me through my e-mail: knightt1821@gmail.com