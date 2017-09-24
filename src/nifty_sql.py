import pyodbc
import pandas.io.sql as psql

server = 'hurricane-iot-server.database.windows.net'
database = 'hurricane-iot'
username = 'dwg11'
password = 'Presence.19'

# Initialization
driver='{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# INSERT statement
def insert(column_names=[], values=[]):
    """

    :param key_value_pairs: The column_names variable should be a list of strings. Each string refers to the name of a column.
                    The values should be a list of lists (or tuples) where each entry in the list is a row in the table.
    :return:
    """

    for value in values:
        value_str = map(lambda x : str(x), value)
        command = "INSERT INTO Data (%s) VALUES (%s)" % ( ",".join(column_names), ",".join(value_str) )
        print command
        cursor.execute(command)
        cnxn.commit()



def select_statement(cmd="SELECT Data, Temperature, Humidity FROM Data"):
    # SELECT statement
    cursor.execute(cmd)


    # Prints what was last in your cursor
    row = cursor.fetchone()
    while row:
        print 'Inserted Product key is ' + str(row)
        row = cursor.fetchone()

def sql_command(cmd=""):
    cursor.execute(cmd)
    cnxn.commit()

def sql_query(X="SELECT Timestamp, Temperature, Humidity, SoundDecibels FROM Data"):
    df = psql.read_sql(X, cnxn)
    return df