--1 задание
SELECT 
    id,
    scores,
    RANK() OVER (ORDER BY scores DESC) AS position
FROM examination;

--2 задание

--минимально 30 (каждая строка второй таблицы совпадает со строкой первой) и максимально 50 (30 + 20) строк

--3 задание
SELECT 
    a.client_id
FROM account a
JOIN transaction t 
    ON a.id = t.account_id
WHERE 
    t.transaction_date >= CURRENT_DATE - INTERVAL '1 month'
    AND t.type = 'buy'
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;