## 2. The Empirical Probability ##

'''Just like in our example above, we tossed a coin 100 times and got heads 56 times. Calculate the probability of getting tails using the formula above and assign the result to p_tail.'''
p_tail = (100 - 56) / 100

'''We rolled a regular six-sided die 200 times and:

1. We got a six 28 times. Calculate the probability of getting a 6 when rolling a six-sided die. Assign the result to p_six.'''
p_six = 28 / 200

'''2. We got an odd number (a 1, a 3, or a 5) 102 times. Calculate the probability of getting an odd number when rolling a six-sided die. Assign the result to p_odd.'''
p_odd = 102 / 200

print(p_tail)
print(p_six)
print(p_odd)

## 3. Probability as Relative Frequency ##

'''We tossed a coin 300 times and got tails 162 times.
- Find the probability of getting heads. Assign your result to p_heads_1.
- Transform the probability in p_heads_1 to a percentage value. Assign the result to percentage_1.'''
p_heads_1 = (300 - 162) / 300
percentage_1 = p_heads_1 * 100

'''In a different trial, we tossed a coin 5,000 times and got tails 2,450 times.
- Find the probability of getting heads. Assign your result to p_heads_2.
- Transform the probability in p_heads_2 to a percentage value. Assign the result to percentage_2.'''
p_heads_2 = (5000 - 2450) / 5000
percentage_2 = p_heads_2 * 100

## 4. Repeating an Experiment ##

# INITIAL CODE
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'
    
probabilities = []
heads = 0

for n in range(1, 10001):
    outcome = coin_toss()
    
    if outcome == 'HEAD':
        heads += 1
        
    current_probability = heads / n
    probabilities.append(current_probability)
    
print(probabilities[:10])
print(probabilities[-10:])

## 5. The True Probability Value ##

'''An insurance company conducted a study with 200 individuals, and found that:
- 87 individuals opted for at least a life insurance policy.
- 40 individuals opted for at least life and car insurance policies.
- 63 individuals opted for at least a house insurance policy.
- 160 individuals opted for at least one type of insurance policy.

We can't predict people's choices with certainty, so an individual choosing to buy an insurance policy is a random experiment. 200 individuals were part of the study, so you can consider the random experiment was performed 200 times. Find:'''

'''P(L): The probability that a new customer opts for at least a life insurance. Assign your answer to a variable named p_l.'''
p_l = 87 / 200

'''P(L and C): The probability that an individual opts for at least a life and a car insurance policy. Assign your answer to a variable named p_l_and_c.'''
p_l_and_c = 40 / 200

'''P(H): The probability that an individual opts for at least a house insurance policy. Assign your answer to a variable named p_h.'''
p_h = 63 / 200

'''P(NO): The probability that an individual opts for no insurance at all. Assign your answer to a variable named p_no.'''
p_no = (200 - 160) / 200

## 6. The Theoretical Probability ##

'''Find the theoretical probability of getting a 5 when rolling a six-sided die. Assign your answer to p_5.'''
p_5 = 1 / 6

'''Tossing a coin twice has four possible outcomes (assume all the outcomes are equally likely):
- Heads on the first toss and heads on the second toss (HH).
- Heads on the first toss and tails on the second (HT).
- Tails on the first toss and heads on the second (TH).
- Tails on the first toss and tails on the second (TT).
Find:
P(HT): Assign your result to p_ht.'''
p_ht = 1 / 4

'''P(TT): Assign your result to p_tt.'''
p_tt = 1 / 4

## 7. Events vs. Outcomes ##

'''Assume all the outcomes of rolling a six-sided die have an equal chance of occuring. Calculate as proportion the probability of the following events:
- We get an even number — assign your answer to p_even.
- We get an odd number different than 3 — assign your answer to p_odd_no_3.
- We get an odd number greater than 5 — assign your answer to p_odd_greater_5.'''
p_even = 3 / 6
p_odd_no_3 = 2 / 6
p_odd_greater_5 = 0 / 6

## 8. A Biased Die ##

'''In a jar of 100 marbles, 90 marbles are red and 10 are blue. Find as a proportion:
- The probability of randomly selecting a blue marble from the jar — assign your answer to p_blue.'''
p_blue = 10 / 100 

'''The probability of randomly selecting a red marble from the jar — assign your answer to p_red.'''
p_red = 90 / 100