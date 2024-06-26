---
lang: en
author: "Singular-value Decomposition"
title: DSTA
---

<!-------------------------------------------------------------->
# Foundations

## Remember eigenpairs?

Matrix $A$ has a real $\lambda$ and a vector $\mathbf{v}$ s.t.

$$A\mathbf{v} = \lambda \mathbf{v}$$

We think of A as __scaling__ space with a factor $\lambda$ in direction $\mathbf{v}$.

Singular values uncover categories and their strenghts.

The Eigen-decomposition of a square matrix seen in [Goodfellow et al.] can be extended to arbitrary matrices!

-----

![Epairs](./imgs/eigenpairs.png)

![Epairs 2](./imgs/eigenpairs-caption.png)

-----

We think of A as __scaling__ space with a factor $\lambda$ in direction $\mathbf{v}$.

$$
f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}
$$

For unit vectors the max (resp. min) of $f(\cdot)$ corresponds to $\lambda_1$ (resp. $\lambda_n$).

## Decompose the "effect" of A

Let the square matrix A have n  

- linearly-independent e-vectors $\{ \mathbf{v}^{(1)}\dots \mathbf{v}^{(n)}\}$

- corresponding e-values $\{\lambda_1 \ge \lambda_1 \ge \dots \lambda_n\}$. Then  

. . .  

$$
A = V \rm{diag}(\mathbf{\lambda}) V^{T}
$$

where $V = [\mathbf{v}^{(1)} \mathbf{v}^{(1)}\dots \mathbf{v}^{(n)}]$

-----

$\mathbf{\lambda} = [\lambda_1 \lambda_2\dots \lambda_n]$.

$$ \rm{diag}(\mathbf{\lambda}) = 
\begin{pmatrix}
\lambda_1 & 0 & \dots \\
0 & \lambda_2 & \dots\\
\vdots & \vdots & \ddots
\end{pmatrix}
$$

-----

$$ A = 
\begin{pmatrix}
\big\uparrow    \big\uparrow   &\vdots & \big\uparrow \\
\mathbf{v}^{1}  \mathbf{v}^{2} &\dots  & \mathbf{v}^{n}\\
\big\downarrow  \big\downarrow &\vdots & \big\downarrow 
\end{pmatrix}
\begin{pmatrix}
\lambda_1 & 0 & \dots \\
0 & \lambda_2 & \dots\\
\vdots & \vdots & \ddots 
\end{pmatrix}
\begin{pmatrix}
\longleftarrow  &\mathbf{v}^{1}  & \longrightarrow \\
\longleftarrow  &\mathbf{v}^{2}  & \longrightarrow \\
\dots &\dots & \dots \\
\longleftarrow  &\mathbf{v}^{n}  & \longrightarrow \\
\end{pmatrix}
$$

## A general form for real symmetric Ms

$$
A = Q \Lambda Q^T
$$

where Q is an orthogonal matrix of e-vectors and $\Lambda$ is a diagonal m.

For repeated $\lambda$ values the decomposition is not unique.

<!-- ------------------------------------- -->
# Singular-Value Decomposition

## Definition

Singular-value decomp. generalises eigen-decomp.:

- any real matrix has one

- even non-square m. admit one

. . .

$$
A = V \rm{diag}(\mathbf{\lambda}) V^{-1}
$$

-----

$$
A_{(n \times m)} = U_{(n \times n)} D_{(n \times m)} V^T_{(m \times m)}
$$

- U is a orthogonal m. of *left-singular* (col.) vectors

- D is a diagonal matrix of *singular values*

- V is a orthogonal m. of *right-singular* (col.) vectors

. . .

Where does all this come from?

## Interpreting SV-decomposition

- cols. of U will be the e-vectors of $AA^T$

- $D_{ii}=\sqrt{\lambda_i}$ the i-th e-value of $A^T A$ (same for $AA^T$)

- cols. of V will be the e-vectors of $A^T A$

Please see $\S$ 2.7 of [[Goodfellow et al.]](https://www.deeplearningbook.org/contents/linear_algebra.html)

<!-- --------------------------------------------- -->
# Moore-Penrose pseudo-inverse

## Motivations

solve linear systems  

$$
A\mathbf{x} = \mathbf{y}
$$

for non-square (rectangular) matrices:

- n >m: the problem is overconstrained (no solution?)

- n < m: the problem is overparametrized (many sols.?)

## Ideal procedure

If A is squared (n=m) and non-singular ($|A|\neq 0$) then

$$
A\mathbf{x} = \mathbf{y}
$$

. . .

$$
A^{-1}A\mathbf{x} = A^{-1} \mathbf{y}
$$

. . .

$$
I\mathbf{x} = A^{-1} \mathbf{y}
$$

Compute once, run for different values of __y.__

## Define the pseudo-inverse

$$
A^+ = \lim_{\alpha\rightarrow 0} (A^TA + \alpha I)^{-1}A^T
$$

It is proved that $A^+ A \approx I$ so $A^+$ will work as the left-inverse of A

Consequence: over-constrained linear systems can now be solved w. approximation.

## SVD leads to approx. inversion

for the decomposition

$$
A = UDV^T
$$

$$
A^+ = VD^+ U^T
$$

where $D^+$, such that $D^+D=I$ is easy to calculate: D is diagonal.

-----

Does $A^+ A \approx I$?

Yes, because U and V are s. t. $U^T U = VV^T=I$.

. . .  

$$
VD^+ U^T \cdot UDV^T\ =
$$

. . .

$$
VD^+ I DV^T\ =
$$

. . .

$$
VD^+ DV^T \ =
$$

. . .

$$
V I V^T   = V V^T = I
$$
