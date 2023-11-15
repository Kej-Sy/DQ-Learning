## 1. Retrieving Column Data Types ##

/* In these project we will help the product team, which conidering lunching a campaign on Kickstarter to test the viability of some offerings, to pull data which help them understand what might influence success. We will answer following question:
- What type of projects are mostly likely to be successful?
- Which project fail?*/

--Get the name and data type from every field in the "ksprojects" table
PRAGMA table_info(ksprojects);

## 2. Initial Selection of Rows and Columns ##

SELECT main_category, goal, pledged, backers
  FROM ksprojects
 LIMIT 10;

## 3. Filtering by Category ##

SELECT main_category, goal, backers, pledged
  FROM ksprojects
 WHERE state IN ('failed', 'canceled', 'suspended')
 LIMIT 10;

## 4. Filtering by Quantity ##

SELECT main_category, goal, backers, pledged
 FROM ksprojects
WHERE (state IN ('failed', 'canceled', 'suspended')) AND
      (backers >= 100 AND pledged >= 20000)
LIMIT 10;

## 5. Ordering Results ##

SELECT main_category, goal, backers, pledged,
       ROUND(pledged/goal, 2) AS pct_pledged
  FROM ksprojects
 WHERE state = 'failed'
   AND (backers >= 100 AND pledged >= 20000)
 ORDER BY main_category, pct_pledged DESC
 LIMIT 10;

## 6. Applying Conditional Logic ##

  SELECT main_category, backers, pledged, goal,
         ROUND(pledged / goal, 2) AS pct_pledged,
         CASE
         WHEN pledged/goal >= 1 THEN 'Fully funded'
         WHEN pledged/goal BETWEEN 0.75 AND 1 THEN 'Nearly funded'
         ELSE 'Not nearly funded'
         END AS funding_status
    FROM ksprojects
   WHERE state IN ('failed')
     AND (backers >= 100 AND pledged >= 20000)
ORDER BY main_category, pct_pledged DESC
   LIMIT 10;
   
-- It looks like all project which failed had backers but didn't reach the amount of money set as a goal