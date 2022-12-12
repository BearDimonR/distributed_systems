## Task

#### Configure partitioning

MariaDB has build-in partition support wia plugin. 

All that we need to do, make some partitions in DDL:
```
(init.sql)

CREATE TABLE `country_stats` (
  `country_id` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `population` int(11) DEFAULT NULL,
  `gdp` decimal(15,0) DEFAULT NULL,
  PRIMARY KEY (`country_id`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
PARTITION BY RANGE ( year ) (
    PARTITION p0 VALUES LESS THAN (1950),
    PARTITION p1 VALUES LESS THAN (2000),
    PARTITION p2 VALUES LESS THAN MAXVALUE
);
```

#### Test write to save records into different partitions

  1. Run ```docker-compose up --build```

  2. Follow http://127.0.0.1:8080/docs#/

  3. Use swagger api to create records and test them (available partitions 'p0', 'p1', 'p2')

  4. To run locally ```uvicorn app/main:app --reload```