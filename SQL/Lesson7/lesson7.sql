USE shop;

-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

SELECT
  users.name,
  COUNT(orders.user_id) AS count
FROM users JOIN orders ON users.id = orders.user_id
GROUP BY users.id
ORDER BY count DESC;

-- Выведите список товаров products и разделов catalogs, который соответствует товару.

SELECT prod.name, cat.name product_type FROM products AS prod JOIN catalogs AS cat ON prod.catalog_id = cat.id;

