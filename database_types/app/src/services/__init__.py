from . import mysql, mongodb, neo4j

mysql_service = mysql.MySQLService()
mongodb_service = mongodb.MongoDBService()
neo4j_service = neo4j.Neo4jService()
