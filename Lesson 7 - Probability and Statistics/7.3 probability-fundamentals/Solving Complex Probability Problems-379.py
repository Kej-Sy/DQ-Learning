## 1. Complex Probability Problems ##

'''An advertisement company runs a quick test and shows two ads on the same web page (ad "A" and ad "B") to 100 users. At the end of the trial, they found:
- 12 users clicked on ad "A"
- 17 users clicked on ad "B"
- 3 users clicked on both ad "A" and ad "B"
Find:'''

#The empirical probability that a user clicks on ad "A." Assign your result to p_a.
p_a = 12 / 100

#The empirical probability that a user clicks on ad "B." Assign your result to p_b.
p_b = 17 /100

#The empirical probability that a user clicks on both ad "A" and ad "B." Assign your result to p_a_and_b.
p_a_and_b = 3 / 100

#The probability that a user clicks on either ad "A" or ad "B." Assign your result to p_a_or_b. For this exercise, keep in mind a user can click on both ads, so the events are not mutually exclusive — use the addition rule.
p_a_or_b = p_a + p_b - p_a_and_b

## 2. Opposite Events ##

#A company that develops a time-tracking tool sells two kinds of subscription: basic and premium. When a new user tries the product, there's a 0.2 probability the user buys the basic subscription and 0.15 he buys premium. Find:

#The probability that a new user doesn't buy a basic subscription (you'll need to use the P(E) = 1 - P(non-E) formula). Assign your result to p_non_basic.
p_non_basic = 1 - 0.2
    
#The probability that a new user doesn't buy a premium subscription. Assign your result to p_non_premium.
p_non_premium = 1 - 0.15

#The probability that a user buys either basic or premium. Assign your result to p_subscription (assume buying basic and buying premium are mutually exclusive).
p_subscription = 0.2 + 0.15

#The probability that a new user doesn't buy a subscription. Assign your result to p_non_subscription.
p_non_subscription = 1 - 0.2 - 0.15

## 3. Example Walk-Through ##

#Find the probability that it takes four flips or more for a coin to land heads up (let's call this event "B").

#Begin with finding the probability of the event non-B, which is equivalent to finding the probability that we'll get at least one heads if we flip a coin three times. Assign your result to p_non_b.
'''Omega: HHH, HHT, HTT, THH, THT, TTH, TTT, HTH'''
p_non_b = 7 / 8

#Now use p_non_b to find the probability of B. Assign your result to p_b.
p_b = 1 - p_non_b

## 4. Set Complements ##

#An advertisement company monitors the activity for a specific ad and shows it repeatedly to the same users (so a single user sees the ad multiple times). Regardless of the number of times the ad is shown to a user, the probability that the user clicks on the ad is 0.5. Find:

#The probability that a user doesn't click on the ad. Assign your answer to p_non_click.
p_non_click = 1 - 0.5

#The probability that it takes two times or less for a user to click on the ad. Assign your answer to p_two_or_less.
''' (C,C), (C,NC,) (NC, C), (NC, NC)'''
p_two_or_less = 3 / 4

#The probability that it takes three times or more for a user to click on the ad. Assign your answer to p_three_or_more.
p_three_or_more = 1 - 3 / 4

## 5. The Multiplication Rule ##

#For rolling a fair six-sided die, find:

#The probability of getting a 6 two times in a row. Assign your result to p_6_6.
p_6_6 = 1/6 * 1/6

#The probability of getting a 3 on the first throw and a 2 on the second throw. Assign your result to p_3_2.
p_3_2 = 1/6 * 1/6

#The probability of getting an even number on both throws. Assign your result to p_even_even.
p_even_even = 3/6 * 3/6

#The probability of getting a 1 on the first throw and an even number on the second throw. Assign your result to p_1_even.
p_1_even = 1/6 * 3/6

## 6. Independent Events ##

#Getting heads up 18 times in a row when flipping a fair coin. Assign your answer to p_18h.
p_18h = 0.5 ** 18

#Getting a six three times in a row when throwing a fair six-sided die. Assign your answer to p_666.
p_666 = (1/6) ** 3

#Not getting any six when throwing a fair six-sided die four times. Assign your answer to p_not_6.
p_not_6 = (1 - 1/6) ** 4 

## 7. Combining Formulas ##

p_one_double_6 = 1 - (35 / 36) ** 24

## 8. Sampling With(out) Replacement ##

#We're sampling without replacement from a standard 52-card deck. Find the probability of:

#Getting two kings in a row. Assign your answer to p_kk.
p_kk = 4/52 * 3/51

#Getting a seven of hearts, followed by a queen of diamonds. Assign your answer to p_7q.
p_7q = 1/52 * 1/51

#Getting a jack, followed by a queen of diamonds, followed by a king, followed by another jack. Assign your answer to p_jqkj. This one is a bit tricky, so pay attention to the details of the question.
p_jqkj = 4/52 * 1/51 * 4/50 * 3/49