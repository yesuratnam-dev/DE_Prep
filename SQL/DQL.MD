# 🔷 DQL – Data Query Language

DQL commands are used to **retrieve** or **query** data from a database. The main command in this category is `SELECT`, which allows you to fetch data from one or more tables.

---

## ✅ Key DQL Commands

| Command         | Description                                   |
|------------------|-----------------------------------------------|
| `SELECT`         | Retrieves data from database                 |
| `WHERE`          | Filters rows based on a condition            |
| `GROUP BY`       | Groups rows that have the same values        |
| `HAVING`         | Filters groups based on a condition          |
| `ORDER BY`       | Sorts the result set                         |
| `LIMIT`          | Restricts the number of rows returned        |
| `JOIN`           | Combines rows from multiple tables           |
| `WITH` (CTE)     | Creates a temporary result set               |
| `PARTITION BY`   | Divides result sets for window functions      |
| Aggregate Functions | Performs calculations on data (e.g., `SUM`, `AVG`) |
| Window Functions | Performs calculations across a result set    |

---

## 📘 Syntax & Examples

### 🔹 SELECT
```sql
-- Retrieve all rows and columns from the Employees table
SELECT * FROM Employees;

-- Retrieve specific columns
SELECT Name, Salary FROM Employees;

-- Filter data with WHERE clause
SELECT * FROM Employees WHERE Salary > 60000;

-- Retrieve distinct values
SELECT DISTINCT Department FROM Employees;

-- Sort data using ORDER BY
SELECT * FROM Employees ORDER BY Salary DESC;

-- Limit results (useful for pagination)
SELECT * FROM Employees LIMIT 5;
```

---

### 🔹 JOINs
#### Inner Join
```sql
-- Retrieve employees and their department names
SELECT e.Name, d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

#### Left Join
```sql
-- Retrieve all employees, including those without a department
SELECT e.Name, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

#### Right Join
```sql
-- Retrieve all departments, including those without employees
SELECT e.Name, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

#### Full Outer Join
```sql
-- Retrieve all employees and departments, including unmatched rows
SELECT e.Name, d.DepartmentName
FROM Employees e
FULL OUTER JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

#### Self Join
```sql
-- Retrieve employees who report to a manager
SELECT e1.Name AS Employee, e2.Name AS Manager
FROM Employees e1
INNER JOIN Employees e2 ON e1.ManagerID = e2.EmployeeID;
```

---

### 🔹 Aggregate Functions
```sql
-- Calculate the total salary
SELECT SUM(Salary) AS TotalSalary FROM Employees;

-- Calculate the average salary by department
SELECT DepartmentID, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentID;

-- Count the number of employees
SELECT COUNT(*) AS EmployeeCount FROM Employees;

-- Find the minimum and maximum salary
SELECT MIN(Salary) AS MinSalary, MAX(Salary) AS MaxSalary FROM Employees;

-- Count distinct departments
SELECT COUNT(DISTINCT DepartmentID) AS UniqueDepartments FROM Employees;
```

---

### 🔹 Window Functions
```sql
-- Calculate the running total of salaries
SELECT Name, Salary, SUM(Salary) OVER (ORDER BY Salary) AS RunningTotal
FROM Employees;

-- Rank employees by salary
SELECT Name, Salary, RANK() OVER (ORDER BY Salary DESC) AS Rank
FROM Employees;

-- Partition data by department and calculate the average salary
SELECT Name, DepartmentID, Salary,
       AVG(Salary) OVER (PARTITION BY DepartmentID) AS AvgDeptSalary
FROM Employees;
```

---

### 🔹 Common Table Expressions (CTEs)
```sql
-- Define a CTE to calculate average salary
WITH AvgSalaryCTE AS (
    SELECT DepartmentID, AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY DepartmentID
)
-- Use the CTE in a query
SELECT e.Name, e.Salary, a.AvgSalary
FROM Employees e
INNER JOIN AvgSalaryCTE a ON e.DepartmentID = a.DepartmentID;
```

---

### 🔹 ROW_NUMBER and RANK Functions
```sql
-- Assign a unique row number to each employee
SELECT Name, Salary, ROW_NUMBER() OVER (ORDER BY Salary DESC) AS RowNumber
FROM Employees;

-- Rank employees by salary (with ties)
SELECT Name, Salary, RANK() OVER (ORDER BY Salary DESC) AS Rank
FROM Employees;

-- Dense rank (no gaps in ranking)
SELECT Name, Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS DenseRank
FROM Employees;
```

---

### 🔹 Advanced Filtering
#### IN and NOT IN
```sql
-- Retrieve employees in specific departments
SELECT Name
FROM Employees
WHERE DepartmentID IN (1, 2, 3);

-- Exclude employees from specific departments
SELECT Name
FROM Employees
WHERE DepartmentID NOT IN (1, 2, 3);
```

#### BETWEEN
```sql
-- Retrieve employees with salaries between 50,000 and 100,000
SELECT Name, Salary
FROM Employees
WHERE Salary BETWEEN 50000 AND 100000;
```

#### LIKE
```sql
-- Retrieve employees whose names start with 'A'
SELECT Name
FROM Employees
WHERE Name LIKE 'A%';

-- Retrieve employees whose names contain 'John'
SELECT Name
FROM Employees
WHERE Name LIKE '%John%';
```

---

### 🔹 Combining Queries
#### UNION and UNION ALL
```sql
-- Combine results without duplicates
SELECT Name FROM Employees
UNION
SELECT Name FROM Managers;

-- Combine results with duplicates
SELECT Name FROM Employees
UNION ALL
SELECT Name FROM Managers;
```

---

### 🔹 CASE Statements
```sql
-- Categorize employees based on salary
SELECT Name,
       CASE
           WHEN Salary > 80000 THEN 'High'
           WHEN Salary BETWEEN 50000 AND 80000 THEN 'Medium'
           ELSE 'Low'
       END AS SalaryCategory
FROM Employees;
```

---


