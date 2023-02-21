-- You were hired to babysit your cousin
-- and you want to find a few movies that he can watch with you.Find out how many films there are for each rating.
SELECT
    film.rating,
    count(film_id) as film_count
FROM
    film
GROUP by
    film.rating -- Get a list of all the movies that have a rating of G
SELECT
    film.title,
    film.rating
from
    film
WHERE
    film.rating = 'G'
    OR film.rating = 'PG-13';

-- or PG -13.Filter this list further: look for only movies that are under 2 hours long,
-- and whose rental price (rental_rate) is under 3.00.Sort the list alphabetically.Find a customer in the customer table,
-- and change his / her details to your details,
-- using SQL
-- UPDATE
-- .Now find the customer ’ s address,
--     and use
-- UPDATE
--     to change the address to your address (
--         or make one up
--     ).
SELECT
    film.title,
    film.rating
from
    film
WHERE
    film.rating = 'G'
    OR film.rating = 'PG-13'
    and film.length < 120
    and film.rental_rate < 3.00
ORDER BY
    film.title ASC;

SELECT
    *
FROM
    customer
WHERE
    customer.first_name ilike 'jar%';