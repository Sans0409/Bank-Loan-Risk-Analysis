Bank Loan Risk & Approval Analysis

Project Overview
This project demonstrates an end-to-end data analytics pipeline designed to evaluate retail bank credit portfolios, highlight customer risk segmentation and identify loan approval drivers.

The data lifecycle moves through three specific engineering phases:
1.Profiled 2,500 programmatic credit entries and executed automated cleansing via Pandas inside Jupyter Notebook.
2.Ingested raw records into a relational database and developed complex queries leveraging CTEs and window ranking functions to isolate credit segments.
3.Engineered semantic data models utilizing DAX measures to build self-serve interactive KPI dashboards for stakeholder overview.


Advanced SQL Analysis Code Showcase
The following query was developed in PostgreSQL using advanced analytical logic to structure demographic bands and rank applicant positions:

```
WITH TieredMetrics AS (
    SELECT 
        Applicant_ID, Gender, Education, Annual_Income, Credit_Score, Loan_Amount_Requested, Approval_Status,
        AVG(Loan_Amount_Requested) OVER(PARTITION BY Education) AS Avg_Loan_For_Edu_Group,
        DENSE_RANK() OVER(PARTITION BY Education ORDER BY Annual_Income DESC) AS Income_Rank_In_Edu
    FROM bank_loan_data
)
SELECT 
    Applicant_ID, Education, Annual_Income, Loan_Amount_Requested,
    ROUND(Avg_Loan_For_Edu_Group, 2) AS Group_Average_Loan,
    Income_Rank_In_Edu, Approval_Status
FROM TieredMetrics
WHERE Income_Rank_In_Edu <= 10 
ORDER BY Education, Income_Rank_In_Edu;
----
```
