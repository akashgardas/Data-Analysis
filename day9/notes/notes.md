Data Correlations- Finding Relationships
 
A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set.
 
df.corr()
 
Note: The corr() method ignores "not numeric" columns.
 
                      Duration     Pulse         Maxpulse    Calories
  Duration  1.000000    -0.155408  0.009403      0.922721
  Pulse        -0.155408    1.000000   0.786535      0.025120
  Maxpulse  0.009403    0.786535   1.000000      0.203814
  Calories  0.922721    0.025120   0.203814      1.000000
 
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
 
The number varies from -1 to 1.
 
1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
 
0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
 
-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
 
0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
 
What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.
 
Perfect Correlation:
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.
 
Good Correlation:
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.
 
Bad Correlation:
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.


---
Kaggle Dataset
https://www.kaggle.com/datasets/vijayuv/onlineretail

“E-Commerce Transaction Analytics” (Using Online Retail Dataset)
🎯 Scenario / Story
You are a data analyst at ShopWave, an e-commerce platform in the UK. ShopWave logs every transaction (order) made in their store. Each record has:
Invoice number
Stock code / product ID
Description
Quantity
Invoice date
Unit price
Customer ID
Country

Your manager wants you to clean the data, fix inconsistencies, derive business metrics, and explore relationships. The cleaned data should enable deeper dashboards later.

Tasks & Steps 
Below is a full pipeline of tasks that students should perform. Each task corresponds to one or more of the functions/techniques you already taught.

1. Load & Inspect
Read the CSV (e.g. OnlineRetail.csv)
Display head(), tail(), info(), shape
Check dtypes

2. Missing Data Handling
Use isnull().sum() to find missing values (e.g. some Description or Customer ID missing)
Drop rows that have missing Customer ID (because you can’t tie to a customer)
Fill missing Description or other columns using a placeholder (e.g. "Unknown")

3. Date Parsing / Format Correction
The InvoiceDate column might be string. Convert using pd.to_datetime(..., format='mixed')
Drop records where parsing failed (if any)

4. Detect & Fix Bad or Outlier Data
Some transactions might have negative quantity (returns) — detect those and decide whether to treat as returns or drop
Some unit prices might be zero or negative — fix/clean these (e.g. drop or adjust)

5. Duplicates
Use duplicated() to find duplicated invoice-item entries
Drop duplicates

6. Filtering & Sorting
Filter transactions where Quantity > 1000 (suspicious outliers)
Sort by UnitPrice * Quantity descending (i.e. highest revenue orders)

7. Merge / Enrich Data
Create a small custom DataFrame product_info with columns StockCode, Category, Supplier
Convert its date (if needed) and merge with the main dataset on StockCode (left join)

8. Group & Aggregation
Group by Country and compute total revenue, mean revenue per order, and count of orders
Create a new column Revenue = Quantity * UnitPrice
Use pd.cut() to bucket UnitPrice (e.g. cheap, medium, expensive) and then group by that price range to see how many purchases and average revenue

9. Correlation / Relationships
Use .corr() on numeric columns (Quantity, UnitPrice, Revenue)
Interpret which factors are strongly related (e.g. high quantity often correlates with higher revenue)

10. Rename & String Operations
Rename StockCode to Product_ID, UnitPrice to Price
Use .str methods on Description — e.g., .str.lower(), .str.contains("glass"), etc.
Filter products whose description contains certain keywords

11. Descriptive Statistics
Use .describe() on numeric columns
Use .value_counts() on Country or Category

12. Advanced Filtering / Querying
Use .query() to find orders where Revenue > 1000 and Country == 'Germany'
Use .between() to capture Quantity between 10 and 100

13. Export Cleaned Data
Save the final cleaned & enriched dataset to CSV / Excel