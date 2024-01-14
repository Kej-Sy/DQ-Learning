## 1. An Important Difference ##

'''
Find:
- P(M), the probability that a customer buys a mouse — assign your answer to p_m.
- P(M|L), the probability that a customer buys a mouse given that they bought a laptop — assign your answer to p_m_given_l.
- P(M ∩ L), the probability that a customer buys both a mouse and a laptop — assign your answer to p_m_and_l.
- P(M ∪ L), the probability that a customer buys a mouse or a laptop — assign your answer to p_m_or_l. Check the hint if you don't remember how to calculate this.
'''
p_m = 515/2000
p_m_given_l = 32/90
p_m_and_l = 32/2000
p_m_or_l = 515/2000 + 90/2000 - 32/2000

## 2. Complements ##

p_b_given_m = 0.1486
p_c_given_l = 0.0928
p_non_b_given_c = 0.7622
'''
For our electronics store example, say new data is collected, and we know that:
- P(B|M) = 0.1486, the probability that a customer buys batteries given that they bought a mouse is 0.1486.
- P(C|L) = 0.0928, the probability that a customer buys a cooler given that they bought a laptop is 0.0928.
- P(BC|C) = 0.7622, the probability that a customer doesn't buy batteries given that they bought a cooler is 0.7622.

Using the two rules we learned above, find:
- P(BC|M), and assign your answer to p_non_b_given_m.
- P(CC|L), and assign your answer to p_non_c_given_l.
- P(B|C), and assign your answer to p_b_given_c.
- P(B|MC), and assign your answer to p_b_given_non_m. If you think you can't calculate the probability using any of the two rules above, assign the string 'not possible' to the same variable p_b_given_non_m.
'''
p_non_b_given_m = 1 - p_b_given_m
p_non_c_given_l = 1 - p_c_given_l
p_b_given_c = 1 - p_non_b_given_c
p_b_given_non_m = 'not possible'

## 3. Order of Conditioning ##

'''
Find:
- P(M|LC) — assign your answer to p_m_given_non_l.
- P(LC|M) — assign your answer to p_non_l_given_m.
- P(M ∩ LC) — assign your answer to p_m_and_non_l.
- P(LC ∩ M) — assign your answer to p_non_l_and_m. Check the hint if you're not sure about exercises 3 and 4.
'''
p_m_given_non_l = 483/1910
p_non_l_given_m = 483/515
p_m_and_non_l = 483/2000
p_non_l_and_m = 483/2000

## 4. The Multiplication Rule ##

p_ram = 0.0822
p_gl = 0.0184
p_ram_given_gl = 0.0022
'''
For the exercises below, we know:
- The probability that a customer buys RAM memory from an electronics store is P(RAM) = 0.0822.
- The probability that a customer buys a gaming laptop is P(GL) = 0.0184.
- The probability that a customer buys RAM memory given that they bought a gaming laptop is P(RAM | GL) = 0.0022.

Calculate:
- P(GL ∩ RAM) — assign your answer to p_gl_and_ram.
- P(RAMC | GL) — assign your answer to p_non_ram_given_gl.
- P(GL ∩ RAMC) — assign your answer to p_gl_and_non_ram.
- P(GL ∪ RAM) — assign your answer to p_gl_or_ram.
'''
p_gl_and_ram = p_gl * p_ram_given_gl
p_non_ram_given_gl = 1 - p_ram_given_gl
p_gl_and_non_ram = p_gl * p_non_ram_given_gl
p_gl_or_ram = p_ram + p_gl - p_gl_and_ram

## 5. Statistical Independence ##

'''
A fair six-sided die is rolled twice and the following three events are considered:
- Event K — the die showed a 4 on the second roll
- Event L — the die showed a 2 on the first roll
- Event M — the die showed an even number on the second roll

Find whether the following events are independent or not:
- Events K and L — assign the string 'independent' to a variable named k_and_l if the events are independent, otherwise assign the string 'dependent'.
- Events L and M — assign the string 'independent' to a variable named l_and_m if the events are independent, otherwise assign the string 'dependent'.
- Events K and M — assign the string 'independent' to a variable named k_and_m if the events are independent, otherwise assign the string 'dependent'.
'''
k_and_l = 'independent'
l_and_m = 'independent'
k_and_m = 'dependent'

## 6. Statistical Dependence ##

'''
Find whether the following events are independent or not (check the hint if you don't know how to solve this):
- Events L and M — assign the string 'independent' to a variable named l_and_m if the events are independent, otherwise assign the string 'dependent'.
- Events L and MC — assign the string 'independent' to a variable named l_and_non_m if the events are independent, otherwise assign the string 'dependent'.

Use the formulas we learned to calculate (you could also calculate the probabilities just by looking at the table in this case, but try to use the formulas):

P(L ∩ M) — assign your answer to p_l_and_m.

P(L ∩ MC) — assign your answer to p_l_and_non_m.
'''
p_l = 90/2000
p_l_given_m = 32/515
p_l_given_non_m = 58/1485
check = p_l == p_l_given_m
check1 = p_l == p_l_given_non_m
l_and_m = 'dependent'
l_and_non_m = 'dependent'
p_m = 515/2000
p_non_m = 1485/2000
p_l_and_m = p_m * p_l_given_m
p_l_and_non_m = p_non_m * p_l_given_non_m

## 7. Independence for Three Events ##

p_et = 0.0432
p_ac = 0.0172
p_ps = 0.0236
'''
For our electronics store example, say new data is collected, and we know that:
- The probability that a customer buys an electric toothbrush is P(ET) = 0.0432.
- The probability that a customer buys an air conditioning system is P(AC) = 0.0172
- The probability that a customer buys a PlayStation is P(PS) = 0.0236.

Assuming events ET, AC, and PS are mutually independent, calculate:
- P(ET ∩ PS) — assign your answer to p_et_and_ps.
-P(ET ∩ AC) — assign your answer to p_et_and_ac.
- P(AC ∩ PS) — assign your answer to p_ac_and_ps.
- P(ET ∩ AC ∩ PS) — assign your answer to p_et_and_ac_and_ps.
'''
p_et_and_ps = p_et * p_ps
p_et_and_ac = p_et * p_ac
p_ac_and_ps = p_ac * p_ps
p_et_and_ac_and_ps = p_et * p_ac * p_ps

## 8. Formula for Three Dependent Events ##

p_non_ls = 0.9821
p_cw_given_ls = 0.0079
p_l_given_ls_and_cw = 0.2908
'''
For our electronics store example, say new data is collected. We know that:
- The probability that a customer doesn't buy a set of laptop stickers is P(LSC) = 0.9821.
- The probability that a customer buys screen cleaning wipes given that they bought a set of laptop stickers is P(CW | LS) = 0.0079.
- The probability that a customer buys a laptop given that they bought both a set of laptop stickers and screen cleaning wipes is P(L | LS ∩ CW) = 0.2908.

Assume events LS, CW, and L are dependent and calculate P(LS ∩ CW ∩ L). Assign your answer to p_ls_and_cw_and_l.
'''
p_ls = 1- p_non_ls
p_ls_and_cw_and_l = p_ls * p_cw_given_ls * p_l_given_ls_and_cw