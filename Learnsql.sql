MAX
MAX finds the max value in a column.
MAX(column_name)

Cast
Cast functions converts a data type to another
Cast(column_name as data_type)

bigint
bigint is a data type that can store large integer values.
Cast(column_name as bigint)

`OVER` is the clause that makes a function a window function. 
It tells SQL to calculate a value across a set of related rows while still keeping every row in the result, 
instead of collapsing them into one like `GROUP BY` does.

`PARTITION BY` goes inside `OVER` and splits the rows into groups that share the same value, s
uch as the same department. The window function then runs separately on each group, 
and without it the function treats the whole result set as one group.

`RANK()` is a window function that gives each row a position number within its partition, 
based on the `ORDER BY` inside `OVER`. Rows with the same value get the same rank, 
and the next rank is skipped, so two people tied at 1 are followed by 3.

CONVERT
CONVERT is a function that converts a value from one data type to another.
Convert(value, data_type)

With
WITH is the SQL keyword that starts a common table expression (CTE).

Create Table
CREATE TABLE is the statement that defines a new table in a relational database.

CREATE VIEW is the statement that saves a query under a name so you can use it like a table.

In SQL, a SET clause assigns new values to columns, most often inside an UPDATE statement to change existing rows.

```sql
UPDATE employees
SET salary = 75000, title = 'Senior Analyst'
WHERE employee_id = 101;
```

This changes the salary and title for employee 101 only. Without the WHERE clause, every row would be updated.

INNER JOIN is a type of join that returns rows when there is a match in both tables being joined.
So Inner join returns only the rows that have matching values in both tables. 
SELECT e.name AS employee,
       m.name AS manager
FROM employees e
INNER JOIN employees m
    ON e.manager_id = m.employee_id;

table e (column manager_id)  will search table m (column employee_id) for a match. If there is a match, the row is returned in the result set.
if no match is found, the row is not returned.