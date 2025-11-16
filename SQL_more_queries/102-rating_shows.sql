-- list all shows and the sum of their ratings
SELECT
    tv_shows.title,                       -- show title
    SUM(tv_show_ratings.rate) AS rating   -- total rating for this show
FROM
    tv_shows                              -- all shows
INNER JOIN
    tv_show_ratings                       -- table with rating rows
ON
    tv_shows.id = tv_show_ratings.show_id -- match each rating to its show
GROUP BY
    tv_shows.id                           -- group all ratings for the same show
ORDER BY
    rating DESC;                          -- highest total rating first
