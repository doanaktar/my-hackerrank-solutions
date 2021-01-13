SELECT TOP 1 CITY, len(city) 
    FROM STATION
    ORDER BY len(CITY), CITY;
SELECT TOP 1 CITY, len(city) 
    FROM STATION
    ORDER BY len(city) desc, city;