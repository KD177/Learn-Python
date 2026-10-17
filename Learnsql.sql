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
