/* SELECT
    customer_id,
    COUNT(Visits.visit_id) as count_no_trans
FROM Visits
NATURAL LEFT JOIN Transactions
WHERE Transactions.visit_id IS NULL
GROUP BY customer_id
ORDER BY count_no_trans; */

# my solution is below but I really liked the 
# use of NATURAL LEFT JOIN, so I added it as a note
SELECT
    customer_id,
    COUNT(Visits.visit_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id IS NULL
GROUP BY customer_id
ORDER BY count_no_trans DESC;