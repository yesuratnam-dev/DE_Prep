### **String Functions**
String functions are used to manipulate and query string data.

`ASCII: `Returns the ASCII value of the first character in a string.
`CHAR_LENGTH / CHARACTER_LENGTH: `Returns the number of characters in a string.
`CONCAT: `Concatenates two or more strings.
`CONCAT_WS: `Concatenates strings with a specified separator.
`FIELD: `Returns the index of a value in a list of values.
`FIND_IN_SET: `Returns the position of a string in a comma-separated list.
`FORMAT: `Formats a number to a specified decimal format.
`INSERT: `Inserts a substring into a string at a specified position.
`INSTR: `Returns the position of the first occurrence of a substring.
`LCASE / LOWER: `Converts a string to lowercase.
`LEFT: `Returns the leftmost characters of a string.
`LENGTH: `Returns the length of a string in bytes.
`LOCATE / POSITION: `Finds the position of a substring in a string.
`LPAD: `Pads a string on the left with a specified character.
`LTRIM: `Removes leading spaces from a string.
`MID / SUBSTR / SUBSTRING: `Extracts a substring from a string.
`REPEAT: `Repeats a string a specified number of times.
`REPLACE: `Replaces occurrences of a substring with another substring.
`REVERSE: `Reverses a string.
`RIGHT: `Returns the rightmost characters of a string.
`RPAD: `Pads a string on the right with a specified character.
`RTRIM: `Removes trailing spaces from a string.
`SPACE: `Returns a string of spaces of a specified length.
`STRCMP: `Compares two strings.
`SUBSTRING_INDEX: `Returns a substring from a string before a specified delimiter.
`TRIM: `Removes leading and trailing spaces from a string.
`UCASE / UPPER: `Converts a string to uppercase.

----
| Function| Description| Example |
| ------- | ------------ | ------- |
| ASCII| Returns the ASCII value of the first character.|  SELECT ASCII('A'); -- Output: 65 |
| CHAR_LENGTH| Returns the number of characters in a string.|  SELECT CHAR_LENGTH('Hello'); -- Output: 5 |
| CONCAT| Concatenates two or more strings.|  SELECT CONCAT('Hello', ' ', 'World'); -- Output: Hello World |
| CONCAT_WS| Concatenates strings with a separator.|  SELECT CONCAT_WS('-', '2025', '04', '14'); -- Output: 2025-04-14 |
| FIELD| Returns the index of a value in a list.|  SELECT FIELD('B', 'A', 'B', 'C'); -- Output: 2 |
| FIND_IN_SET| Finds the position of a string in a list.|  SELECT FIND_IN_SET('B', 'A,B,C'); -- Output: 2 |
| FORMAT| Formats a number with commas and decimals.|  SELECT FORMAT(1234567.89, 2); -- Output: 1,234,567.89 |
| INSERT| Inserts a substring into a string.|  SELECT INSERT('Hello World', 7, 5, 'SQL'); -- Output: Hello SQL |
| LCASE / LOWER| Converts a string to lowercase.|  SELECT LOWER('HELLO'); -- Output: hello |
| REPLACE| Replaces occurrences of a substring.|  SELECT REPLACE('Hello World', 'World', 'SQL'); -- Output: Hello SQL |
| TRIM| Removes leading and trailing spaces.|  SELECT TRIM('   Hello   '); -- Output: Hello |
| UCASE / UPPER| Converts a string to uppercase.|  SELECT UPPER('hello'); -- Output: HELLO |

---

---
### **Numeric Functions**
Numeric functions are used to perform mathematical operations.

`ABS: `Returns the absolute value of a number.
`ACOS: `Returns the arccosine of a number.
`ASIN: `Returns the arcsine of a number.
`ATAN / ATAN2: `Returns the arctangent of a number or the arctangent of two numbers.
`AVG: `Returns the average of a set of values.
`CEIL / CEILING: `Rounds a number up to the nearest integer.
`COS: `Returns the cosine of a number.
`COT: `Returns the cotangent of a number.
`COUNT: `Returns the number of rows in a result set.
`DEGREES: `Converts radians to degrees.
`DIV: `Performs integer division.
`EXP: `Returns the exponential value of a number.
`FLOOR: `Rounds a number down to the nearest integer.
`GREATEST: `Returns the largest value in a list.
`LEAST: `Returns the smallest value in a list.
`LN / LOG / LOG10 / LOG2: `Returns the natural logarithm or logarithm to a specified base.
`MAX: `Returns the maximum value in a set.
`MIN: `Returns the minimum value in a set.
`MOD: `Returns the remainder of a division.
`PI: `Returns the value of π.
`POW / POWER: `Returns a number raised to the power of another number.
`RADIANS: `Converts degrees to radians.
`RAND: `Returns a random number.
`ROUND: `Rounds a number to a specified number of decimal places.
`SIGN: `Returns the sign of a number (-1, 0, or 1).
`SIN: `Returns the sine of a number.
`SQRT: `Returns the square root of a number.
`SUM: `Returns the sum of a set of values.
`TAN: `Returns the tangent of a number.
`TRUNCATE: `Truncates a number to a specified number of decimal places.


---
| Function| Description| Example |
| ----- | ----- | -----|
| ABS| Returns the absolute value of a number.| SELECT ABS(-10); -- Output: 10 |
| AVG| Returns the average of a set of values.| SELECT AVG(Salary) FROM Employees; |
| CEIL / CEILING| Rounds a number up to the nearest integer.| SELECT CEIL(10.2); -- Output: 11 |
| FLOOR| Rounds a number down to the nearest integer.| SELECT FLOOR(10.8); -- Output: 10 |
| MAX| Returns the maximum value in a set.| SELECT MAX(Salary) FROM Employees; |
| MIN| Returns the minimum value in a set.| SELECT MIN(Salary) FROM Employees; |
| ROUND| Rounds a number to a specified number of decimals.| SELECT ROUND(10.567, 2); -- Output: 10.57 |
| SUM| Returns the sum of a set of values.| SELECT SUM(Salary) FROM Employees; |

---

---

### **Date Functions**
Date functions are used to manipulate and query date and time values.

`ADDDATE / DATE_ADD: `Adds a specified interval to a date.
`ADDTIME: `Adds a specified time interval to a time.
`CURDATE / CURRENT_DATE: `Returns the current date.
`CURRENT_TIME: `Returns the current time.
`CURRENT_TIMESTAMP / NOW: `Returns the current date and time.
`CURTIME: `Returns the current time.
`DATEDIFF: `Returns the difference between two dates.
`DATE_FORMAT: `Formats a date according to a specified format.
`DATE_SUB: `Subtracts a specified interval from a date.
`DAY / DAYOFMONTH: `Returns the day of the month for a date.
`DAYNAME: `Returns the name of the day for a date.
`DAYOFWEEK: `Returns the weekday index for a date.
`DAYOFYEAR: `Returns the day of the year for a date.
`EXTRACT: `Extracts a part of a date (e.g., year, month).
`FROM_DAYS: `Converts a number of days to a date.
`HOUR: `Returns the hour from a time.
`LAST_DAY: `Returns the last day of the month for a date.
`LOCALTIME / LOCALTIMESTAMP: `Returns the current date and time.
`MAKEDATE: `Creates a date from a year and day of the year.
`MAKETIME: `Creates a time from hour, minute, and second values.
`MICROSECOND: `Returns the microseconds from a time.
`MINUTE: `Returns the minute from a time.
`MONTH: `Returns the month from a date.
`MONTHNAME: `Returns the name of the month for a date.
`PERIOD_ADD: `Adds a period to a year-month value.
`PERIOD_DIFF: `Returns the difference between two year-month values.
`QUARTER: `Returns the quarter of the year for a date.
`SECOND: `Returns the second from a time.
`SEC_TO_TIME: `Converts seconds to a time value.
`STR_TO_DATE: `Converts a string to a date.
`SUBDATE: `Subtracts a date interval from a date.
`SUBTIME: `Subtracts a time interval from a time.
`SYSDATE: `Returns the current date and time.
`TIME: `Extracts the time part of a date-time value.
`TIME_FORMAT: `Formats a time according to a specified format.
`TIME_TO_SEC: `Converts a time to seconds.
`TIMEDIFF: `Returns the difference between two times.
`TIMESTAMP: `Returns a date-time value.
`TO_DAYS: `Converts a date to the number of days since year 0.
`WEEK / WEEKOFYEAR: `Returns the week number for a date.
`WEEKDAY: `Returns the weekday index for a date.
`YEAR: `Returns the year from a date.
`YEARWEEK: `Returns the year and week number for a date.

---

| Function| Description| Example |
| ----- | ------ | ------ |
| CURDATE / CURRENT_DATE| Returns the current date.| SELECT CURDATE(); -- Output: 2025-04-14 |
| NOW / CURRENT_TIMESTAMP| Returns the current date and time.| SELECT NOW(); -- Output: 2025-04-14 12:34:56 |
| DATEDIFF| Returns the difference between two dates.| SELECT DATEDIFF('2025-04-14', '2025-04-01'); -- Output: 13 |
| DATE_ADD| Adds an interval to a date.| SELECT DATE_ADD('2025-04-14', INTERVAL 10 DAY); -- Output: 2025-04-24 |
| DATE_FORMAT| Formats a date.| SELECT DATE_FORMAT('2025-04-14', '%W, %M %d, %Y'); -- Output: Monday, April 14, 2025 |
| YEAR| Returns the year from a date.| SELECT YEAR('2025-04-14'); -- Output: 2025 |

---
---
### **Advanced Function**
Advanced functions provide additional capabilities for handling data.

`BIN: `Converts a number to binary.
`BINARY: `Casts a string to binary for case-sensitive comparison.
`CASE: `Implements conditional logic in queries.
`CAST / CONVERT: `Converts a value from one data type to another.
`COALESCE: `Returns the first non-NULL value in a list.
`CONNECTION_ID: `Returns the connection ID for the current session.
`CONV: `Converts a number from one base to another.
`CURRENT_USER: `Returns the current user.
`DATABASE: `Returns the name of the current database.
`IF: `Implements conditional logic.
`IFNULL / ISNULL: `Returns a value if NULL is encountered.
`LAST_INSERT_ID: `Returns the last auto-increment ID generated.
`NULLIF: `Returns NULL if two values are equal.
`SESSION_USER / SYSTEM_USER / USER: `Returns information about the current user.
`VERSION: `Returns the version of the database.


- CASE: Conditional logic
```
SELECT Name,
       CASE
           WHEN Salary > 80000 THEN 'High'
           WHEN Salary BETWEEN 50000 AND 80000 THEN 'Medium'
           ELSE 'Low'
       END AS SalaryCategory
FROM Employees;
```

- COALESCE: Return the first non-NULL value
```
SELECT COALESCE(NULL, 'Default', 'Fallback'); -- Output: Default
```

- IF: Conditional logic
```
SELECT IF(Salary > 50000, 'Above Average', 'Below Average') FROM Employees;
```

- NULLIF: Return NULL if two values are equal
```
SELECT NULLIF(10, 10); -- Output: NULL
```

---
