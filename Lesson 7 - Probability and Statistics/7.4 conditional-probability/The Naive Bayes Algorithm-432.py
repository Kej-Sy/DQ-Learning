## 3. Using Bayes' Theorem ##

p_spam = 0.5
p_non_spam = 0.5
p_new_message = 0.5417
p_new_message_given_spam = 0.75
p_new_message_given_non_spam = 0.3334
'''
Classify this new message as spam or non-spam:
- Calculate P(Spam|New Message). Assign your answer to p_spam_given_new_message.
- Calculate P(SpamC|New Message). Assign your answer to p_non_spam_given_new_message.
- Classify the message by comparing the probability values. If the message is spam, then assign the string 'spam' to the variable classification. Otherwise, assign the string 'non-spam'.
'''
p_spam_given_new_message = (p_spam * p_new_message_given_spam) / (p_spam * p_new_message_given_spam + p_non_spam * p_new_message_given_non_spam)
p_non_spam_given_new_message = (p_non_spam * p_new_message_given_non_spam) / (p_spam * p_new_message_given_spam + p_non_spam * p_new_message_given_non_spam)

if p_new_message_given_non_spam < p_new_message_given_spam:
    classification = 'spam'
elif p_new_message_given_non_spam > p_new_message_given_spam:
    classification = 'non-spam'

## 4. Ignoring the Division ##

p_spam = 0.5
p_non_spam = 0.5
p_new_message_given_spam = 0.75
p_new_message_given_non_spam = 0.3334
'''
Use the new equations we learned on this screen, and classify the new message as spam or non-spam:
- Calculate P(Spam|New Message). Assign your answer to p_spam_given_new_message.
- Calculate P(SpamC|New Message). Assign your answer to p_non_spam_given_new_message.
- Classify the message by comparing the probability values — if the message is spam, then assign the string 'spam' to the variable classification. Otherwise, assign the string 'non-spam'.
'''
p_spam_given_new_message = p_spam * p_new_message_given_spam
p_non_spam_given_new_message = p_non_spam * p_new_message_given_non_spam

if p_spam_given_new_message < p_non_spam_given_new_message:
    classification = 'non-spam'
elif p_spam_given_new_message > p_non_spam_given_new_message:
    classification = 'spam'

## 5. A One-Word Message ##

p_spam_given_secret = 8/21
'''
Using the table below (there are the same messages as above), classify the message "secret" as spam or non-spam.

0 spam      'secret monry secret secret'
1 spam      'money secret place'
2 non-spam  'you know the secret'
3 ?         'secret'

- Calculate P(SpamC) and assign the answer to p_non_spam.
- Calculate P("secret"|SpamC) and assign the answer to p_secret_given_non_spam.
- Calculate P(SpamC|"secret") and assign the answer to p_non_spam_given_secret.
- Compare P(SpamC|"secret") with P(Spam|"secret") and classify the message "secret" — if the message is spam, then assign the string 'spam' to the variable classification, otherwise assign the string 'non-spam'.
'''
p_non_spam = 1/3
p_secret_given_non_spam = 1/4
p_non_spam_given_secret = p_non_spam * p_secret_given_non_spam

if p_spam_given_secret < p_non_spam_given_secret:
    classification = 'non-spam'
elif p_spam_given_secret > p_non_spam_given_secret:
    classification = 'spam'

## 6. Multiple Words ##

p_spam_given_w1_w2_w3_w4 = 64/4802
'''
Using the table below (the same as above), classify the message "secret place secret secret" as spam or non-spam.

0 non-spam  'secret party at my place'
1 spam      ' secret money secret secret'
2 spam      ' money secret place'
3 non-spam  ' you know the secret'
4 ?         ' secret place secret secret'

- Calculate P(SpamC|w1, w2, w3, w4). Assign the answer to p_non_spam_given_w1_w2_w3_w4. Check the hint if you get stuck.
- Compare P(SpamC|w1, w2, w3, w4) with P(Spam|w1, w2, w3, w4) and classify the message "secret place secret secret" — if the message is spam, then assign the string 'spam' to the variable classification. Otherwise, assign the string 'non-spam'.
'''
p_non_spam = 2/4
p_w1_given_spam = 2/9
p_w2_given_spam = 1/9
p_w3_given_spam = 2/9
p_w4_given_spam = 2/9
p_non_spam_given_w1_w2_w3_w4 = p_non_spam * p_w1_given_spam * p_w2_given_spam * p_w3_given_spam * p_w4_given_spam

if p_spam_given_w1_w2_w3_w4 < p_non_spam_given_w1_w2_w3_w4:
    classification = 'non-spam'
elif p_spam_given_w1_w2_w3_w4 > p_non_spam_given_w1_w2_w3_w4:
    classification = 'spam'

## 9. Edge Cases ##

p_spam = 2/4
p_secret_given_spam = 4/7
p_the_given_spam = 0/7
p_money_given_spam = 2/7
p_spam_given_message = (p_spam * p_secret_given_spam *
                        p_the_given_spam * p_money_given_spam)
'''
P(Spam|"secret code to unlock the money") is already calculated for you. Use the table below (the same as above) to calculate P(SpamC|"secret code to unlock the money").

0 non-spam  'secret party at my place'
1 spam      ' secret money secret secret'
2 spam      ' money secret place'
3 non-spam  ' you know the secret'
4 ?         ' secret code to unlock the money'

- Calculate P(SpamC|"secret code to unlock the money"). Assign your answer to p_non_spam_given_message.
- Print p_spam_given_message and p_non_spam_given_message. Why do you think we got these values? We'll discuss more about this in the next screen.
'''
p_non_spam = 2/4
p_secret_given_non_spam = 2/9
p_the_given_non_spam = 1/9
p_money_given_non_spam = 0/9
p_non_spam_given_message = (p_non_spam * p_secret_given_non_spam *
                        p_the_given_non_spam * p_money_given_non_spam)

print(p_spam_given_message)
print(p_non_spam_given_message)

## 10. Additive Smoothing ##

p_spam = 2/4
p_secret_given_spam = (4 + 1) / (7 + 9)
p_the_given_spam = (0 + 1) / (7 + 9)
p_money_given_spam = (2 + 1) / (7 + 9)
p_spam_given_message = (p_spam * p_secret_given_spam *
                        p_the_given_spam * p_money_given_spam)
'''
P(Spam|"secret code to unlock the money") is already calculated for you. Use the table below (the same as above) to calculate P(SpamC|"secret code to unlock the money").

0 non-spam  'secret party at my place'
1 spam      ' secret money secret secret'
2 spam      ' money secret place'
3 non-spam  ' you know the secret'
4 ?         ' secret code to unlock the money'

- Using the additive smoothing technique, calculate P(SpamC|"secret code to unlock the money"). Assign your answer to p_non_spam_given_message.
- Compare p_spam_given_message and p_non_spam_given_message to classify the message as spam or non-spam. If you think it's spam, then assign the string 'spam' to classification. Otherwise, assign 'non-spam'.
'''
p_non_spam = 2/4
p_secret_given_non_spam = (2 + 1) / (9 + 9)
p_the_given_non_spam = (1 + 1) / (9 + 9)
p_money_given_non_spam = (0 + 1) / (9 + 9)
p_non_spam_given_message = p_non_spam * p_secret_given_non_spam * p_the_given_non_spam * p_money_given_non_spam

if p_spam_given_message < p_non_spam_given_message:
    classification = 'non-spam'
elif p_spam_given_message > p_non_spam_given_message:
    classification = 'spam'