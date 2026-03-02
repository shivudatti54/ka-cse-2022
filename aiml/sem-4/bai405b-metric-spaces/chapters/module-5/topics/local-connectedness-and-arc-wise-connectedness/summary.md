# **Local Connectedness and Arc-Wise Connectedness**

### Definitions

- **Local Connectedness**: A space $X$ is locally connected if for every $x\in X$ and every open set $U$ containing $x$, there exists a connected open set $V$ such that $x\in V\subseteq U$.
- **Arc-Wise Connectedness**: A space $X$ is arc-wise connected if for any two points $x,y\in X$, there exists a continuous arc $[a,b]\subseteq X$ such that $x\in [a,b]$ and $y\in [a,b]$.

### Important Formulas

- **Urysohn's Lemma**: If $X$ is a normal space and $A,B$ are disjoint closed sets, then there exists a continuous function $f:X\to [0,1]$ such that $f(A)=0$ and $f(B)=1$.
- **Hausdorff Dimension**: The Hausdorff dimension of a set $S\subseteq X$ is defined as $\inf\{s\in\mathbb{R}:\text{the Hausdorff measure of }S\text{ is zero}\}$.

### Theorems

- **Theorem 1**: If $X$ is a metric space and $A$ is a closed set, then $X\setminus A$ is open if and only if $A$ is locally connected.
- **Theorem 2**: If $X$ is a metric space and $A$ is a closed set, then $X$ is arc-wise connected if and only if $X\setminus A$ is locally connected.

### Key Points

- Local connectedness is a weaker property than arc-wise connectedness.
- Urysohn's Lemma is a key tool in proving theorems about local connectedness and arc-wise connectedness.
- The Hausdorff dimension is a useful concept in understanding the connectedness of sets in metric spaces.
- Examples:

* A metric space with two connected components is arc-wise disconnected but locally connected at the boundary.
* A metric space with a closed set that is locally connected is arc-wise connected.
