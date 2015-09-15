
# coding: utf-8

# In[ ]:

import time
from dateutil.parser import parse
import collections
import sqlite3 as lite
import requests
import pandas as pd

con = lite.connect('citi_bike.db')
cur = con.cursor()

# Data needs to be imported from JSON format. Here, we are taking the stationBeanList and passing values associated 
# with it to pandas to create a DataFrame out of the data instead of the whole JSON.
  
r = requests.get('http://www.citibikenyc.com/stations/json')

from pandas.io.json import json_normalize
df = json_normalize(r.json()['stationBeanList'])

exec_time = parse(r.json()['executionTime']) 
    
#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

    #create the table
    #in this case, we're concatentating the string and joining all the station ids (now with '_' and 'INT' added)
    
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")
    
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    con.commit()

for i in range(60):   
    id_bikes = collections.defaultdict(int)
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']
    for k, v in id_bikes.items():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
    con.commit()
    time.sleep(60)

con.close() #close the database connection when done


# In[ ]:

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')


# In[ ]:

hour_change = collections.defaultdict(int)
for col in df.columns:
    station_vals = df[col].tolist()
    station_id = col[1:] #trim the "_"
    station_change = 0
    for k,v in enumerate(station_vals):
        if k < len(station_vals) - 1:
            station_change += abs(station_vals[k] - station_vals[k+1])
    hour_change[int(station_id)] = station_change #convert the station id back to integer


# In[ ]:

def keywithmaxval(d):
    # create a list of the dict's keys and values; 
    v = list(d.values())
    k = list(d.keys())

    # return the key with the max value
    return k[v.index(max(v))]

# assign the max key to max_station
max_station = keywithmaxval(hour_change)


# In[ ]:

#query sqlite for reference information
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,))
data = cur.fetchone()
print "The most active station is station id %s at %s latitude: %s longitude: %s " % data
print "With " + str(hour_change[379]) + " bicycles coming and going in the hour between " + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S') + " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S')


# In[ ]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.bar(hour_change.keys(), hour_change.values())

