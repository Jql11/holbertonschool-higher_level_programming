-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS `avg_temp` FROM temperatures WHERE month = 'July' AND month = 'August' ORDER BY `avg_temp` DESC LIMIT 3;
