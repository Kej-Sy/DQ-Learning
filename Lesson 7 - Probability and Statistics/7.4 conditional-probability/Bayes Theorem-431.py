## 1. Independence vs. Exclusivity ##

'''
For the exercises below, consider the following probabilities:
- The probability of being infected with HIV is 0.00014. That is P(HIV)=0.00014
- The probability of being infected with HIV given a positive result from an HIV test is 0.03. That is P(HIV|T+)=0.03

Assess with True or False the following statements:
- Events HIV and T+ are independent. If you think this statement is true, then assign the boolean True to statement_1, otherwise assign False.
- Events HIV and HIVC are mutually exclusive. If you think this statement is true, then assign the boolean True to statement_2, otherwise assign False.
- Events HIVC and T+ are dependent. If you think this statement is true, then assign the boolean True to statement_3, otherwise assign False.
'''
statement_1 = False
statement_2 = True
statement_3 = True

## 2. Example Walk-through ##

p_spam = 0.2388
p_secret_given_spam = 0.4802
p_secret_given_non_spam = 0.1284
'''
We can find the word "secret" in many spam emails. However, some emails are not spam even though they contain the word "secret." Let's say we know the following probabilities:
- The probability of getting a spam email is 23.88%. That is P(Spam)=0.2388.
- The probability of an email containing the word "secret" given that the email is spam is 48.02%. That is P("secret"|Spam)=0.4802.
- The probability of an email containing the word "secret" given that the email is not spam is 12.84%. That is P("secret"|SpamC)=0.1284.

Calculate:
- P(SpamC). Assign the result to p_non_spam.
- P(Spam ∩ "secret"). Assign the result to p_spam_and_secret.
- P(SpamC ∩ "secret"). Assign the result to p_non_spam_and_secret.
- P("secret"). Assign the result to p_secret.
'''
p_non_spam = 1 - p_spam
p_spam_and_secret = p_spam * p_secret_given_spam
p_non_spam_and_secret = p_non_spam * p_secret_given_non_spam
p_secret = p_spam_and_secret + p_non_spam_and_secret

## 3. A General Formula ##

'''
An airline transports passengers using two types of planes: a Boeing 737 and an Airbus A320.
- The Boeing operates 73% of the flights. Out of these flights, 3% arrive at the destination with a delay.
- The Airbus operates the remaining 27% of the flights. Out of these flights, 8% arrive with a delay.

Convert the percentages above to probabilities:
- Assign the probability of flying with a Boeing to p_boeing (to better understand what this probability means, imagine a passenger having bought a ticket with this airline — what's the probability that this passenger will be assigned to fly to her destination with a Boeing?).
- Assign the probability of flying with an Airbus to p_airbus.
- Assign the probability of arriving at the destination with a delay given that the passenger flies with a Boeing to p_delay_given_boeing.
- Assign the probability of arriving at the destination with a delay given that the passenger flies with an Airbus to p_delay_given_airbus.

Calculate:

The probability that a passenger will arrive at her destination with a delay. Assign your answer to p_delay. Check the hint if you get stuck.
'''
p_boeing = 0.73
p_airbus = 0.27
p_delay_given_boeing = 0.03
p_delay_given_airbus = 0.08

p_delay = p_boeing * p_delay_given_boeing + p_airbus * p_delay_given_airbus

## 4. Formula for Three Events ##

p_boeing = 0.62
p_airbus = 0.35
p_erj = 0.03
p_delay_boeing = 0.06 
p_delay_airbus = 0.09
p_delay_erj = 0.01
'''
An airline transports passengers using three types of planes: a Boeing 737, - The Boeing operates 62% of the flights. Out of these flights, 6% arrive at the destination with a delay.
- The Airbus operates 35% of the flights. Out of these flights, 9% arrive with a delay.
- The ERJ operates the remaining 3% of the flights. Out of these flights, 1% arrive with a delay.

Calculate the probability of delay and assign your result to p_delay. 
'''
p_delay = p_boeing * p_delay_boeing + p_airbus * p_delay_airbus + p_erj * p_delay_erj

## 6. Bayes' Theorem ##

p_boeing = 0.73
p_airbus = 0.27
p_delay_given_boeing = 0.03
p_delay_given_airbus = 0.08
'''
An airline transports passengers using two types of planes: a Boeing 737 and an Airbus A320.
- The Boeing operates 73% of the flights. Out of these flights, 3% arrive at the destination with a delay.
- The Airbus operates the remaining 27% of the flights. Out of these flights, 8% arrive with a delay.

Use Bayes' theorem to find P(Airbus|Delay). Assign your answer to p_airbus_delay. 
'''
p_airbus_delay = (p_airbus * p_delay_given_airbus) / (p_boeing * p_delay_given_boeing + p_delay_given_airbus * p_airbus)

## 7. Prior and Posterior Probability ##

p_spam = 0.2388
p_secret_given_spam = 0.4802
p_secret_given_non_spam = 0.1284
'''
Many spam emails contain the word "secret". However, some emails are not spam even though they contain the word "secret". Let's say we know the following probabilities:
- The probability of getting a spam email is 23.88%. That is P(Spam)=0.2388.
- The probability of an email containing the word "secret" given that the email is spam is 48.02%. That is P("secret"|Spam)=0.4802.
- The probability of an email containing the word "secret" given that the email is not spam is 12.84%. That is P("secret"|SpamC)=0.1284.

Use Bayes' theorem to find P(Spam|"secret"). Assign your answer to p_spam_given_secret.

Assign the prior probability of getting a spam email to prior.

Assign the posterior probability of getting a spam email (after we see the email contains the word "secret") to posterior.

Calculate the ratio between the posterior and the prior probability — you'll need to divide the posterior probability by the prior probability. Assign your answer to ratio.
'''
p_spam_given_secret = (p_spam * p_secret_given_spam) / ((1 - p_spam) * p_secret_given_non_spam + p_spam * p_secret_given_spam)
prior = p_spam
posterior = p_spam_given_secret
ratio = posterior/prior