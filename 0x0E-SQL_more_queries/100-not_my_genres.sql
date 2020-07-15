-- list all genres not linked to the show Dexter in hbtn_0d_tvshows
-- results must be sorted in ascending order by the genre name
SELECT name FROM tv_genres WHERE name NOT IN (SELECT name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE title = "Dexter"
GROUP BY name) ORDER BY name;
