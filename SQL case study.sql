select * from work
select * from artist
select * from canvas_size
select * from image_link
select * from museum
select * from museum_hours
select * from product_size
select * from subject


Identify the museum which are open on both sunday and monday. 

select * from museum_hours mh1
where day = 'Sunday'
and exists (select 1 from museum_hours mh2
		   where mh2.museum_id = mh1.museum_id
		   and mh2.day = 'Monday')


Which museum is open for the longest during a day.
Display museum name, state and hours open and which day?

select * from museum_hours
select * from museum

SELECT *
FROM (
    SELECT m.name as museum_name, m.state as museum_state, mh.day,
           to_timestamp(open, 'HH:MI AM') as open_time,
           to_timestamp(close, 'HH:MI PM') as close_time,
           to_timestamp(close, 'HH:MI PM') - to_timestamp(open, 'HH:MI AM') as duration,
           RANK() OVER(ORDER BY to_timestamp(close, 'HH:MI PM') - to_timestamp(open, 'HH:MI AM') DESC) as rank
    FROM museum_hours as mh
    JOIN museum m on m.museum_id = mh.museum_id
) as x
WHERE x.rank = 1;


Display the country and the city with the most no. of museums.
Output 2 seperate columns to mention the city and country
If there are multiple value, seperate them with comma.

with cte_country as
		(select country, count(1)
		 , rank() over (order by count(1) desc) as rnk
		from museum
		group by country),
	cte_city as
		(select city, count(1)
		 , rank() over (order by count(1) desc) as rnk
		from museum
		group by city)
select country,city
from cte_country
cross join cte_city
where cte_country.rnk = 1
and cte_city.rnk = 1










