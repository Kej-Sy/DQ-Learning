## 1. The Rule of Product ##

#Consider the composite experiment E1E2, where E1 is rolling a fair six-sided die once, and E2 is rolling the same die again. One of the outcomes of E1E2 could be (1, 6), which means we get a 1 for the first roll and a 6 for the second one.

#Use the rule of product to calculate the total number of outcomes. Assign your answer to n_outcomes.
n_outcomes = 6 * 6

#Use n_outcomes to calculate the probability of getting a (6,6). Assign your answer to p_six_six. Check the hint if you have difficulties calculating this.
p_six_six = 1 / n_outcomes

#Use n_outcomes to calculate the probability of not getting a (5,5) and assign your answer to p_not_five_five.
p_not_five_five = 1 - (1/36)

## 2. Extended Rule of Product ##

#We roll a fair six-sided die three times and then randomly draw a card from a standard 52-card deck. One of the outcomes is (6, 6, 6, ace of diamonds), which means getting three 6's in a row when we roll the die, followed by drawing an ace of diamonds from the deck.

#Use the extended rule of product to calculate the total number of outcomes. Assign your answer to total_outcomes.
total_outcomes = 6 * 6 * 6 * 52

#Use total_outcomes to calculate the probability of getting (6, 6, 6, ace of diamonds) — three sixes in a row followed by an ace of diamonds. Assign your answer to p_666_ace_diamonds.
p_666_ace_diamonds = 1 / total_outcomes

#Use p_666_ace_diamonds to calculate the probability of getting anything but (6, 6, 6, ace of diamonds). Assign your answer to p_no_666_ace_diamonds.
p_no_666_ace_diamonds = 1 - p_666_ace_diamonds

## 3. Example Walkthrough ##

p_crack_4 = 1 / 10 ** 4
p_crack_6 = 1 / 10 ** 6

## 4. Permutations ##

def fractorial(n):
    
    final_product = 1
    
    for i in range(n, 0 ,-1):
        final_product *= i
        
    return final_product

permutations_1 = fractorial(6)
permutations_2 = fractorial(52)

## 5. More About Permutations ##

perm_3_52 = 52 * 51 * 50
perm_4_20 = 20 * 19 * 18 * 17
perm_4_27 = 27 * 26 * 25 * 24

## 6. Permutations Formulas ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def permutation(n,k):
    numerator = factorial(n)
    denominator = factorial(n-k)
    return numerator/denominator

p_crack_pass = 1 / permutation(127, 16)

## 7. Unique Arrangements ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def permutation(n, k):
    numerator = factorial(n)
    denominator = factorial(n-k)
    return numerator/denominator

c = permutation(52, 5) / factorial(5)
p_aces_7 = 1 / c

c_lottery = permutation(49, 6) / factorial(6)
p_big_prize = 1 / c_lottery

print(p_big_prize)

## 8. Combinations ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def combinations(n,k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k)
    
    return numerator/denominator

'''
A small company is interested in running an A/B test and is about to select a group of 18 customers out of a total of 34 customers. Find the number of unique ways in which 18 customers can be selected from a group of 34 and assign your result to c_18.
'''
c_18 = combinations(34, 18)

'''
One of the possible outcomes is group Y, which is a group formed by 18 customers. Assume all the outcomes have equal chances of occurring and calculate the probability of getting a group other than group Y. Assign your answer to p_non_Y.
'''
p_Y = 1 / c_18
p_non_Y = 1 - p_Y