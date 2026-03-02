# **Local Connectedness and Arc-Wise Connectedness**

## **Introduction**

In metric spaces, connectedness is a fundamental concept that studies the properties of a space that allow it to be "hugged" or "connected" in some sense. Two important aspects of connectedness are local connectedness and arc-wise connectedness. In this study material, we will explore these concepts, their definitions, and key properties.

## **Local Connectedness**

**Definition:** A metric space X is said to be locally connected at a point x ∈ X if for every open set U containing x, there exists an open set V containing x such that V ⊆ U.

**Example:** The set of real numbers with the standard metric is locally connected at every point. This is because for any open set U containing a point x, we can find an open set V containing x such that V ⊆ U.

**Key Properties:**

- **Local connectedness implies connectedness:** If a space is locally connected, then it is connected.
- **Local connectedness is a weaker property than connectedness:** A space can be locally connected but not connected (e.g., the set of integers with the standard metric).
- **Local connectedness is preserved under homeomorphisms:** If a homeomorphism φ between two metric spaces is defined, then φ(X) is locally connected if and only if X is locally connected.

## **Arc-Wise Connectedness**

**Definition:** A metric space X is said to be arc-wise connected if for any two points x, y ∈ X, there exists a continuous function f: [0, 1] → X such that f(0) = x and f(1) = y.

**Example:** The open interval [0, 1] with the standard metric is arc-wise connected. This is because for any two points x, y ∈ [0, 1], we can find a continuous function f: [0, 1] → [0, 1] such that f(0) = x and f(1) = y.

**Key Properties:**

- **Arc-wise connectedness implies connectedness:** If a space is arc-wise connected, then it is connected.
- **Arc-wise connectedness is a stronger property than local connectedness:** A space can be locally connected but not arc-wise connected (e.g., the set of real numbers with the standard metric).
- **Arc-wise connectedness is preserved under homeomorphisms:** If a homeomorphism φ between two metric spaces is defined, then φ(X) is arc-wise connected if and only if X is arc-wise connected.

## **Relationship Between Local Connectedness and Arc-Wise Connectedness**

- **Local connectedness implies arc-wise connectedness:** If a space is locally connected, then it is arc-wise connected.
- **Arc-wise connectedness does not imply local connectedness:** A space can be arc-wise connected but not locally connected (e.g., the set of real numbers with the standard metric).
