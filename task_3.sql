SELECT `name`, sum(sales.sale) AS sale_count, (SELECT sum(sales.sale * sales.price)) AS sale_rank FROM people
LEFT JOIN sales on people.id = sales.people_id
GROUP BY name;