import psycopg2

db_params = {
    'dbname' : 'postgres',
    'user' : 'postgres',
    'password' : '1234',
    'host' : 'localhost',
    'port' : '5432'
}


conn = psycopg2.connect(**db_params)
print("Conexion exitosa")

try:
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS my_movies (
        ID SERIAL PRIMARY KEY,
        Autor VARCHAR(255),
        Descripcion VARCHAR(255),
        FechaDeEstreno DATE

    )
'''

    cursor.execute(create_table_query)

    conn.commit()

except Exception as e:
    print(f"Error:{e}")

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conection Closed.")