--     Write a query to display the names (first_name, last_name) using an alias name “First”, “Last” from the employee table.
SELECT
    first_name as first,
    last_name as last
FROM
    public.employees;

-- Write a query to get unique departments ID from the employee table (ie. without duplicates).
SELECT
    distinct (department_id)
FROM
    public.employees;

-- Write a query to get the details of all employees from the employee table, do so in descending order by first name.
SELECT
    *
FROM
    public.employees
order by
    first_name;

-- Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.
SELECT
    employees.first_name,
    employees.last_name,
    employees.salary,
    0.15 * employees.salary AS pf_salary
FROM
    employees;

-- Write a query to get the employee IDs, names (first_name, last_name) and salary in ascending order according to their salary.
SELECT
    employee_id,
    first_name,
    last_name,
    salary
FROM
    employees
order by
    employees.salary;

-- Write a query to get the total sum of all salaries paid to the employees.
SELECT
    sum(salary) as sumsalary
FROM
    employees;

-- Write a query to get the maximum and minimum salaries paid to the employees.
SELECT
    max(salary) as maxsalary,
    min(salary) as minsalary
FROM
    employees;

-- Write a query to get the average salary paid to the employees.
SELECT
    avg(salary) as avgsalary
FROM
    employees;

-- Write a query to get the number of employees working in the company.
SELECT
    count(*) as numemployees
FROM
    employees;

-- Write a query to get all the first names from the employees table in upper case.
SELECT
    upper(first_name) as upperfirstname
FROM
    employees;

-- Write a query to get the first three characters of each first name of all the employees in the employees table.
SELECT
    substring(first_name, 1, 3) as firstthree
FROM
    employees;

-- Write a query to get the full names of all the employees in the employees table. You have to include the first name and last name.
SELECT
    first_name || ' ' || last_name as fullname
from
    employees;

-- Write a query to get the first name, last name and the length of the full name of all the employees from the employees table.
SELECT
    first_name,
    last_name,
    length(first_name || last_name) as fullnamelength
FROM
    employees;

-- Write a query to check whether the first_name column of the employees table contains any numbers.
SELECT
    first_name ~ '[0-9]' as hasnumbers
FROM
    employees;

-- Write a query to select the first ten records from a table.
SELECT
    *
FROM
    employees
LIMIT
    10;

-- 🌟 Restricting And Sorting
-- Write a query to display the first_name, last_name and salary of all employees whose salary is between $10,000 and $15,000.
SELECT
    first_name,
    last_name,
    salary
FROM
    employees
WHERE
    salary BETWEEN 10000
    AND 15000;

-- Write a query to display the first_name, last_name and hire date of all employees who were hired in 1987.
SELECT
    first_name,
    last_name,
    hire_date
FROM
    employees
WHERE
    hire_date BETWEEN '1987-01-01'
    AND '1987-12-31';

-- Write a query to get the all employees whose first_name has both the letters ‘c’ and ‘e’.
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE '%c%e%';

-- Write a query to display the last_name, job, and salary of all the employees who don’t work as Programmers or Shipping Clerks, and who don’t receive a salary equal to $4,500, $10,000, or $15,000.
SELECT
    last_name,
    salary,
    jobs.job_title
FROM
    employees
    INNER JOIN jobs ON employees.job_id = jobs.job_id
WHERE
    job_title NOT IN ('Programmer', 'Shipping Clerk')
    AND salary NOT IN (4500, 10000, 15000);

-- Write a query to display the last names of all employees whose last name contains exactly six characters.
SELECT
    last_name
FROM
    employees
WHERE
    length(last_name) = 6;

-- Write a query to display the last name of all employees who have the letter ‘e’ as the third character in the name.
SELECT
    last_name
FROM
    employees
WHERE
    last_name LIKE '__e%';

-- Write a query to display the jobs title appearing in the employees table.
SELECT
    employees.job_id,
    jobs.job_title,
    COUNT(*) AS total_employees
FROM
    employees
    INNER JOIN jobs ON employees.job_id = jobs.job_id
GROUP BY
    employees.job_id,
    jobs.job_title;

-- Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.
SELECT
    *
FROM
    employees
WHERE
    last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD');