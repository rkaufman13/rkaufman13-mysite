---
layout: post
title: "What Is A Snowflake Stage?"
categories: things-i-learned
excerpt_separator: <!--more-->
---

![Some snowflakes photographed under a microscope](/assets/PHOTO-snowflake-noaa-121516-1120x534-landscapehero.jpg)

At work the past week, I've been working with large datasets, trying to figure out the most efficient way to process and transform the data without overloading other teams' servers.

_Disclaimer, I'm not a data scientist and SQL is not my strong suit. Any mistakes in the below are mine :)_

So imagine you have a table like this:

| First  | Last       | Favorite_color | Zip_code |
| ------ | ---------- | -------------- | -------- |
| Angela | Apple      | red            | 90210    |
| Bruce  | Banana     | yellow         | 02134    |
| Claire | Canteloupe | orange         | 20008    |
| ...    | ...        | ...            | ...      |
| Zed    | Zucchini   | ...zcolor      | 12345    |

And let's say that table has eleventy billion rows in it. The actual number is not important, for the purposes of our exercise the fact that it is "huge" is the important part.

Now let's say you want to get everyone's first name whose Zip code matches a list of 10,000 arbitrary zip codes.[\*](#fn-1)

You could do:
`SELECT First FROM my_table WHERE Zip_code in (10001, 10002, 10003 ... 20000)`

but that is very slow! I don't know how long it takes on this hypothetical table but in my real-world scenario, a similar query took 20 seconds for 1000 items in the "in" clause. With the amount of data we need to pull from this table (which is significantly more than 10,000 rows), batching in groups of 1000 would be prohibitively slow.

However, if you had your desired ZIP codes as a separate table, `my_codes`:

| Desired_zip_codes |
| ----------------- |
| 10001             |
| 10002             |
| ...               |
| 20000             |

you could run a much faster query:

`SELECT First from my_table INNER JOIN my_codes ON my_table.zip_code = my_codes.desired_zip_codes`

This is much faster because [sql magic](https://www.mssqltips.com/sqlservertip/6659/sql-exists-vs-in-vs-join-performance-comparison/)?[\*\*](#fn-2)

In my case, I had confirmed that a join would be faster than an in clause. So how do I get my list of codes into a JOIN-able format?

A colleague suggested using a Snowflake Stage, which I had never heard of before. The basic [documentation on stages](https://docs.snowflake.com/en/sql-reference/sql/create-stage) explains how to create them. Essentially it's a loading area for ingesting structured data that is not in your database.

In my case I have a CSV uploaded to S3 with the data I want to join on. So I need to load that into a stage and then I can join against it.

So we create a stage:

`CREATE STAGE my_stage URL='s3://mybucket/mypath'`

There are a million other params you can pass in to tweak the behavior of said stage, see more on that [here](https://docs.snowflake.com/en/sql-reference/sql/create-stage). But that's all it takes to create a very basic stage. Depending on how your database and AWS integrations are set up you probably need to add some [permissions](https://docs.snowflake.com/en/user-guide/data-load-s3-config). This will be different for every setup so I'll spare you the gory details of what I did here (it was mostly Terraform and pinging our data-platform team for help). But assuming you've created the stage and your database role has permissions to read from it, you are now in business!

Say you have a file in your S3 storage: `mybucket/mypath/data.csv`. It's now as simple as:

`SELECT $1, $2 FROM @my_stage/data.csv`

Snowflake doesn't know that the header of your CSV is its column names (if you're not using a headerless CSV, which is a whole other thing) which is why we have to use positional arguments. However, we can fix that by importing the CSV into a temporary (or permanent, depending on our use case) table:

`CREATE TEMP TABLE mytemptable (ZIP number);`

Lets now say our zip code list is a one-column CSV:

```
COPY INTO mytemptable @my_stage/data.csv;

SELECT First FROM mytable JOIN mytemptable ON mytemptable.ZIP = mytable.Zip_code;
```

As before, there are about a thousand different configurable options here. I especially like `MATCH_BY_COLUMN_NAME`, which, when paired with `parse_header=TRUE`, automagically determines the column names in your CSV (with headers) and inserts them into the table, even if the columns in the table are in a different order.

Note: `MATCH_BY_COLUMN_NAME` doesn't get you a free pass to _not_ create the temp table, if you want to select by column name. To dynamically create the temp table without knowing the headers in the CSV, that's a separate post. Or see "Generate column description" in my resources below.

That said, I've now created a script that does everything I want to and selects the data I want from Snowflake, joining on my imported CSV! It's still quite slow, taking a few minutes to run each time, but compared to the previous process, this is a huge improvement!

### Resources:

- [Querying data in staged files](https://docs.snowflake.com/en/user-guide/querying-stage)
- [Generate column description](https://docs.snowflake.com/en/sql-reference/functions/generate_column_description)
- [Create FILE FORMAT](https://docs.snowflake.com/en/sql-reference/sql/create-file-format) (very useful for specifying options on your incoming CSV)

\*<a name="fn-1"></a>I realize this is a contrived example; believe me that my real-world use-case is more relevant.

\*\*<a name="fn-2"></a>I learned in the process of writing this blog post that a JOIN is not _always_ faster than an IN, and 'real' data scientists and database admins have dedicated [many words](https://explainextended.com/2009/06/16/in-vs-join-vs-exists/) to analyzing which query is faster under which circumstances. (Don't forget that with most database languages you can run something like EXPLAIN PLAN before actually running the query to see how long it might take.)
