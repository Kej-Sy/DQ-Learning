## 2. Brief Recap ##

'''
Consider rolling a fair six-sided die once and calculate:
- The probability of getting a 2. Assign your answer to p_2.
- The probability of getting an odd number (1, 3, or 5). Assign your answer to p_odd.
- The probability of getting a 2 or a 4, Assign your answer to p_2_or_4.
'''
p_2 = 1/6
p_odd = 3/6
p_2_or_4 = 1/6 + 1/6

## 3. Updating Probabilities ##

'''
A fair six-sided die is rolled. All we know is that the number we got is less than 5. Calculate:
- The probability of getting a 3. Assign your answer to p_3.
- The probability of getting a 6. Assign your answer to p_6.
- The probability of getting an odd number. Assign your answer to p_odd.
- The probability of getting an even number. Assign your answer to p_even.
'''
p_3 = 1/4
p_6 = 0/4
p_odd = 2/4
p_even = 2/4

## 4. Conditional Probability ##

'''
A student is randomly selected from a class. All we know is that he was born during winter. Assume the winter months are December, January, and February and ignore the fact that these three months have different number of days. Find:
- The probability that he was born in December. Assign your answer to p_december.
- The probability that he was born during summer. Assign your answer to p_summer.
- The probability that he was born in a month which ends in letter "r" — "September", for instance, ends in "r", while "April" doesn't. Assign your answer to p_ends_r.
'''
p_december = 1/3
p_summer = 0/3
p_ends_r = 1/3

## 5. Conditional Probability Formula ##

'''
Two fair six-sided dice are simultaneously rolled, and the two numbers they show are added together.
Find P(A|B), where A is the event where the sum is an even number, and B is the event that the sum is less than eight.
1. Find card(B). Assign your answer to card_b.
    - Note that you'll have to treat identical sums differently if they         come from different die numbers. On the diagram above, we see that          we have three sums of 4, but they all come from different die              outcomes: (3, 1), (2,2), and (1, 3), where the first number                describes the outcome of the first die throw, and the second number        the outcome of the second die throw.
2. Find card(A ∩ B). Assign your answer to card_a_and_b.
3. Calculate P(A|B). Assign your answer to p_a_given_b.
'''
card_b = 21
card_a_and_b = 9
p_a_given_b = 9/21

## 6. Example Walkthough ##

'''
- 23 people are infected with HIV.
- 30 people are not infected with HIV (HIVC means not infected with HIV — recall from the previous course that the superscript "C" indicates a set complement).
- 45 people tested positive for HIV .
- 8 people tested negative for HIV.
- Out of the 23 infected people, 21 tested positive (correct diagnosis).
- Out of the 30 not-infected people, 24 tested positive (wrong diagnosis).
1. Calculate P(T- | HIVC). Assign your answer to p_negative_given_non_hiv.
2. Print p_negative_given_non_hiv.
3. Interpret the result — does the value of P(T- | HIVC) suggest that the test needs more work? Or does it look like the test is reliable enough to use in hospitals? Write your thoughts using a multi-line string. This part of the exercise is not answer-checked, but we suggest a solution nonetheless.
'''

p_negative_given_non_hiv = 6/30
print(p_negative_given_non_hiv)

'''
The probability of testing negative given that a patient is not
infected with HIV is 20%. This means that for every 10,000 healthy
patients, only about 2000 will get a correct diagnosis, while the
other 8000 will not. It looks like the test is almost completely
inefficient, and it could be dangerous to have it used in hospitals.
'''

## 7. Probability Formula ##

'''
A company offering a browser-based task manager tool intends to do some targeted advertising based on people's browsers. The data they collected about their users is described in the table below:
Find:
-  P(Premium | Chrome) — the probability that a randomly chosen user has a premium subscription, provided their browser is Chrome. Assign your answer to p_premium_given_chrome.
- P(Basic | Safari) — the probability that a randomly chosen user has a basic subscription, provided their browser is Safari. Assign your answer to p_basic_given_safari.
- P(Free | Firefox)} — the probability that a randomly chosen user has a free subscription, provided their browser is Firefox. Assign your answer to p_free_given_firefox.
- Between a Chrome user and a Safari user, who is more likely to have a premium subscription? If you think a Chrome user is the answer, then assign the string 'Chrome' to a variable named more_likely_premium, otherwise assign 'Safari'. To solve this exercise, you'll also need to calculate P(Premium | Safari).
'''
p_premium_given_chrome = 158/2762
p_basic_given_safari = 274/1288
p_free_given_firefox = 2103/2285
p_premium_given_safari = 120/1288
more_likely_premium = 'Safari'