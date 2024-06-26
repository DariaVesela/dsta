---
lang: en
author: DSTA
title: "Computing Eigenpairs"
---

<!-------------------------------------------------------------->
#  From paper to Python

## Background material

This unit is less about computing than about learning/revising how eigehpairs are computed in Mathematics.

Goal: give a feeling of how these almost-magical entities that are eigenpairs do come to help us understand *latent trends in data.*

Please cover this lab in class (if time allows) or at home with pen and paper, in the rest of the class e-pairs will always be given by the `numpy.linalg` submodule.

## Exercise

From the [MMDS](http://mmds.org/), Ch. 11, pp. 385-387.

Let, $M$ be a square matrix. 

Let $\lambda$ be a constant and $\mathbf{e}$ be a non-zero column vector with the same number of rows as $M$.

Then $\lambda$ is an e-value of $M$ and $\mathbf{e}$ is its corresponding e-vector if 

$$M\mathbf{e} = \lambda \mathbf{e}.$$

This can be reformulated as $(M-\lambda I)e=0.$

## A worked-out ex.

Let

$M=
\left[
\begin{matrix}
 3 & 2 \\
 2 & 6
\end{matrix}
\right]$

. . .

Then

$M - \lambda I = \left[
\begin{matrix}
 3- \lambda & 2 \\
 2 & 6- \lambda
\end{matrix}
\right]$

## The determinant

The determinant of $M- \lambda I$ is $(3- \lambda)(6- \lambda)-4$.

__What are the values of $\lambda$ that make the determinant=0?__

-----

 $|M- \lambda I|=0$ has two roots: $\lambda_1 = 7$, and $\lambda_2 = 2$.

Now we can discover the associated eigenvetors.

Recall that $M\mathbf{e} = \lambda \mathbf{e}$

At the moment, $\mathbf{e}$ is unknown: $[x, y]^T$.

Let's substitute $\lambda = 7$ in the eq.

$\left[
\begin{matrix}
 3 & 2 \\
 2 & 6
\end{matrix}
\right]\cdot\left[
\begin{matrix}
 x \\
 y
\end{matrix}
\right]=7\cdot \left[
\begin{matrix}
 x \\
 y
\end{matrix}
\right]$

-----

by multiplying matrix and vector we get two equations:

$3x+2y = 7x$

$2x+6y = 7y$

Both of the equations really say that $y = 2x$.

-----

Infinte solutions are possible, let's fix $\mathbf{e_1}=$

$\left[
\begin{matrix}
 1 \\
 2
\end{matrix}
\right]$

But $\mathbf{e_1}=$ vector, since its norm, i.e., the sum of the squares of its components, is 5, not 1.

Thus to get the unit vector in the same direction, we divide each components by $\sqrt{5}$. 

-----

So the principal (7 is the max $\lambda$ value) e-vector is  

$\left[
\begin{matrix}
 1/\sqrt{5} \\
 2/ \sqrt{5}
\end{matrix}
\right]$

## Can we solve it for the second eigenpair?

```python
import numpy as np

from numpy import linalg as LA

M = np.array([[3,2],[2,6]])

print(M)

w, v = LA.eig(M)

print(w)
print(v)
```

---

<!-- ------------------------------ -->
# Reference material: The PCA technique

## Objective

What if we want to have less dimensions while still retaining the differences between data points?

In the Iris example:

-some 2D data plot collapsed datapoints very close to each other (hard to classify them)

-other data plots showed scattered ponts: easier to classify data

Spectral analysis leads to Principal Component Analysis

## A new reference system

From [MMDS](http://mmds.org/), Ch. 11, pp. 391-396.

Let $M$ represents the dataset.

If we find e-vectors of $MM^T$ or $M^T M$, then the matrix made up of these e-vectors will represent a rigid rotation in the high dimensional space:

unlike the Mona lisa example, distances/shapes are unchanged.

Result: the axis corresponding to the principal e-vector is the one along which the points *are most spread out.*

-----

Try the following program and observe the phenomenon.

```python
 M=np.array([[1,2], [2,1], [3,4], [4,3]])

 MtM = np.matmul(M.T, M)

 print(MtM)

 w,v = LA.eig(MtM)

 print(w)
 print(v)
 
 ME = np.matmul(M, v)

 print(ME)
```

## Iris example, I

The principal e-pair (see above) gives the direction of most spread

![Iris rotation](./imgs/zm-fig71-iris-rotation.png)

## Iris example, II

The principal e-pair (see above) gives the best 3D-to-1D approximation

![Iris compression](./imgs/zm-fig72-iris-compression.png)
