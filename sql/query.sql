SELECT row_to_json(t)
-- SELECT array_to_json(array_agg(row_to_json(t)))
FROM
  (SELECT
    id,
    row_to_json(
      (SELECT d FROM (SELECT number, description) d)
    ) AS data
  FROM
    datas) t
