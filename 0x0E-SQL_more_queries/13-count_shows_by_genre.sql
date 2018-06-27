-- script to find number of shows
SELECT name AS genre, count(*) AS number_shows FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre_id ORDER BY number_shows DESC;
