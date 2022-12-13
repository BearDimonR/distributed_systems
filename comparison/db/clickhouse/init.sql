CREATE DATABASE IF NOT EXISTS `shopping`;

USE `shopping`;


DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `customer_id` UInt16 NOT NULL,
  `customer_name` String NOT NULL,
  `gender` String NOT NULL,
  `age` UInt16 NOT NULL,
  `home_address` String NOT NULL,
  `zip_code` String NOT NULL,
  `city` String NOT NULL,
  `state` String NOT NULL,
  `country` String NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE = AggregatingMergeTree();


DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` UInt16 NOT NULL,
  `product_name` String NOT NULL,
  `product_type` String NOT NULL,
  `size` String NOT NULL,
  `colour` String NOT NULL,
  `description` text NOT NULL,
  `quantity` UInt8 NOT NULL,
  `price` Float32 NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE = AggregatingMergeTree();


DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `order_id` UInt16 NOT NULL,
  `order_date` Date NOT NULL,
  `payment` UInt16 NOT NULL,
  `delivery_date` Date NOT NULL,
  `customer_id` UInt16 NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE = AggregatingMergeTree();


DROP TABLE IF EXISTS `sales`;

CREATE TABLE `sales` (
  `sales_id` UInt16 NOT NULL,
  `order_id` UInt16 NOT NULL,
  `product_id` UInt16 NOT NULL,
  `quantity` UInt16 NOT NULL,
  `price_per_unit`Float32 NOT NULL,
  `total_price` Float32 NOT NULL,
  PRIMARY KEY (`sales_id`)
) ENGINE = AggregatingMergeTree();