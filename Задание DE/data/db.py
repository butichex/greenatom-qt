import psycopg2
from psycopg2 import sql
from config import load_db_config


def get_conn():
    # Load the database connection details from a separate configuration file
    db_config = load_db_config()

    # Connect to the database
    conn = psycopg2.connect(**db_config)
    return conn


def create_table():
    # Get the database connection
    conn = get_conn()

    # Create a cursor
    cur = conn.cursor()

    # Check if the table already exists
    table_name = "missions"
    cur.execute("SELECT to_regclass(%s);", (table_name,))
    exists = cur.fetchone()[0]

    if exists:
        print("Table {} already exists.".format(table_name))
        cur.close()
        conn.close()
        return

    # Use a prepared statement to create the table, which is more secure
    # against SQL injection attacks
    table_cols = [
        sql.SQL("details TEXT"),
        sql.SQL("rocket_name TEXT"),
        sql.SQL("mission_name TEXT"),
        sql.SQL("mission_id TEXT"),
    ]
    create_table_stmt = sql.SQL("CREATE TABLE {} ({});").format(
        sql.Identifier(table_name), sql.SQL(', ').join(table_cols)
    )
    cur.execute(create_table_stmt)

    # Commit the changes
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()


def insert_data(details, rocket_name, mission_name, mission_id):
    conn = get_conn()
    cur = conn.cursor()

    insert_data_stmt = """
        INSERT INTO missions (details, rocket_name, mission_name, mission_id)
        VALUES (%s, %s, %s, %s);
    """
    data = (details, rocket_name, mission_name, mission_id)
    cur.execute(insert_data_stmt, data)

    conn.commit()

    cur.close()
    conn.close()
