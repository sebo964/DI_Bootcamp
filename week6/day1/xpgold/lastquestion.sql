SELECT first_name, last_name, birth_date
	FROM public.students OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;