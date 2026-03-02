# Auctions: Auctions with an Arbitrary Distribution of Valuations

## **Introduction**

Auctions are a fundamental mechanism for allocating scarce resources in economic systems. In this study material, we will focus on auctions with an arbitrary distribution of valuations, which is a classic problem in algorithmic game theory. We will explore the definitions, key concepts, and examples of this topic, as well as discuss the motivations and general definitions of auctions in Bayesian games.

## **Definition of an Auction**

An auction is a mechanism for allocating a single item or resource to a group of bidders. The bidders submit their bids, which are their proposed prices for the item, and the auctioneer determines the winner based on the highest bid.

## **Types of Auctions**

There are several types of auctions, including:

- **First-Price Auction**: The winner pays the price of their bid.
- **Second-Price Auction**: The winner pays the second-highest bid.
- **Symmetric Auction**: All bidders pay the same price.

## **Auctions with an Arbitrary Distribution of Valuations**

In an auction with an arbitrary distribution of valuations, each bidder has a private valuation for the item, which is not known by the other bidders. The objective of this study material is to design an algorithm that can determine the winner of the auction, given the distribution of valuations.

## **Key Concepts**

- **Valuation Distribution**: The probability distribution of the valuations of the bidders.
- **Expected Value**: The expected value of a bid, which is the sum of the product of each possible valuation and its probability.
- **Bayes' Rule**: A formula for updating the probability distribution of a variable based on new evidence.

## **Bayes' Rule in Auctions**

Bayes' rule can be used to determine the expected value of a bid, given the distribution of valuations. Let's assume that the bidders have private valuations for the item, denoted by $v_i$, and the distribution of valuations is $P(v_i)$. The expected value of a bid, denoted by $E[b_i]$, is given by:

$$E[b_i] = \sum_{v_i} v_i P(v_i)$$

Using Bayes' rule, we can update the probability distribution of the winner based on the bids:

$$P(w_i | b_i) = \frac{P(b_i | w_i) P(w_i)}{\sum_{w_j} P(b_i | w_j) P(w_j)}$$

where $w_i$ is the winner and $P(w_i)$ is the prior probability of the winner.

## **Example 1**

Suppose we have three bidders, Alice, Bob, and Charlie, who have private valuations for a car. The distribution of valuations is:

| Bidder  | Valuation |
| ------- | --------- |
| Alice   | 10,000    |
| Bob     | 8,000     |
| Charlie | 12,000    |

The expected value of a bid is:

$$E[b_i] = (10,000 + 8,000 + 12,000) / 3 = 10,667$$

Using Bayes' rule, we can update the probability distribution of the winner based on the bids. Suppose Alice bids 10,500 and Bob bids 8,200. The updated probability distribution of the winner is:

| Winner  | Probability |
| ------- | ----------- |
| Alice   | 0.6         |
| Bob     | 0.3         |
| Charlie | 0.1         |

## **Example 2**

Suppose we have five bidders, David, Emily, Frank, George, and Helen, who have private valuations for a house. The distribution of valuations is:

| Bidder | Valuation |
| ------ | --------- |
| David  | 200,000   |
| Emily  | 180,000   |
| Frank  | 220,000   |
| George | 160,000   |
| Helen  | 240,000   |

The expected value of a bid is:

$$E[b_i] = (200,000 + 180,000 + 220,000 + 160,000 + 240,000) / 5 = 208,000$$

Using Bayes' rule, we can update the probability distribution of the winner based on the bids. Suppose David bids 210,000 and Emily bids 190,000. The updated probability distribution of the winner is:

| Winner | Probability |
| ------ | ----------- |
| David  | 0.6         |
| Emily  | 0.3         |
| Frank  | 0.1         |
| George | 0           |
| Helen  | 0           |

## **Conclusion**

Auctions with an arbitrary distribution of valuations are a fundamental problem in algorithmic game theory. By using Bayes' rule, we can design algorithms that can determine the winner of the auction, given the distribution of valuations. The examples above illustrate how to apply Bayes' rule to determine the expected value of a bid and update the probability distribution of the winner.
