-- list each genre and how many shows use it
SELECT
    tv_genres.name AS genre,           -- genre name
    COUNT(tv_shows.id) AS number_of_shows  -- how many shows have this genre
FROM
    tv_genres                          -- list of all genres
INNER JOIN
    tv_show_genres                     -- link table between shows and genres
ON
    tv_genres.id = tv_show_genres.genre_id   -- match genre row to link row
INNER JOIN
    tv_shows                           -- list of all shows
ON
    tv_shows.id = tv_show_genres.show_id     -- match show row to link row
GROUP BY
    tv_genres.id                       -- group rows by genre
ORDER BY
    number_of_shows DESC;              -- sort by count from biggest to smallest
