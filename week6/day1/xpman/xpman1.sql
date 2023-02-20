-- column ID 
-- column id_key = 7
-- counter_keyid = 7 
-- count_id = 1
-- while counter ID < 7
-- select id_key from table id = counter_id
--  counter_id = counter_id + 1
--  count_keyid = count_keyid + 1
Declare counter_id number(2) := 1;

count_keyid number(2) := 1;

Begin while counter_id < 7
select
    id_key
from
    table id = counter_id;

counter_id = counter_id + 1;

count_keyid = count_keyid + 1
end while;

end;