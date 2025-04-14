# 🔷 DDL – Data Definition Language

DDL commands are used to define or modify the structure of database objects like tables, schemas, indexes, etc.

---

## ✅ Key DDL Commands

| Command     | Description                            |
|-------------|----------------------------------------|
| `CREATE`    | Creates a new table, view, or database |
| `ALTER`     | Modifies existing database objects     |
| `DROP`      | Deletes a table or database            |
| `TRUNCATE`  | Removes all rows from a table quickly  |
| `RENAME`    | Renames a database object              |

---

## 📘 Syntax & Examples

### 🔹 CREATE
```sql
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Salary DECIMAL(10, 2),
    Department VARCHAR(50)
);
```

### 🔹 ALTER
```sql
ALTER TABLE Employees ADD JoinDate DATE;
ALTER TABLE Employees MODIFY Salary DECIMAL(12, 2);
```

### 🔹 DROP
```sql
DROP TABLE Employees;
DROP DATABASE CompanyDB;
```

### 🔹 TRUNCATE
```sql
TRUNCATE TABLE Employees;  -- Fast and irreversible!
```

### 🔹 RENAME
```sql
RENAME TABLE Employees TO Staff;
```

---

## 🚨 When to Use

- Creating a new table or modifying an existing one
- Removing unwanted tables or columns
- Resetting data quickly (use `TRUNCATE`)
- Managing database schema evolution

---

## ⚠️ Things to Watch Out For

- `DROP` and `TRUNCATE` are **irreversible** in most databases
- `ALTER` changes structure – test it before applying in production
- Use DDL commands **carefully** in live databases

---

## 🔍 DROP vs TRUNCATE

| Feature          | `DROP`                            | `TRUNCATE`                                |
|------------------|-----------------------------------|--------------------------------------------|
| 🔄 Purpose       | Deletes the **entire table**      | Deletes **all data** in the table         |
| 📦 Structure     | Removes structure + data          | Keeps structure, removes only data        |
| 🔙 Rollback      | ❌ Cannot be rolled back (DDL)     | ⚠️ Usually cannot be rolled back (DDL)    |
| 🔑 Constraints   | Drops constraints/indexes too     | Preserves structure and indexes           |
| 🚀 Speed         | Slower (removes from dictionary)  | Faster (minimal logging)                  |
| 🪪 Triggers      | Triggers *do not* fire             | Triggers *may/may not* fire               |
| 🔧 Usage         | When table is no longer needed     | When you want to reset table data only    |