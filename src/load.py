import psycopg2

def load(df):
    conn = psycopg2.connect(
        dbname="sales_db",
        user="postgres",
        password="password",
        host="localhost"
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO sales VALUES (%s, %s, %s, %s, %s)",
            tuple(row)
        )

    conn.commit()
    conn.close()