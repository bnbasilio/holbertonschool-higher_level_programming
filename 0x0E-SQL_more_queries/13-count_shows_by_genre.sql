-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- results must be sorted in descending order by the number of shows linked
SELECT name AS genre, COUNT(show_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON genre_id = tv_genres.id GROUP BY genre ORDER BY number_of_shows DESC;
