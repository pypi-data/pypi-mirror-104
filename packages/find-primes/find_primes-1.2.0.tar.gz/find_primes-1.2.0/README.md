Find Primes is a library to find all kinds of primes.

**Install**
```shell
pip install find-primes
```
**Twin Primes**

https://en.wikipedia.org/wiki/Twin_prime

A twin prime is a prime number that is either 2 less or 2 more than another prime number.

Example: Find all twin primes below 1000.
```python
from find_primes import find_twins
print(find_twins(1000))
```

**Palindrome Primes**

https://en.wikipedia.org/wiki/Palindromic_prime

A palindrome prime is a prime number that is also a palindrome number.

Example: Find all palindrome primes below 1000.
```python
from find_primes import find_palindromes
print(find_palindromes(1000))
```

**Emirps**

https://en.wikipedia.org/wiki/Emirp

An emirp is a prime number that results in a different prime when its decimal digits are reversed.

Example: Find all emirps below 1000.
```python
from find_primes import find_reverse
print(find_reverse(1000))
```

**Primes in Arithmetic Progression**

https://en.wikipedia.org/wiki/Primes_in_arithmetic_progression

Primes in arithmetic progression are any sequence of at least three prime numbers that are consecutive terms in an arithmetic progression.

Example: Find all primes in arithmetic progression below 1000.
```python
from find_primes import find_arithmetic_prime_progressions
print(find_arithmetic_prime_progressions(1000))
```

**Mersenne Primes**

https://en.wikipedia.org/wiki/Mersenne_prime

A mersenne prime is a prime number that is one less than a power of two.

Example: Find all mersenne primes below 600000.
```python
from find_primes import find_mersenne_primes
print(find_mersenne_primes(600000))
```

**Fermat Pseudoprime**

https://en.wikipedia.org/wiki/Fermat_pseudoprime

A fermat pseudoprime is a pseudoprime that satisfies fermat's little theorem.

Example: Find all fermat pseudoprimes below 1000.
```python
from find_primes import find_fermat_pseudoprime
print(find_fermat_pseudoprime(1000))
```