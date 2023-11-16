# Guided Project - List and description of all project

## Table of Contents

- [General info](#general-info)
- [Technologies](#technologies)
- [List of projects and their description](#List-of-projects-and-their-description)
  - [Guided Project - Jupyter Notebook](#1.-Guided-Project---Jupyter-Notebook)
  - [Guided Project - Profitable App Profiles for the App Store and Google Play Markets](#2.-Guided-Project---Profitable-App-Profiles-for-the-App-Store-and-Google-Play-Market)
  - [Guided Project - Exploring Hacker News Posts](#3.-Guided-Project---Exploring-Hacker-News-Posts)
  - [Guided Project - Exploring eBay Car Sales Data](#4.-Guided-Project---Exploring-eBay-Car-Sales-Data)
  - [Guided Project - Finding Heavy Traffic Indicators on I-94](#5.-Guided-Project---Finding-Heavy-Traffic-Indicators-on-I-94)
  - [Guided Project - Storytelling Data Visualization on Exchange Rates](#6.-Guided-Project---Storytelling-Data-Visualization-on-Exchange-Rates)
  - [Guided Project - Clean and Analyze Employee Exit Surveys](#7.-Guided-Project---Clean-and-Analyze-Employee-Exit-Surveys)
  - [Guided Project Analyzing NYC High School Data](#8.-Guided-Project-Analyzing-NYC-High-School-Data)
  - [Guided Project - Star Wars Survey](#9.-Guided-Project---Star-Wars-Survey)
  - [Guided Project_ Analyzing Kickstarter Projects-811](#10.-Guided-Project_-Analyzing-Kickstarter-Projects-811)
  - [Guided Project - Customers and Products Analysis Using SQL](#11.-Guided-Project---Customers-and-Products-Analysis-Using-SQL)
  - [Guided Project - SQL Window Functions for Northwind Traders](#12.-Guided-Project---SQL-Window-Functions-for-Northwind-Traders)

### General info

Here I will saved all performed guided project from my learning course.

### Technologies

- Python 3.11
- Jupyter Notebook
- SQL
- Python libraries

### List of projects and their description

#### 1. Guided Project - Jupyter Notebook

In these project I learn how to use Jupyter Notebook and short cuts in it.

#### 2. Guided Project - Profitable App Profiles for the App Store and Google Play Markets

The goal of these project is to find profiles of mobile apps that will be profitable for the App Store and Google Play markets. I will work as data analysts at a company that develops mobile apps for Android and iOS, and my job is to enable the team of developers to make data-driven decisions about the type of apps they develop.

#### 3. Guided Project - Exploring Hacker News Posts

[Hacker News]("https://news.ycombinator.com/") is a website where user-submitted stories (beter know as posts) recives votes and comments. It's popular in technology and startup circle.

For my analzy two type of post are interesting:

- `Ask HN`: questions to the community,
- `Show HN`: announcements and showcasing of products, projects etc.

In our analysis, we will determine:

- Which post(`Ask HN` or `Show HN`) receive more comments on average.
- Whether posts created at a certain time of the day receive more comments on average.

We'll be working with the [`hacker_news.csv`]("https://dq-content.s3.amazonaws.com/356/hacker_news.csv") dataset.

#### 4. Guided Project - Exploring eBay Car Sales Data

Project goals:
- clean the data,
- analyze the included used car listings.

In these project I'll be working with a dataset of used cars from eBay Kleinanzeigen, a classifieds section of the German eBay website.
The original dataset isn't available on Kaggle anymore, but you can find it [here](https://data.world/data-society/used-cars-data). For my project purposed we will be working a sample of 50 000 data points from full dataset.

#### 5. Guided Project - Finding Heavy Traffic Indicators on I-94

What the project is about:
- I'm going to analyze a dataset about the westbound traffic on the [I-94 Interstate highway](https://en.wikipedia.org/wiki/Interstate_94). The dataset can be download from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume) and was created by John Hogue.

My goal with this project:
-  is to determine indicators of heavy traffic on I-94.

#### 6. Guided Project - Storytelling Data Visualization on Exchange Rates

In these project I will use [the dataset](https://www.kaggle.com/datasets/lsind18/euro-exchange-daily-rates-19992020), created by Daria Chemkaeva, which describe Euro daily exchange rate between 1999 and 2021. The euro (symbolized with €) is the official currency in most of the countries of the European Union.

If the exchange rate of the euro to the US dollar is 1.5, you get 1.5 $ if you pay 1.0 € (one euro has more value than one US dollar at this exchange rate). 

#### 7. Guided Project - Clean and Analyze Employee Exit Surveys

In these project I will b eworking with [exit survrys from employees of the  Department of Education, Training and Employment (DETE)](https://data.gov.au/dataset/ds-qld-fe96ff30-d157-4a81-851d-215f2a0fe26d/details?q=exit%20survey) and the Technical and Further Education (TAFE) institute in Queensland, Australia. Slighty modifications was made in the orginal dataset to make the work on it easier. One of them was changing encoding from `cp1252` to `UTF-8`.

My goal is to find answers for below questions:

- Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?
- Are younger employees resigning due to some kind of dissatisfaction? What about older employees?

#### 8. Guided Project Analyzing NYC High School Data

This analysis aims to explore the relationships between SAT scores and various demographic factors in New York City public schools. As a brief background, the SAT, or Scholastic Aptitude Test, is a standardized test taken by high school seniors in the U.S., and colleges often use it as a criterion for admissions. Higher average SAT scores are typically associated with better-performing schools.

To conduct this study, we will merge and analyze multiple datasets containing student SAT scores and additional demographic information for each public high school in New York. By combining these datasets, we hope to gain valuable insights into the potential factors that may impact the average SAT scores in these schools and gain a comprehensive understanding of the educational landscape in the city.

Below are the links to all the datasets used in this project:

- SAT scores by school - SAT scores for each high school in New York City
- School attendance - Attendance information for each school in New York City
- Class size - Information on class size for each school
- AP test results - Advanced Placement (AP) exam results for each high school (passing an optional AP exam in a particular subject can earn a student college credit in that subject)
- Graduation outcomes - The percentage of students who graduated, and other outcome information
- Demographics - Demographic information for each school
- School survey - Surveys of parents, teachers, and students at each school

All of these datasets are interrelated. We'll need to combine them into a single dataset before we can find correlations.
Background Research

Goals of the project

High school students take the AP exams before applying to college. There are several AP exams, each corresponding to a school subject. High school students who earn high scores may receive college credit.

The objectives of the project include:

- Investigating the potential correlation between AP exam scores and SAT scores among high schools.
- Analyzing the equity aspect of the SAT by examining correlations between demographic factors such as race, gender, safety level, percentage of English learners, class size, and SAT scores.

#### 9. Guided Project - Star Wars Survey

In these project I will use the data colected by the team at [FiveThirtyEight](http://fivethirtyeight.com/) which can be donwload from [their GitHub respository](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey).

My goal is to find answer for the question:
- **Does the rest of America realise that 'The Empire Strikes Back' is by far the best of the bunch? "** 

#### 10. Guided Project_ Analyzing Kickstarter Projects-811

In these project we will help the product team, which conidering lunching a campaign on Kickstarter to test the viability of some offerings, to pull data which help them understand what might influence success. We will answer following question:
- What type of projects are mostly likely to be successful?
- Which project fail?

#### 11. Guided Project - Customers and Products Analysis Using SQL

The Vehicle Distributors, a fictional wholesale distributor of die cast vehicle models, operates globally with customers in over 15 countries. The company has approached us with a dataset analysis task to help them make critical decisions regarding potential future expansion.  The objective of this project is to address their inquiries and provide data-driven answers by examining the available data. The provided dataset, along with its corresponding schema, can be found [here](https://www.mysqltutorial.org/mysql-sample-database.aspx)

#### 12. Guided Project - SQL Window Functions for Northwind Traders

This project focuses on the rich [Northwind database](https://github.com/pthom/northwind_psql/tree/master), which provides a real-world-like platform for exploring and analyzing sales data.

The projects focus on:
- Evaluating employee performance to boost productivity,
- Understanding product sales and category performance to optimize inventory and marketing strategies,
- Analyzing sales growth to identify trends, monitor company progress, and make more accurate forecasts,
- And evaluating customer purchase behavior to target high-value customers with promotional incentives.

Using the PostgreSQL window functions on the Northwind database, I will provide essential insights which contributing significantly to the company's strategic decisions.


```python

```
