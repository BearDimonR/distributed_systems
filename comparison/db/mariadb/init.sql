/*
*********************************************************************
http://www.mysqltutorial.org
*********************************************************************
Name: MySQL Sample Database classicmodels
Link: http://www.mysqltutorial.org/mysql-sample-database.aspx
Version 3.1
+ changed data type from DOUBLE to DECIMAL for amount columns
Version 3.0
+ changed DATETIME to DATE for some colunmns
Version 2.0
+ changed table type from MyISAM to InnoDB
+ added foreign keys for all tables 
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`shopping` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `shopping`;

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `home_address` varchar(50) NOT NULL,
  `zip_code` varchar(15) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA INFILE '/csv/customers.csv' 
INTO TABLE customers 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `payment` int(11) NOT NULL,
  `order_date` date NOT NULL,
  `delivery_date` date NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA INFILE '/csv/orders.csv' 
INTO TABLE orders 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(order_id,customer_id,payment, @var1, @var2)
SET order_date = STR_TO_DATE(@var1, '%Y-%m-%d'),     
delivery_date = STR_TO_DATE(@var2, '%Y-%m-%d');

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_type` varchar(50) NOT NULL,
  `product_name` varchar(70) NOT NULL,
  `size` varchar(30) NOT NULL,
  `colour` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` smallint(6) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA INFILE '/csv/products.csv' 
INTO TABLE products 
CHARACTER SET 'utf8'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


DROP TABLE IF EXISTS `sales`;

CREATE TABLE `sales` (
  `sales_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `price_per_unit` decimal(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`sales_id`),
  KEY `product_id` (`product_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA INFILE '/csv/sales.csv' 
INTO TABLE sales 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;