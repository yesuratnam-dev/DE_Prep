# 🧩 SQL Command Categories

| Category | Full Form                   | Purpose                           |
|----------|-----------------------------|-----------------------------------|
| **DDL**  | Data Definition Language     | Define or modify database structure |
| **DML**  | Data Manipulation Language   | Manage data within tables         |
| **DQL**  | Data Query Language          | Query data                        |
| **DCL**  | Data Control Language        | Control access/permissions        |
| **TCL**  | Transaction Control Language | Manage transactions               |

---

## 🔷 DDL – Data Definition Language

Used to define or modify database structure.

| Command     | Description                             |
|-------------|-----------------------------------------|
| `CREATE`    | Creates a new table or database         |
| `ALTER`     | Modifies existing table structure       |
| `DROP`      | Deletes a table or database             |
| `TRUNCATE`  | Removes all records from a table        |
| `RENAME`    | Renames a table                         |

### ✅ DDL Example
```sql
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Salary DECIMAL(10, 2),
    JoinDate DATE
);

ALTER TABLE Employees ADD Department VARCHAR(50);

DROP TABLE Employees;

TRUNCATE TABLE Employees;
```

---

## 🔷 DML – Data Manipulation Language

Used for inserting, updating, and deleting records.

| Command    | Description                    |
|------------|--------------------------------|
| `INSERT`   | Adds new records to a table    |
| `UPDATE`   | Modifies existing records      |
| `DELETE`   | Removes records from a table   |

### ✅ DML Example
```sql
INSERT INTO Employees (ID, Name, Salary) VALUES (1, 'Alice', 60000.00);

UPDATE Employees SET Salary = 65000.00 WHERE ID = 1;

DELETE FROM Employees WHERE ID = 1;
```

---

## 🔷 DQL – Data Query Language

Used to query and retrieve data from tables.

| Command   | Description                  |
|-----------|------------------------------|
| `SELECT`  | Retrieves data from database |

### ✅ DQL Example
```sql
SELECT * FROM Employees;

SELECT Name, Salary FROM Employees WHERE Salary > 50000;
```

---

## 🔷 DCL – Data Control Language

Used to manage access control and user permissions.

| Command   | Description                         |
|-----------|-------------------------------------|
| `GRANT`   | Gives privileges to users           |
| `REVOKE`  | Takes back privileges from users    |

### ✅ DCL Example
```sql
GRANT SELECT, INSERT ON Employees TO 'username';

REVOKE INSERT ON Employees FROM 'username';
```

---

## 🔷 TCL – Transaction Control Language

Used to manage changes made by DML statements and control transactions.

| Command      | Description                             |
|--------------|-----------------------------------------|
| `COMMIT`     | Saves all changes since the last commit |
| `ROLLBACK`   | Undoes changes since last commit        |
| `SAVEPOINT`  | Sets a point to rollback to             |
| `SET TRANSACTION` | Sets characteristics of a transaction |

### ✅ TCL Example
```sql
BEGIN;

UPDATE Accounts SET Balance = Balance - 1000 WHERE ID = 1;
UPDATE Accounts SET Balance = Balance + 1000 WHERE ID = 2;

COMMIT;

-- or

ROLLBACK;

-- or using SAVEPOINT
SAVEPOINT beforeTransfer;

UPDATE Accounts SET Balance = Balance - 500 WHERE ID = 3;

ROLLBACK TO beforeTransfer;
```


---

| Keyword	             | Description |
| -------- | ----------- |
| ADD	             | Adds a column in an existing table |
| ADD CONSTRAINT	             | Adds a constraint after a table is already created |
| ALL	             | Returns true if all of the subquery values meet the condition |
| ALTER	             | Adds, deletes, or modifies columns in a table, or changes the data type of a column in a table |
| ALTER COLUMN	             | Changes the data type of a column in a table |
| ALTER TABLE	             | Adds, deletes, or modifies columns in a table |
| AND	             | Only includes rows where both conditions is true |
| ANY	             | Returns true if any of the subquery values meet the condition |
| AS	             | Renames a column or table with an alias |
| ASC	             | Sorts the result set in ascending order |
| BACKUP DATABASE	             | Creates a back up of an existing database |
| BETWEEN	             | Selects values within a given range |
| CASE	             | Creates different outputs based on conditions |
| CHECK	             | A constraint that limits the value that can be placed in a column |
| COLUMN	             | Changes the data type of a column or deletes a column in a table |
| CONSTRAINT	             | Adds or deletes a constraint |
| CREATE	             | Creates a database, index, view, table, or procedure |
| CREATE DATABASE	             | Creates a new SQL database |
| CREATE INDEX	             | Creates an index on a table (allows duplicate values) |
| CREATE OR REPLACE VIEW	             | Updates a view |
| CREATE TABLE	             | Creates a new table in the database |
| CREATE PROCEDURE	             | Creates a stored procedure |
| CREATE UNIQUE INDEX	             | Creates a unique index on a table (no duplicate values) |
| CREATE VIEW	             | Creates a view based on the result set of a SELECT statement |
| DATABASE	             | Creates or deletes an SQL database |
| DEFAULT	             | A constraint that provides a default value for a column |
| DELETE	             | Deletes rows from a table |
| DESC	             | Sorts the result set in descending order |
| DISTINCT	             | Selects only distinct (different) values |
| DROP	             | Deletes a column, constraint, database, index, table, or view |
| DROP COLUMN	             | Deletes a column in a table |
| DROP CONSTRAINT	             | Deletes a UNIQUE, PRIMARY KEY, FOREIGN KEY, or CHECK constraint |
| DROP DATABASE	             | Deletes an existing SQL database |
| DROP DEFAULT	             | Deletes a DEFAULT constraint |
| DROP INDEX	             | Deletes an index in a table |
| DROP TABLE	             | Deletes an existing table in the database |
| DROP VIEW	             | Deletes a view |
| EXEC	             | Executes a stored procedure |
| EXISTS	             | Tests for the existence of any record in a subquery |
| FOREIGN KEY	             | A constraint that is a key used to link two tables together |
| FROM	             | Specifies which table to select or delete data from |
| FULL OUTER JOIN	             | Returns all rows when there is a match in either left table or right table |
| GROUP BY	             | Groups the result set (used with aggregate functions: COUNT, MAX, MIN, SUM, AVG) |
| HAVING	             | Used instead of WHERE with aggregate functions |
| IN	             | Allows you to specify multiple values in a WHERE clause |
| INDEX	             | Creates or deletes an index in a table |
| INNER JOIN	             | Returns rows that have matching values in both tables |
| INSERT INTO	             | Inserts new rows in a table |
| INSERT INTO SELECT	             | Copies data from one table into another table |
| IS NULL	             | Tests for empty values |
| IS NOT NULL	             | Tests for non-empty values |
| JOIN	             | Joins tables |
| LEFT JOIN	             | Returns all rows from the left table, and the matching rows from the right table |
| LIKE	             | Searches for a specified pattern in a column |
| LIMIT	             | Specifies the number of records to return in the result set |
| NOT	             | Only includes rows where a condition is not true |
| NOT NULL	             | A constraint that enforces a column to not accept NULL values |
| OR	             | Includes rows where either condition is true |
| ORDER BY	             | Sorts the result set in ascending or descending order |
| OUTER JOIN	             | Returns all rows when there is a match in either left table or right table |
| PRIMARY KEY	             | A constraint that uniquely identifies each record in a database table |
| PROCEDURE	             | A stored procedure |
| RIGHT JOIN	             | Returns all rows from the right table, and the matching rows from the left table |
| ROWNUM	             | Specifies the number of records to return in the result set |
| SELECT	             | Selects data from a database |
| SELECT DISTINCT	             | Selects only distinct (different) values |
| SELECT INTO	             | Copies data from one table into a new table |
| SELECT TOP	             | Specifies the number of records to return in the result set |
| SET	             | Specifies which columns and values that should be updated in a table |
| TABLE	             | Creates a table, or adds, deletes, or modifies columns in a table, or deletes a table or data inside a table |
| TOP	             | Specifies the number of records to return in the result set |
| TRUNCATE TABLE	             | Deletes the data inside a table, but not the table itself |
| UNION	             | Combines the result set of two or more SELECT statements (only distinct values) |
| UNION ALL	             | Combines the result set of two or more SELECT statements (allows duplicate values) |
| UNIQUE	             | A constraint that ensures that all values in a column are unique |
| UPDATE	             | Updates existing rows in a table |
| VALUES	             | Specifies the values of an INSERT INTO statement |
| VIEW	             | Creates, updates, or deletes a view |
| WHERE	             | Filters a result set to include only records that fulfill a specified condition |