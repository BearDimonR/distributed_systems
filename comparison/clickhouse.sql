-- Count number of sold item 0.034 sec

SELECT SUM(quantity) 
FROM shopping.sales;

-- Count total price of sold item 0.020 sec

SELECT SUM(total_price) 
FROM shopping.sales;

-- Count price of sold items in the period 0.075 sec

SELECT SUM(total_price) 
FROM shopping.sales
WHERE order_id IN (
    SELECT order_id
    FROM shopping.orders
    WHERE order_date BETWEEN '2021-4-11' AND '2021-12-15'
); 

-- Count number of item A sold in shop B in C period 0.056 sec

SELECT SUM(quantity) 
FROM shopping.sales
WHERE product_id IN (
    SELECT product_id
    FROM shopping.products
    WHERE product_name='Pullover'
)
AND order_id IN (
    SELECT order_id
    FROM shopping.orders
    WHERE order_date BETWEEN '2019-4-11' AND '2021-12-15'
    AND customer_id IN (
        SELECT customer_id
        FROM shopping.customers
        WHERE customer_name='Sonny Tremollet'
    )
); 

-- Count number of item A sold in all shops in C period 0.058 sec

SELECT SUM(quantity) 
FROM shopping.sales
WHERE product_id IN (
    SELECT product_id
    FROM shopping.products
    WHERE product_name='Pullover'
)
AND order_id IN (
    SELECT order_id
    FROM shopping.orders
    WHERE order_date BETWEEN '2021-4-11' AND '2021-12-15'
); 

-- Count price of sold items in all shops in C period 0.049 sec

SELECT SUM(total_price) 
FROM shopping.sales
WHERE order_id IN (
    SELECT order_id
    FROM shopping.orders
    WHERE order_date BETWEEN '2021-4-11' AND '2021-12-15'
);

-- Top 10 sold together by 2 in C period (example, (bread, butter) - 1000 times) 0.059 sec

SELECT a.product_id AS first, b.product_id AS second, COUNT(a.sales_id) AS times
FROM shopping.sales a INNER JOIN shopping.sales b ON a.order_id=b.order_id
WHERE a.product_id != b.product_id
GROUP BY a.product_id, b.product_id
LIMIT 10; 

-- Top 10 sold together by 3 in C period (example, (bread, butter, milk) - 1000 times) 0.200 sec

SELECT a.product_id AS first, b.product_id AS second, c.product_id AS third, COUNT(a.sales_id) AS times
FROM shopping.sales a 
    INNER JOIN shopping.sales b ON a.order_id=b.order_id
    INNER JOIN shopping.sales c ON a.order_id=c.order_id
WHERE a.product_id != b.product_id 
    AND a.product_id != c.product_id
    AND c.product_id != b.product_id
GROUP BY a.product_id, b.product_id, c.product_id
LIMIT 10; 

-- Top 10 sold together by 4 in C period 0.619 sec

SELECT a.product_id AS first, b.product_id AS second, c.product_id AS third, d.product_id AS forth, COUNT(a.sales_id) AS times
FROM shopping.sales a 
    INNER JOIN shopping.sales b ON a.order_id=b.order_id
    INNER JOIN shopping.sales c ON a.order_id=c.order_id
    INNER JOIN shopping.sales d ON a.order_id=d.order_id
WHERE a.product_id != b.product_id 
    AND a.product_id != c.product_id
    AND a.product_id != d.product_id
    AND b.product_id != c.product_id
    AND b.product_id != d.product_id
    AND c.product_id != d.product_id
GROUP BY a.product_id, b.product_id, c.product_id, d.product_id
LIMIT 10;