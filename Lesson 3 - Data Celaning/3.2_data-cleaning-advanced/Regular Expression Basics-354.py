## 1. Introduction ##

import pandas as pd
hn = pd.read_csv("hacker_news.csv")

## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()

python_mentions = 0
pattern = "[Pp]ython"

for title in titles:
    if re.search(pattern, title):
        python_mentions += 1
        
        

## 3. Counting Matches with pandas Methods ##

pattern = '[Pp]ython'

titles = hn["title"]

python_mentions = titles.str.contains(pattern).sum()

## 4. Using Regular Expressions to Select Data ##

titles = hn['title']
pattern = "[Rr]uby"

ruby_titles = titles[titles.str.contains(pattern)]

## 5. Quantifiers ##

# The `titles` variable is available from
# the previous screens

email_bool = titles.str.contains("e-?mail")
email_count = email_bool.sum()
email_titles = titles[email_bool]

## 6. Character Classes ##

pattern = "\[\w+\]"

tag_titles = titles.str.contains(pattern)
tag_count = tag_titles.sum()

## 7. Accessing the Matching Text with Capture Groups ##

pattern = r"\[(\w+)\]"

tag_freq = titles.str.extract(pattern, expand=False).value_counts()

## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10

pattern = "[Jj]ava[^[Ss]"
java_titles = titles[titles.str.contains(pattern)]

## 9. Word Boundaries ##

pattern = r"\b[Jj]ava\b"

java_titles = titles[titles.str.contains(pattern)]

## 10. Matching at the Start and End of Strings ##

beginning_count = titles.str.contains(r"^\[\w+\]").sum()
ending_count = titles.str.contains(r"\[\w+\]$").sum()

## 11. Challenge: Using Flags to Modify Regex Patterns ##

import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])

pattern = r"\be[\-\s]?mails?\b"

test = email_tests.str.contains(pattern, flags=re.I)

email_mentions = titles.str.contains(pattern, flags=re.I).sum()