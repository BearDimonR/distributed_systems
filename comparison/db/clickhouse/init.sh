
BASEDIR=$(dirname "$0")

cat $BASEDIR/init.sql | clickhouse-client -mn --password pass

cat /csv/customers.csv | clickhouse-client --password pass --database shopping --query="INSERT INTO customers FORMAT CSVWithNames";
cat /csv/orders.csv | clickhouse-client --password pass --database shopping --query="INSERT INTO orders FORMAT CSVWithNames";
cat /csv/products.csv | clickhouse-client --password pass --database shopping --query="INSERT INTO products FORMAT CSVWithNames";
cat /csv/sales.csv | clickhouse-client --password pass --database shopping --query="INSERT INTO sales FORMAT CSVWithNames";