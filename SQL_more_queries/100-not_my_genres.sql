-- list genres that are not linked to dexter
SELECT
    tv_genres.name              -- genre name
FROM
    tv_genres                   -- all genres
WHERE
    tv_genres.id NOT IN (       -- remove genres used by dexter
        SELECT
            tv_show_genres.genre_id   -- genre ids for dexter
        FROM
            tv_shows                  -- all shows
        INNER JOIN
            tv_show_genres            -- link table
        ON
            tv_shows.id = tv_show_genres.show_id   -- match show to links
        WHERE
            tv_shows.title = 'Dexter'              -- only the show dexter
    )
ORDER BY
    tv_genres.name ASC;          -- sort names a to z
