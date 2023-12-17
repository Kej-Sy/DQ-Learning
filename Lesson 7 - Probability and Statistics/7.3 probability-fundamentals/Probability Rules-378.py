## 1. Sample Space ##

'''We toss a normal coin two times. Find the sample space of this experiment and assign it to the list coin_toss_omega.

One of the outcomes is heads first, tails second. Abbreviate heads as H, tails as T, and assign the string 'HT' (heads first, tails second) to the list coin_toss_omega. Repeat this pattern for the other outcomes.'''
coin_toss_omega = {'HT', 'HH', 'TH', 'TT'}

## 2. Probability of Events ##

'''we'll consider a random experiment where we roll a fair six-sided die two times ("fair" means all outcomes have equal chances of occurring). The sample space of this experiment has 36 possible outcomes (all the sequences of numbers we can get from the two throws):

Ω={(1,1),(1,2),(1,3),...,(3,1),(3,2),...,(6,5),(6,6)}'''

#The sum of the two rolls is 6. Assign the probability to p_sum_6.
p_sum_6 = 5 / 36

#The sum of the two rolls is lower than 15. Assign the probability to p_lower_15.
p_lower_15 = 36 / 36

#The sum of the two rolls is greater than 13. Assign the probability to p_greater_13.
p_greater_13 = 0 /36

## 3. Certain and Impossible Events ##

'''we'll consider a random experiment where we roll a fair six-sided die two times ("fair" means all outcomes have equal chances of occurring). The sample space of this experiment has 36 possible outcomes (all the sequences of numbers we can get from the two throws):

Ω={(1,1),(1,2),(1,3),...,(3,1),(3,2),...,(6,5),(6,6)}'''

#The sum is either 2 or 4. Assign the probability as a proportion to p_2_or_4.
p_2_or_4 = 1 / 36 + 3 / 36

#The sum is either 12 or 13. Assign the probability as a proportion to p_12_or_13.
p_12_or_13 = 1 / 36 + 0 / 36

## 4. The Addition Rule ##

#The sum is either 5 or 9 — assign your answer to p_5_or_9.
p_5_or_9 = 4 / 36 + 4 / 36

#The sum is either even or less than 2 — assign your answer to p_even_or_less_2.
p_even_or_less_2 = 18 / 36 + 0 / 36

#The sum is either 4 or a multiple of 3 — assign your answer to p_4_or_3_multiple. Check the hint if you don't remember what a multiple is.
p_4_or_3_multiple = 3 / 36 + 12 / 36

## 5. Venn Diagrams ##

p_c = 3 / 6
p_d = 3 / 6

p_c_d_addition = p_c + p_d

p_c_d_formula = 4 / 6

print(p_c_d_addition)
print(p_c_d_formula)

## 6. Exceptions to the Addition Rule ##

'''An online betting company offers customers the possibility of betting on a variety of games and events (football, tennis, hockey, horse races, car races, etc.). Based on historical data, the company knows the empirical probabilities of the following events:
- Event F (a new customer's first bet is on football) — the probability is 0.26.
- Event T (a new customer's first bet is on tennis) — the probability is 0.11.
- Event "T and F" (a new customer's first bet is on both football and tennis) — the probability is 0.03.

Find the probability that a new customer's first bet is either on football or tennis. Assign your answer to p_f_or_t. You can't use theoretical probability formula to solve this, so you'll need to make use of the addition rule.'''
p_f_or_t = 0.26 + 0.11 - 0.03

## 7. Mutually Exclusive Events ##

'''Based on historical data, the company knows the empirical probabilities of the following events:
- Event H (a new customer's first bet is on hockey) — the probability is 0.08.
- Event C (a new customer's first bet is on car races) — the probability is 0.11.
- Event "H or C" (a new customer's first bet is either on hockey or car races) — the probability is 0.17.

Find the probability that a new customer's first bet is on both hockey and car races. Assign your answer to p_h_and_c. Check the hint if you get stuck.'''
p_h_and_c = 0.08 + 0.11 - 0.17

## 8. Set Notation ##

'''Consider the following sets:

    M = {100, 22, 1, 2}
    N = {22, car insurance, 2, house insurance}
    O = {HHHH, TTTT, TH}
    P = {Hockey, Cycling, Athletics, Swimming}

Consider the following set operations and their results:'''

#M ∪ P = Ø: If you think the result is correct, assign the boolean True to a variable named operation_1, otherwise assign False.
operation_1 = False

#N ∩ M = {22, 2}: If you think the result is correct, assign the boolean True to a variable named operation_2, otherwise assign False.
operation_2 = True

#O ∪ M = {HHHH, TTTT, 100, 22, 2}: If you think the result is correct, assign the boolean True to a variable named operation_3, otherwise assign False.
operation_3 = False

#P ∩ N = Ø: If you think the result is correct, assign the boolean True to a variable named operation_4, otherwise assign False.
operation_4 = True