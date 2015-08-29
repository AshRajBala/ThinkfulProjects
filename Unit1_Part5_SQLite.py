# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:34:35 2015

@author: AshRajBala
"""


"""
Projects at Thinkful.com
"""

"""
SQLITE
"""

"""
TERMINOLOGY:
 A relational database stores information about both data and how it is related. 
 Data and relationships are represented in flat, two-dimensional tables that preserve relational structuring. 
 A database table is a set of values organized into columns and rows. 
 A database row represents a single data item in a table, and is sometimes called a tuple or a record. 
 A field is a single item at one column and one row position.
 """
 
 """
 At terminal, type: sqlite3 --version
 """
 
 #****************************************************************************#
 """
 SQLITE INTRO:
 """
 #****************************************************************************#

# At terminal, type: 
 cd /Users/AshRajBala/Repositories/ThinkfulProjects
 sqlite3 getting_started.db #Creates an empty database
 
# Information about the state of the database: (starts with a .)
# At terminal, type: 
.tables
#Terminal output: Nothing (because database is currently empty)

.indices
#Terminal output: Nothing (because database is currently empty)

.schema
#Terminal output: Nothing (because database is currently empty)


#****************************************************************************#
"""
CREATING TABLES: DETAILED EXAMPLE 
"""
#****************************************************************************#

CREATE TABLE cities (name text, state text);

"""
For the command above:
CREATE TABLE is the SQL command for creating a new table
cities is the name of the table we want to create
The opening parenthesis indicates the start of the list of columns which the table will hold
The different columns will be separated by commas
name text is an example of a column definition
The column name will be name
The data type of the column is text (i.e. the column will hold a string of text)
"""

INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');

"""
For the command above:
New rows are added using the INSERT INTO command. 
You specify that the rows want to be added to the cities table. 
The (name, state) section indicates which columns you are adding data to, 
and the order in which you will supply the data. In this case the name of the city comes first, 
and the state the city belongs to comes second.

VALUES indicates the start of the list of values which you are going to insert. 
Each row is supplied as a list of values contained in parentheses. 
So for example here you create a row where the name column contains the value "New York City", 
and the state column contains the value "NY".    
"""

#****************************************************************************#
"""
CREATING TABLES: QUICK, SECOND EXAMPLE 
"""
#****************************************************************************#

 CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);
 
 INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES
 ('New York City',   2013,    'July',        'January',   62),
 ('Boston',          2013,    'July',        'January',   59),
 ('Chicago',         2013,    'July',        'January',   59),
 ('Miami',           2013,    'August',      'January',   84),
 ('Dallas',          2013,    'July',        'January',   77),
 ('Seattle',         2013,    'July',        'January',   61),
 ('Portland',        2013,    'July',        'December',  63),
 ('San Francisco',   2013,    'September',   'December',  64),
 ('Los Angeles',     2013,    'September',   'December' , 75);
 
 .table
 #Terminal Output: cities weather
 
 .schema
#Terminal Output: CREATE TABLE cities (name text, state text);
#                 CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);
 
 
#****************************************************************************#
"""
WRITING QUERIES ON YOUR DATA 
"""
#****************************************************************************#

SELECT * FROM cities;
# This command ask SQLite to query for all of the columns (*) in the cities table. 
# You should see each of the rows you create earlier printed back.

"""
TERMINAL OUTPUT:
New York City|NY
Boston|MA
Chicago|IL
Miami|FL
Dallas|TX
Seattle|WA
Portland|OR
San Francisco|CA
Los Angeles|CA
"""

SELECT name, state FROM cities WHERE state='CA';
#In this case we look for cities which are in California, by returning the rows 
#where the state column is equal to CA.

"""
TERMINAL OUTPUT:
San Francisco|CA
Los Angeles|CA
"""

SELECT name FROM cities WHERE name LIKE '%le%';

"""
TERMINAL OUTPUT
Seattle
Los Angeles
"""

SELECT name FROM cities LIMIT 2 OFFSET 3;

"""
TERMINAL OUTPUT:
Miami
Dallas
"""

"""
Sometime you don't want to deal with all of your data at once. 
This example introduces the LIMIT and OFFSET clauses. 
The LIMIT clause limits the number of rows that are returned by the query. 
The OFFSET clause ignores the first N rows which match the query, giving you an offset into the data. 
So this query will return the fourth and fifth cities only.
"""

SELECT COUNT(*) FROM cities WHERE name LIKE 'San%' AND state='CA';

"""
TERMINAL OUTPUT:
1
"""

"""
The COUNT function is used to return the number of rows which match a query. 
So in this example you count the number of cities in California which start with the string "San". 
Notice how we can logically combine two WHERE clauses using AND, OR and NOT.
"""

"""
SQLite contains a number of additional built-in functions which you may find useful. For example:

SUM() finds the sum of the results
AVG() finds the average of the results
MIN() finds the lowest result
MAX() finds the highest result
"""


#****************************************************************************#
"""
UPDATE YOUR DATA 
"""
#****************************************************************************#

UPDATE cities SET state='Californ-I-A' WHERE state='CA';

"""
To change the values held in a table you use the UPDATE command.
"""

#****************************************************************************#
"""
DELETE YOUR DATA 
"""
#****************************************************************************#

DELETE FROM cities where state='CA';


#****************************************************************************#
"""
EXPORT YOUR DATA TO CSV
"""
#****************************************************************************#

"""
In some situations, we might want to export a table in a database or 
the results of a query on a database, to a CSV.
"""

.mode csv #STEP 1: Switch the output mode to CSV
.headers on #STEP 2: Turn the column headers on
.output cities.csv #STEP 3: You tell SQLite to output any statements to the cities.csv file 
select * from cities; #STEP 4: You make the query to select all of the rows from the cities table.
.output stdout #STEP 5: Redirect output to the command line

#****************************************************************************#
"""
IMPORT DATA TO CSV
"""
#****************************************************************************#

create table cities_copy (name text, state text); #STEP 1: You have to create a new table before loading the CSV into it
.separator "," #STEP 2: Set the comma separator
.import cities.csv cities_copy #STEP 3: tell SQLite to import the data into the table using the .import command

# IMPORTANT NOTE:
# To make sure that it worked, run the .tables command one more time.
