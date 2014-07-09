**SQLite3 Databases: Creating, Populating and Retreiving Data, Part 1** 
################################################################################

:date: 2014-07-04 14:56
:tags: SQLite, relational database
:category: Home
:slug: make_db
:author: **Gina Schmalzle**
:page-order: 1
:summary: **Creating a Database**


Structured Query Language (SQL) is a langauge that is used to design and manage data held in a relational database. A relational database is a database that contains multiple tables that contain related values.  For example, one table may contain names of people and their ages, and another may contain names of people and their favorite color. The names of the people are the related values. SQL provides a relatively easy (and commonly used) way of extracting only the data you want from the database that can later be analyzed or visualized. 

`David Branner <https://github.com/brannerchinese>`_, a fabulous **python** coder who dabbles in creating and using **SQLite** databases, and knows a thing or two about the `Chinese Language <https://brannerchinese.com/>`_, and I are working on `The Weather Project <https://github.com/WeatherStudy/weather_study>`_ where we intend to examine the accuracy of weather forecasts. In order to do that, we need to collect weather forecasts that will be analyzed.  We decided to use weather forecasts from `Open Weather Map <http://openweathermap.org/>`_, a website that gives open access to weather forecasts through an API key. Through the API key, we are able to download JSON files that contain information on the weather forecasts at specific locations around the world. Our goal is for each day to collect weather forecasts for that day and from 1 day before to about two weeks out. We collect the maximum temperature (maxt), the minimum temperature (mint), snow and rain forecasts for each of the forecasts.  Then we subtract the predicted value from the observation to estimate how much the forecast predicts warmer/cooler temperatures or more/less snow and rain.  Hence, we need to collect a lot of information and organize it in a way that will be relatively easy and consistent to retreive. To do that, we created an SQLite3 database. This blog is the first of three, and focuses on **creating a Database with SQLite3**.  The next blogs will cover **Populating an SQLite Database with Data using Python** and **Retrieving data from an SQLite Database using Python**.  


**Part 1: Creating a Database with SQLite3**
==============================================

**SQLite** is a compact and self contained relational database management system. We decided to use **SQLite3** (Mac OS X's version of SQLite) because 
 
 1. It is included on the Mac OS X operating system (/usr/bin/sqlite3)
 2. It does not require a server and no need for an administrator
 3. It does not include any configuration files
 4. No action is required after a system crash

Certainly, there are issues with **SQLite**, but for our humble little project **SQLite** provides all the functionality we wanted. If you are running Mac OSX you can use SQLite3.  Be sure that /usr/bin/ is in your path (it already should be there).  You can check to see if you have it by typing::

 which sqlite3  

Let's get started.  First, a few things about sqlite3. You can enter the sqlite3 `repl <http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`_ by simply typing sqlite3 at the command line.  Or, you can type::

 sqlite3 mydatabase.db 

to ensure your creations/populations/extractions are all for the database mydatabase.db (or whatever you want it named).  If you make a sqlite3 script that is applied to mydatabase.db called myscript.sql, you can run it at the command line by typing:: 

 sqlite3 mydatabase.db < myscript.sql.

Our **SQLite** database that we named *weather_data_OWM.db* is set up with multiple tables.  Information within those tables are related, and is referred to as a *relational database*.  As previously mentioned, a relational database is setup so that there is some common information between tables that helps link them.  Our database tables are linked by city id.  The city id is simply a unique number assigned to each location that has a weather forecast.  In one table we keep the properties of each location, such as the latitude, longitude, city name, etc.  In the other, we assign the forecasts to each city id.  Let's take a closer look at how this works. 

The first thing we did was create a TABLE called *locations* which contains the id, name, latitude, longtiude and country::

 DROP TABLE IF EXISTS locations;
 CREATE TABLE locations (
    id TEXT PRIMARY KEY UNIQUE,
    name TEXT,
    lat NUMBER,
    lon NUMBER,
    country TEXT
 );

Eeeek! The "DROP TABLE" part of this code is a little scary -- here we are saying if there is already a table in our database called *locations* then remove it!  The table *locations* will be completely removed and can not be recovered.  You may ask, *why would you want to do that???* Well, this code is simply meant to provide the bones for our database.  The only reason we are running this script is to make a database from scratch, and if one exists, it should be removed.  It is also recommended because you don't want to confuse the current data with other data sets if a table called *locations* exists.  So **BE CAREFUL** with this command.  

The next command lines create the table with columns that are defined as containing a certain type of field.  The columns that we have are id, name, lat, lon and country and are either TEXT (strings) or NUMBERS (floats).  The id column is special because it also contains PRIMARY KEY command.  The PRIMARY KEY command ensures that all rows in that column are uniquely identifiable.  To be extra certain of this (but may be a little redundant), we also included UNIQUE, which ensures that all values in the column are different. 

How can we tell if the table was made properly?  If you entered the commands above in the repl, then type::

 SELECT * FROM sqlite_master WHERE type='table';

What should print out is information on your new table, including its structure:: 

 table|locations|locations|2|CREATE TABLE locations (
 id TEXT PRIMARY KEY UNIQUE,
 name TEXT,
 lat NUMBER,
 lon NUMBER,
 country TEXT
 )

The line "table|locations|locations|2|CREATE TABLE locations" is simply output that states: *type|name|table name|root page #|sql command used to generate the table*. Then the table column names are printed.  

Very good!  Now we have a table that will contain some characteristics of each city. Now let's make a second TABLE that includes the weather forecasts and will be related to the first one by the city code. We are collecting forecasts for up to 14 days before a *target_date* which we define as the day being forecasted.  We want to know the forecasts for rain and snow, as well as the minimum and maximum temperatures for the *target_date*.  As before, we first need to DROP any existing tables, then we create the table::

 DROP TABLE IF EXISTS owm_values;
 CREATE TABLE owm_values (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id TEXT,
    target_date INTEGER,
    maxt_0 NUMBER,
    mint_0 NUMBER,
    rain_0 NUMBER,
    snow_0 NUMBER,
    maxt_1 NUMBER,
    mint_1 NUMBER,
    rain_1 NUMBER,
    snow_1 NUMBER,
    maxt_2 NUMBER,
    mint_2 NUMBER,
    rain_2 NUMBER,
    snow_2 NUMBER,
    maxt_3 NUMBER,
    mint_3 NUMBER,
    rain_3 NUMBER,
    snow_3 NUMBER,
    maxt_4 NUMBER,
    mint_4 NUMBER,
    rain_4 NUMBER,
    snow_4 NUMBER,
    maxt_5 NUMBER,
    mint_5 NUMBER,
    rain_5 NUMBER,
    snow_5 NUMBER,
    maxt_6 NUMBER,
    mint_6 NUMBER,
    rain_6 NUMBER,
    snow_6 NUMBER,
    maxt_7 NUMBER,
    mint_7 NUMBER,
    rain_7 NUMBER,
    snow_7 NUMBER,
    maxt_8 NUMBER,
    mint_8 NUMBER,
    rain_8 NUMBER,
    snow_8 NUMBER,
    maxt_9 NUMBER,
    mint_9 NUMBER,
    rain_9 NUMBER,
    snow_9 NUMBER,
    maxt_10 NUMBER,
    mint_10 NUMBER,
    rain_10 NUMBER,
    snow_10 NUMBER,
    maxt_11 NUMBER,
    mint_11 NUMBER,
    rain_11 NUMBER,
    snow_11 NUMBER,
    maxt_12 NUMBER,
    mint_12 NUMBER,
    rain_12 NUMBER,
    snow_12 NUMBER,
    maxt_13 NUMBER,
    mint_13 NUMBER,
    rain_13 NUMBER,
    snow_13 NUMBER,
    maxt_14 NUMBER,
    mint_14 NUMBER,
    rain_14 NUMBER,
    snow_14 NUMBER,
    UNIQUE (location_id, target_date),
    FOREIGN KEY (location_id) REFERENCES locations(id)
    );

In this table, each forecast is given its own, unique id (called id).  In addition, it contains a location_id, which will refer to *id* in our first TABLE, *locations*.  These values 'link' the two tables, creating a relational database. The FOREIGN KEY statement defines this relationship, stating that the location_id of the TABLE *owm_values* is REFERENCED to the id of TABLE *locations*. We also created columns in our TABLE that will store forecasts from the day of (\*_0) to 14 days out (\*_14).  UNIQUE ensures that both the location_id and the target_date are unique in this table (i.e., every city will have its own unique id, and every city will have forecasts for unique target dates).  

Now if you type into the repl::

 SELECT * FROM sqlite_master WHERE type='table';

Two tables should print out -- the first one being the *locations* table, the second your brand new *owm_values* table.  

Congratulations!  You have now set up a database in SQLite3 that contains two tables.  Now for  `Part 2 Populating an SQLite Database using Python </pop_db.html>`_ coming soon...  
