-- shows rows where name exists and is not empty
select score, name
from second_table
where name is not null and name != ''
order by score desc;
