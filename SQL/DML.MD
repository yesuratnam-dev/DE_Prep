# 🔷 DML – Data Manipulation Language

DML commands are used to **manipulate data** stored in database tables. These are the SQL commands that deal with **CRUD** operations: Create, Read, Update, and Delete.

---

## ✅ Key DML Commands

| Command    | Description                    |
|------------|--------------------------------|
| `INSERT`   | Adds new records to a table    |
| `UPDATE`   | Modifies existing records      |
| `DELETE`   | Removes records from a table   |

---

## 📘 Syntax & Examples

### 🔹 INSERT
```sql
-- Insert a single row
INSERT INTO Employees (ID, Name, Salary) 
VALUES (1, 'Alice', 60000.00);

-- Insert multiple rows
INSERT INTO Employees (ID, Name, Salary) 
VALUES 
(2, 'Bob', 55000.00),
(3, 'Charlie', 58000.00);
```

### 🔹 UPDATE
```sql
-- Update one row
UPDATE Employees 
SET Salary = 65000.00 
WHERE ID = 1;

-- Update multiple rows
UPDATE Employees 
SET Department = 'Sales' 
WHERE Salary > 60000;
```

### 🔹 DELETE
```sql
-- Delete a single row
DELETE FROM Employees 
WHERE ID = 1;

-- Delete all rows
DELETE FROM Employees;
```

---

## 🚨 When to Use

- `INSERT` when adding new records to a table
- `UPDATE` to modify specific rows based on a condition
- `DELETE` to remove specific records from a table

---

## ⚠️ Things to Watch Out For

- Always use a `WHERE` clause with `UPDATE` and `DELETE` to avoid modifying or deleting **all** rows.
- `DELETE` is logged row-by-row and is slower than `TRUNCATE`.
- `UPDATE` can impact performance if used on large datasets without proper indexes.

---

## 🔄 Bonus: COMBINING with SELECT

You can often preview which rows would be affected:
```sql
SELECT * FROM Employees WHERE Salary > 60000;

-- Before doing:
UPDATE Employees SET Bonus = 1000 WHERE Salary > 60000;
```