-- list shows that do not have the comedy genre
SELECT
    tv_shows.title              -- show title
FROM
    tv_shows                    -- all shows
WHERE
    tv_shows.id NOT IN (        -- remove shows that are comedy
        SELECT
            tv_show_genres.show_id     -- show ids that are comedy
        FROM
            tv_show_genres             -- link table
        INNER JOIN
            tv_genres                  -- genres table
        ON
            tv_genres.id = tv_show_genres.genre_id   -- match genre rows
        WHERE
            tv_genres.name = 'Comedy'                -- only comedy genre
    )
ORDER BY
    tv_shows.title ASC;          -- sort titles a to z
