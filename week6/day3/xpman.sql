-- 🌟 Exercise 1: DVD Rental Instructions 
-- Get a list of all film languages.
select
    distinct language.name
from
    language;

-- Get a list of all films joined with their languages –
-- select
--     the following details: film title,
--     description,
--     and language name.Try your query with different joins: Get all films,
--     even if they don ’ t have languages.Get all languages,
--     even if there are no films in those languages.
SELECT
    film.title,
    film.description,
    language.name
FROM
    film full
    JOIN language ON film.language_id = language.language_id;

--Create a new table called new_film with the following columns : id, name. Add some new films to the table.