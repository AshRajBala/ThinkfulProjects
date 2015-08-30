# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:13:43 2015

@author: AshRajBala
"""

"""
At command prompt:
PART 1: CONNECT TO THE DATABASE 
cd /Users/AshRajBala/Repositories/ThinkfulProjects
sqlite3 getting_started.db 
 
PART 2: CREATE TABLES (originally created in csvs & imported into sqlite)
Note: #Make sure the csv is saved as a Windows Comma Separated CSV, not *just* as a Comma Separated File.
#Mac tags a ^M (end of line character) to each row, which pollutes the data imported into sqlite.


DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS weather;
.tables #terminal output: nothing, implying no tables exist now. 

CREATE TABLE cities (name text, state text); #STEP 1: You have to create a new table before loading the CSV into it
.separator "," #STEP 2: Set the comma separator
.import cities.csv cities #STEP 3: tell SQLite to import the data into the table using the .import command

CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);
.separator "," 
.import weather.csv weather
"""


# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('getting_started.db')

"""
PART 3: INSERTING DATA INTO TABLES
"""

cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 45),
                     ('Atlanta', 2013, 'July', 'January', 56))
                     
                     
with con:

    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities) 
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    

"""
PART 4 & 5: JOIN THE DATA TOGETHER & LOAD INTO PANDAS DATAFRAME
Ref: http://stackoverflow.com/questions/1923259/full-outer-join-with-sqlite
"""

import pandas as pd #Normally this import command is declared at the top. 
#However, it is presented here to follow through with the steps as laid down in the assignment

# Select all rows and print the result set one row at a time
with con:

  cur = con.cursor()
  #Joining  all data together - i.e. FULL JOIN 
  #cur.execute("SELECT city, state, year, warm_month, cold_month, average_high FROM cities LEFT JOIN weather ON cities.name=weather.city UNION ALL SELECT state, city, year, warm_month, cold_month, average_high FROM weather LEFT JOIN cities ON cities.name = weather.city WHERE cities.name IS NULL")
  
  #Joining data specific to the requirements of the assigment
  cur.execute("SELECT city FROM weather INNER JOIN cities ON name = city WHERE warm_month = 'July'")
  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows,columns=cols)
  
  print("The cities warmest in July are: %s" % ', '.join(df["city"].values)) #', '.join(df["city"].values will return a comma-separated string

