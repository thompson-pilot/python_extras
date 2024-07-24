import psycopg2


connection = psycopg2.connect(
    user = "username",
    password = "password",
    host = "localhost",
    port = "5432",
    database = "dbname"
    )


cursor=connection.cursor()

cursor.execute("select version()");

data = cursor.fetchone()
print("Connection established to: ", data)

connection.close()