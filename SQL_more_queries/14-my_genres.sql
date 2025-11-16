-- list all genres of the show dexter
SELECT
    tv_genres.name          -- genre name
FROM
    tv_shows                -- table with all shows
INNER JOIN
    tv_show_genres          -- link between shows and genres
ON
    tv_shows.id = tv_show_genres.show_id      -- match show to link rows
INNER JOIN
    tv_genres               -- table with all genres
ON
    tv_genres.id = tv_show_genres.genre_id    -- match link rows to genre rows
WHERE
    tv_shows.title = 'Dexter'                 -- keep only rows for show Dexter
ORDER BY
    tv_genres.name ASC;                       -- sort genre names a to z
