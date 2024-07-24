import psycopg2


connection = psycopg2.connect(
    user = "thompilot",
    password = "pithomba",
    host = "localhost",
    port = "5432",
    database = "djangoproj"
    )


cursor=connection.cursor()

cursor.execute("select version()");

data = cursor.fetchone()
print("Connection established to: ", data)

connection.close()