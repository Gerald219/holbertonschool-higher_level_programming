-- list all genres and the sum of ratings for their shows
SELECT
    tv_genres.name AS name,                    -- genre name
    SUM(tv_show_ratings.rate) AS rating        -- total rating for this genre
FROM
    tv_genres                                  -- all genres
INNER JOIN
    tv_show_genres                             -- link table between shows and genres
ON
    tv_genres.id = tv_show_genres.genre_id     -- match genre rows to link rows
INNER JOIN
    tv_show_ratings                            -- ratings table
ON
    tv_show_ratings.show_id = tv_show_genres.show_id   -- match link rows to ratings
GROUP BY
    tv_genres.id, tv_genres.name               -- group rows by genre
ORDER BY
    rating DESC;                               -- highest total rating first
