SELECT first_name, last_name, birth_date
	FROM public.students where birth_date = (select max ( birth_date) from public.students)
	
