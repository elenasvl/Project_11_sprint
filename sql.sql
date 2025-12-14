SELECT c.login, COUNT(o.id)
FROM Couriers AS c
INNER JOIN Orders AS o ON o.courierId = c.id
WHERE o.idDelivery = true;


SELECT
    track,
    CASE
        WHEN finished = 'true' THEN 2
        WHEN cancelled = 'true' THEN -1
        WHEN inDelivery = 'true' THEN 1
        ELSE 0
    END AS status
FROM Orders;