import pyodbc
import pandas.io.sql as psql
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

server = 'hurricane-iot-server.database.windows.net'
database = 'hurricane-iot'
username = 'dwg11'
password = 'Presence.19'

driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def tempVis(X):
#     Create dataframe
    df = psql.read_sql(X, cnxn)
    df.rename(columns={'TEMPERATURE': 'Temperature', 'TIMESTAMP': 'Time'}, inplace=True)
    df.sort_values(by='Time', ascending=False)

#   select most recent data point
    row = df.iloc[0]
    origin = row.iloc[-1]

#   create a new dataframe containing only the data within your desired range
    days = 7
    seconds = 86400.0
    range = days * seconds
    time_lim = origin - range
    df_recent = df[df['Time'] >= time_lim]
    df_recent['Time'] = pd.to_datetime(df_recent['Time'], unit='s')
    df_recent['Time'] = df_recent['Time'].apply(str)
    func = mdates.strpdate2num('%Y-%m-%d %H:%M:%S')
    df_recent['Time'] = df_recent.Time.apply(func)


#   plot the function
    # sns.set_style('darkgrid')
    # plt.plot(df_recent['Time'], df_recent['Temperature'], color='cyan', lw = 2.5)
    # plt.xlim(time_lim, origin)
    med_temp = 40.0
    dev = 10.0
#   plt.ylim(med_temp - 20, med_temp + dev)

    # figure size
    plt.figure(figsize=(12, 9))

    # get rid of spines
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # axis ticks only on bottom and left
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # set plot range limits
    # xmin =
    #
    # above = df_recent.copy()
    # below = df_recent.copy()
    #
    # above.replace('Temperature'<= 40.0, np.NaN)
    # below.replace('Temperature' > 40.0, np.NaN)
    #
    #
    # plt.plot(above['Time'],above['Temperature'], color='r')
    # plt.plot(below['Time'],below['Temperature'], color='g')


    plt.plot_date(df_recent['Time'],df_recent['Temperature'], fmt='r-')
    # plt.axis('tight')
    # plt.xlabel('Time (days)')
    # plt.ylabel('Temperature (degrees Fahrenheit)')
    plt.title('Refridgerator Temps Over Time')
    plt.show()

    print (origin)
    print (df_recent)
    # print df.head()
    # sns.tsplot(data=df_recent, time="", unit="subject", condition="ROI", value="BOLD signal")


# generate humidity graph
# def humidityVis(sql):
#     df = psql.read_sql(X, cnxn)
#     df.rename(columns={'HUMIDITY': 'Humidity', 'TIMESTAMP': 'Time'}, inplace=True)
#     df.sort_values(by='Time', ascending=False)
#
#     row = df.iloc[0]
#     origin = row.iloc[-1]
#
#     #   create a new dataframe containing only the data within your desired range
#     days = 7
#     seconds = 86400.0
#     range = days * seconds
#     time_lim = origin - range
#     df_recent = df[df['Time'] >= time_lim]
#     df_recent['Time'] = pd.to_datetime(df_recent['Time'], unit='s')
#     df_recent['Time'] = df_recent['Time'].apply(str)
#     func = mdates.strpdate2num('%Y-%m-%d %H:%M:%S')
#     df_recent['Time'] = df_recent.Time.apply(func)


tempsql = "SELECT TEMPERATURE, TIMESTAMP FROM Data"
tempVis(tempsql)

# humiditysql = "SELECT HUMIDITY, TIMESTAMP FROM Data"
# humidityVis(humiditysql)




