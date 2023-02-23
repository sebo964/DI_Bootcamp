-- Part I
-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)
-- Insert those customers
-- John, Doe
-- Jerome, Lalu
-- Lea, Rive
-- Insert those customer profiles, use subqueries
-- John is loggedIn
-- Jerome is not logged in
-- Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers
SELECT
    customer.first_name
FROM
    customer
    JOIN customer_profile ON customer.id = customer_profile.id
WHERE
    customer_profile.isloggedin = true;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT
    customer.first_name,
    customer_profile.isLoggedIn
FROM
    customer
    LEFT JOIN customer_profile ON customer.id = customer_profile.customer_id;

-- The number of customers that are not LoggedIn
SELECT
    count(customer.first_name) as LoggedOutss
FROM
    customer FULL
    JOIN customer_profile ON customer.id = customer_profile.customer_id
WHERE
    customer_profile.isLoggedIn <> TRUE
    OR customer_profile.isLoggedIn IS NULL;

-- Part II:
-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee
-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
ALTER TABLE
    public.student
ADD
    CONSTRAINT uniqueness UNIQUE (name);

ALTER TABLE
    student
ADD
    CONSTRAINT max_age CHECK (age <= 15);

-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14
-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table
-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021
-- insert John's record
INSERT INTO
    library (student_fk_id, book_fk_id, borrowed_date)
SELECT
    student_id,
    book_id,
    '2022-02-15'
FROM
    student
    CROSS JOIN book
WHERE
    student.name = 'John'
    AND book.title = 'Alice In Wonderland';

-- insert Bob's records
INSERT INTO
    library (student_fk_id, book_fk_id, borrowed_date)
SELECT
    student_id,
    book_id,
    '2021-03-03'
FROM
    student
    CROSS JOIN book
WHERE
    student.name = 'Bob'
    AND book.title = 'To kill a mockingbird';

INSERT INTO
    library (student_fk_id, book_fk_id, borrowed_date)
SELECT
    student_id,
    book_id,
    '2021-08-12'
FROM
    student
    CROSS JOIN book
WHERE
    student.name = 'Bob'
    AND book.title = 'Harry Potter';

-- insert Lera's record
INSERT INTO
    library (student_fk_id, book_fk_id, borrowed_date)
SELECT
    student_id,
    book_id,
    '2021-05-23'
FROM
    student
    CROSS JOIN book
WHERE
    student.name = 'Lera'
    AND book.title = 'Alice In Wonderland';

-- Display the data
SELECT
    book_fk_id,
    student_fk_id,
    borrowed_date
FROM
    public.library;

-- Select all the columns from the junction table
-- Select the name of the student and the title of the borrowed books
SELECT
    student.name,
    book.title,
    library.borrowed_date
FROM
    library
    INNER JOIN student ON library.student_fk_id = student_id
    INNER JOIN book ON library.book_fk_id = book_id
WHERE
    student.name = 'Bob' -- Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT
    avg(age)
FROM
    student
    INNER JOIN library ON student_id = library.student_fk_id
    INNER JOIN book ON book_id = library.book_fk_id
WHERE
    book.title = 'Alice In Wonderland';

-- Delete a student from the Student table, what happened in the junction table ?
DELETE FROM
    student
WHERE
    student_id = 1;

-- JOhn has disappared from the library as well.