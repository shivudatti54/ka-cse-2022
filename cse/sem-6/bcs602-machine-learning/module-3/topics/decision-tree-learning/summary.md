# Decision Tree Learning

## Overview

Decision tree learning algorithms build tree models through recursive partitioning of the feature space. The learning process selects optimal splits to maximize information gain or minimize impurity, creating interpretable rules for classification and regression tasks.

## Key Points

- **Learning Process**: Recursive splitting - select best feature and threshold, split data, repeat on subsets until stopping criteria met
- **Impurity Measures**: Gini Impurity (1 - Σpi²), Entropy (-Σpi\*log₂pi), Misclassification Error; lower impurity = purer node
- **Information Gain**: IG = Impurity(parent) - Weighted_Avg(Impurity(children)); higher IG = better split
- **Splitting Criteria**: Numerical features (find optimal threshold), Categorical (subset or one-vs-rest)
- **Stopping Conditions**: Max depth reached, min samples per node, all samples same class, no information gain
- **Pruning**: Pre-pruning (early stopping) vs Post-pruning (grow full tree, then prune); cost-complexity pruning balances size and error

## Important Concepts

- Greedy algorithm: chooses best split at each step without lookahead (fast but suboptimal)
- Gain Ratio: normalizes Information Gain by split information; reduces bias toward many-valued features
- Variance Reduction: regression trees minimize MSE instead of impurity
- Ensemble methods (Random Forest, Gradient Boosting) overcome single tree instability

## Notes

- Memorize Gini formula (1 - Σpi²) and Entropy formula (-Σpi\*log₂pi)
- Calculate Information Gain: parent impurity minus weighted children impurity
- Understand greedy nature: locally optimal splits may not give globally optimal tree
- Pruning types: pre-pruning (stop early) vs post-pruning (grow then trim)
- Know stopping criteria and their impact on overfitting/underfitting
