# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:56:37 2015

@author: AshRajBala
"""

"""
INSTALLATIONS:
Make sure pysqlite is installed. 
Link: https://pypi.python.org/pypi/pysqlite
"""

#****************************************************************************#
"""
INITIALIZATION PARAMETERS 
"""
#****************************************************************************#

# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('getting_started.db')




#****************************************************************************#
"""
RETRIEVING SQL VERSION USING FETCHONE() COMMAND
"""
#****************************************************************************#
with con:
  # From the connection, you get a cursor object. 
  # The cursor is what goes over the records that result from a query.
  cur = con.cursor()  
  cur.execute('SELECT SQLITE_VERSION()')
  
  # You're fetching the data from the cursor object. 
  # Because you're only fetching one record, you'll use the `fetchone()` method. 
  # If fetching more than one record, use the `fetchall()` method.
  data = cur.fetchone()
  # Finally, print the result.
  print("SQLite version: %s" % data)
  
"""
TERMINAL OUTPUT:
<sqlite3.Cursor object at 0x114acbb90>
SQLite version: 3.8.4.1
"""


"""
You can execute any SQLite command right inside the execute() method. 
You can create tables, insert rows into tables, drop tables, perform selects, joins, etc. 
If you're executing a query, you can fetch the result set using 
the fetchone() or fetchall() methods, and store the result set as an object 
that you can perform further analysis on using Python.  
"""


#****************************************************************************#
"""
INSERTING DATA WITH EXECUTE() COMMAND
"""
#****************************************************************************#

with con:

    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 62)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 64)")

"""
TERMINAL OUTPUT:
>>> with con:
...     
...     cur = con.cursor()
...     cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
...     cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
...     cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 62)")
...     cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 64)")
... 
<sqlite3.Cursor object at 0x114b6b3b0>
<sqlite3.Cursor object at 0x114b6b3b0>
<sqlite3.Cursor object at 0x114b6b3b0>
<sqlite3.Cursor object at 0x114b6b3b0>
"""


#****************************************************************************#
"""
INSERTING DATA WITH EXECUTEMANY() COMMAND
"""
#****************************************************************************#

"""
Instead of passing values directly to execute() and writing a statement for each row 
you want to add, you can pass a tuple of tuples containing the values you want to add 
and write a single statement for them all using the executemany().
"""

cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 45),
                     ('Atlanta', 2013, 'July', 'January', 56))


# Inserting rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities) 
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)


"""
In the above example, the first argument to executemany() is a parameterized SQL statement 
in which placeholders (represented by '?') are used instead of directly writing values into 
statements. 
The second argument to executemany() [i.e. "cities" in the first executemany() statement, 
and "weather" in the second) is the data that you want to insert at the placeholders 
in our parameterized SQL.
"""

 #****************************************************************************#
"""
RETRIEVING DATA WITH FETCHALL() COMMAND
"""
#****************************************************************************#

"""
Now that you've inserted some data, let's fetch it back.
"""

with con:    

    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print(row)

"""
TERMINAL OUTPUT:
<sqlite3.Cursor object at 0x114b6b490>
('New York City', 'NY')
('Boston', 'MA')
('Chicago', 'IL')
('Miami', 'FL')
('Dallas', 'TX')
('Seattle', 'WA')
('Portland', 'OR')
('San Francisco', 'Californ-I-A')
('Los Angeles', 'Californ-I-A')
('Washington', 'DC')
('Houston', 'TX')
('Las Vegas', 'NV')
('Atlanta', 'GA')
"""

"""
Here, the SQL statement within execute() selects all the records from the cities table, 
and the fetchall() fetches the result set of that select query. 
Then, for each row in the result set, you print the row. 
As you can imagine this won't always be useful. 
Instead, you can fetch them and store them in a pandas dataframe:
"""

import pandas as pd
# Select all rows and print the result set one row at a time
with con:

  cur = con.cursor()
  cur.execute("SELECT * FROM cities")

  rows = cur.fetchall()
  df = pd.DataFrame(rows)


"""
You have a dataframe, but if you call df.head() you'll notice that we don't 
have our column names. You can get this information from the cur.description attribute, 
which is a read-only attribute that contains 7 tuples:
name
type_code
display_size
internal_size
precision
scale
null_okay
"""

with con:

  cur = con.cursor()
  cur.execute("SELECT * FROM cities")


  rows = cur.fetchall()
  #cols = [desc[0] for desc in cur.description] => 'name' is at the 0th position
  cols = [desc[0] for desc in cur.description]
  # This will return a list of column names that you can pass to the columns argument 
  #of pd.DataFrame:
  df = pd.DataFrame(rows, columns=cols)
  
  


        
        