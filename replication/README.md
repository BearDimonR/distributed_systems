## Task

1. Configure Master-Slave and Master-Master replication

2. Create test app that can use replication (write to one node and read from the second)

3. Describe configuration process, problems and their solutions


### Master-Slave configuration

1. Use `docker-compose up` to run different instances of MariaDB

2. Login to the `master` and `slave` instances

3. On the ```master``` run 
```
mysql -u root -p (password "pass")
create user 'replication_user'@'%' identified by 'pass';
grant replication slave on *.* to 'replication_user'@'%';
exit
``` 

4. Get ```master``` config info
```
mysql -e "show master status \G" -p

Output:
    File: binary-log.000015 (<master binary file>)
    Position: 725 (<master position>)
```

CHANGE MASTER TO
  MASTER_HOST='replication_second_master_1',
  MASTER_USER='replication_user',
  MASTER_PASSWORD='pass',
  MASTER_PORT=3306,
  MASTER_LOG_FILE='mysql-replication.000002',
  MASTER_LOG_POS=697,
  MASTER_CONNECT_RETRY=10;

5. Update slave ```slave```
```
mysql -u root -p

stop slave;
CHANGE MASTER TO
  MASTER_HOST='replication_master_1',
  MASTER_USER='replication_user',
  MASTER_PASSWORD='pass',
  MASTER_PORT=3306,
  MASTER_LOG_FILE='<master binary file>',
  MASTER_LOG_POS=<master position>,
  MASTER_CONNECT_RETRY=10;
start slave;
show slave status;
```

6. On ```master``` remove table lock
```
mysql -u root -p
lock tables;
unlock tables;
```

### Master-Master configuration

1. Do Master-Slave configuration for each of the masters node


### App launch

  1. Run ```docker-compose up --build```

  2. Follow http://127.0.0.1:8080/docs#/

  3. Use swagger api to work with different mariaDB instances

  4. To run locally ```uvicorn app/main:app --reload```



### Problems and their solutions

1. Need to configure each database separately

    Solution: use ```*.cnf``` file to overwrite required configs

2. Database sync

    Solution: use ```init.sql``` dump to make database content equal

3. Master config doesn't show

    Solution: restart mysql instance or use config file on startup