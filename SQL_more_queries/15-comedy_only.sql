-- list all comedy shows by title
SELECT
    tv_shows.title              -- show title
FROM
    tv_shows                    -- table with all shows
INNER JOIN
    tv_show_genres              -- link table between shows and genres
ON
    tv_shows.id = tv_show_genres.show_id      -- match show rows to link rows
INNER JOIN
    tv_genres                   -- table with all genres
ON
    tv_genres.id = tv_show_genres.genre_id    -- match link rows to genre rows
WHERE
    tv_genres.name = 'Comedy'                 -- keep only rows where genre is Comedy
ORDER BY
    tv_shows.title ASC;                       -- sort titles from a to z

