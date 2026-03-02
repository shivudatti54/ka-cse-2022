# **Chap-12 (12.1-12.3.1) Morphological Image Processing: Preliminaries, Erosion and Dilation, Opening and Closing, Hit-or-Miss Operations**

## **Preliminaries**

- **Definition:** Morphological image processing is a branch of image processing that deals with the analysis and manipulation of image features using mathematical transformations.
- **Theorems:**
  - **Minkowski's theorem:** A morphological operation can be viewed as a mapping between sets.
  - **Minkowski's inequality:** The Minkowski sum of two sets is not necessarily connected.

## **Erosion and Dilation**

- **Definition:** Erosion is the morphological operation that reduces the size of an object, while dilation is the operation that enlarges an object.
- **Erosion formula:**
  - $E_{B}(A) = \bigcap_{(x,y) \in B} B_{x,y} (A)$
- **Dilation formula:**
  - $D_{B}(A) = \bigcup_{(x,y) \in B} B_{x,y} (A)$
- **Properties:**
  - Erosion is a decreasing operation.
  - Dilation is an increasing operation.

## **Opening and Closing**

- **Definition:** Opening is the combination of erosion and dilation, while closing is the combination of dilation and erosion.
- **Opening formula:**
  - $O_{B}(A) = E_{B}(D_{B}(A))$
- **Closing formula:**
  - $C_{B}(A) = D_{B}(E_{B}(A))$
- **Properties:**
  - Opening is a decreasing operation that removes noise.
  - Closing is an increasing operation that fills holes.

## **Hit-or-Miss Operations**

- **Definition:** Hit-or-miss operations are morphological operations that test for the presence of a specific shape in an image.
- **Formula:**
  - $T_{A,B} (A) = \bigcap_{(x,y) \in A} B_{x,y} (A) \cap \bigcap_{(x,y) \in B} A_{x,y} (B)$
- **Properties:**
  - Hit-or-miss operations can be used to detect specific shapes or features in an image.

## **Important Formulas and Definitions**

- **Minkowski distance:** $d_{M} (A,B) = \inf \{ \lambda > 0 | B_{\lambda} (A) \subseteq A \text{ and } B_{\lambda} (B) \subseteq B \}$
- **Minkowski sum:** $A \oplus B = \{ x+y | x \in A \text{ and } y \in B \}$
