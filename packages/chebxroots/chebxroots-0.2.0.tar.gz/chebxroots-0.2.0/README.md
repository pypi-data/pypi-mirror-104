# Scientific Computing Chebychev Roots 
 This project is part of the "Scientific Computing - Practical"-lecture.
 Its aim is to to implement an algorithm to find the roots of a function by approximating the function using Chebychev polynomials and then using polynomial rootfinding methods.

 We have written the function **chebxroots** which computes the roots of a general function on a given interval. 

 The idea is based on a paper by Boyd [1]. We want to expand a general function as a Chebychev series.
First, the Chebychev points are computed at which we evaluate our original function. Subsequently we compute the Chebychev coefficients $`\alpha_j`$ using an interpolation matrix. 

 The form of our approximated function has the form $`f_N = \sum_{j=0}^N \alpha_j T_j(x)`$ where the $`T_j`$ are the Chebychev polynomials and the $`\alpha_j`$ the corresponding Chebychev coefficients 

When approximating we need to determine an $`N`$ which is the degree up to which we approximate our function with a Chebychev series. We use the criterion $`\sum_{j=[2/3N]}^N \vert \alpha_j \vert < \varepsilon`$.

To convert the truncated Chebychev series to a polynomial there are two possibilities. 
1. Convert to powers: We convert the series to a function of the form $`f_N = \sum_{j=0}^N \beta_j x^j`$

2. Degree doubling: We convert the series to a function of the form $`h_{2N} = \alpha_0 z^N + \sum_{j=1}^N \alpha_j(z^{N-j} + z^{N+j})`$

Now we can apply an already implemented polynomial rootfinder. 

If the optimal $`N`$ is higher than the recommended values from the paper, we split the interval into smaller subintervals and apply the above steps to each subinterval.

In the class **prefs** it is possible to change some parameters of the function such as the maximal degree of the polynomials or the maximal number of subintervals. It is also possible to switch off the splitting into subintervals or switch on memoization in evaluating our input function at Chebychev points. 

## Install Package

To use **chebxroots** install the package by running the following command in the command line.
```console
pip install chebxroots
```
For more information see [2].
 
## Example

In example.py you can find a demo of **chebxroots**. There, it is shown how to use chebxroots and how to change some settings using **prefs**.

Run the example with
```console
example.py
```
 

## Links

[1] (https://www.researchgate.net/publication/220179204_Computing_Zeros_on_a_Real_Interval_through_Chebyshev_Expansion_and_Polynomial_Rootfinding)

[2] (https://pypi.org/project/chebxroots/)
