import pyodbc
import pandas.io.sql as psql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style='darkgrid')
import numpy as np
from datetime import datetime
import calendar
import matplotlib.dates as mdates

server = 'hurricane-iot-server.database.windows.net'
database = 'hurricane-iot'
username = 'dwg11'
password = 'Presence.19'

driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def iso8601_to_epoch(datestring):
    """
    iso8601_to_epoch - convert the iso8601 date into the unix epoch time
    >>> iso8601_to_epoch("2012-07-09T22:27:50.272517")
    1341872870
    """
    return calendar.timegm(datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S.%f").timetuple())

def tempVis(X):
#     cursor.execute(X)
#     rows = cursor.fetchall

#     Create dataframe
    df = psql.read_sql(X, cnxn)
    df.rename(columns={'TEMPERATURE': 'Temperature', 'TIMESTAMP': 'Time'}, inplace=True)
    df.sort_values(by='Time', ascending=False)

    df.to_csv(path_or_buf="/Users/cschenker/Documents/Data.csv")
    print (df)

#   select most recent data point
    row = df.iloc[0]
    origin = row.iloc[-1]

#   create a new dataframe containing only the data within your desired range
#     days = 7
#     seconds = 86400.0
#     range = days * seconds
#     time_lim = origin - range
#     df_recent = df[df['Time'] >= time_lim]
#     df_recent['Time'] = pd.to_datetime(df_recent['Time'], unit='s')
#     df_recent['Time'] = df_recent['Time'].apply(str)
#     func = mdates.strpdate2num('%Y-%m-%d %H:%M:%S')
#     df_recent['Time'] = df_recent.Time.apply(func)
#
#     print (df_recent['Time'])
#
#
#
#     plt.plot_date(df_recent['Time'], df_recent['Temperature'], fmt='r-')
#     plt.show()
#
#     print (df_recent)

tempsql = "SELECT TEMPERATURE, TIMESTAMP FROM Data"
tempVis(tempsql)