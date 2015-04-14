**SQLite3 Databases: Creating, Populating and Retrieving Data, Part 2** 
################################################################################

:date: 2014-07-09 14:56
:tags: SQLite, python, relational database
:category: Home
:slug: pop_db
:author: **Gina Schmalzle**
:page-order: 1
:summary: **Populating a Database**

In `Part 1 Creating a Database with SQLite3 </make_db.html>`_  we built a database.  Here we will use the functionality of Python 3.4 to help populate our database created in Part 1 with data and weather forecasts. This blog assumes you followd Part 1, and have some prior knowledge of Python. Much of this work was done with `David Branner <https://github.com/brannerchinese>`_, who was incredibly patient in teaching me how to do this... Kudos, David!

**Part 2. Populating an SQLite Database using Python**
============================================================================== 

Let's put some data into our database!  First, let's fill up our *locations* TABLE. We collected and keep a list of the cities, their unique codes provided by Open Weather Map, their latitudes and longitudes and their country codes `here <https://raw.githubusercontent.com/WeatherStudy/weather_study/master/data/city_lists/city_list_normalized_20140425-1923.txt>`_, in a file called city_list_normalized_20140425-1923.txt.  This file contains information on the cities and looks like this::

 id	nm	lat	lon	countryCode
 819827	Razvilka	55.591667	37.740833	RU
 524901	Moscow	55.752220	37.615555	RU
 1271881	Firozpur Jhirka	27.799999	76.949997	IN
 1283240	Kathmandu	27.716667	85.316666	NP
 703448	Kiev	50.433334	30.516666	UA
 1282898	Pokhara	28.233334	83.983330	NP
 3632308	Merida	8.598333	-71.144997	VE
 .
 .
 .

We need a way to grab this file and read the contents in python.  Let's create a function that will do just that. If we are in the directory containing the file called city_list_normalized_20140425-1923.txt, we can call the file in python and read its contents::
 
 def isolate_city_codes():
    filename = 'city_list_normalized_20140425-1923.txt'
    with open(filename, 'r') as f:
        contents = f.read()
    list_of_lines = [line.split('\t') for line in contents.split('\n')[1:]]
    # Latitude and longitude should be numbers
    for i in range(1, len(list_of_lines)-1):
        list_of_lines[i][2] = float(list_of_lines[i][2])
        list_of_lines[i][3] = float(list_of_lines[i][3])
    return list_of_lines

Let's break down what the function is doing.  The first thing is that it defines a string called filename as 'city_list_normalized_20140425-1923.txt'.  The next two lines of code are contained in a 'with statement'.  A 'with statement' is a context manager, which provides a way to safely close the opened file and exit out of the python script in case of an error. The contents of the file are read and placed into the variable *contents* that looks something like this::

 'id\tnm\tlat\tlon\tcountryCode\n819827\tRazvilka\t55.591667\t37.740833\tRU\n524901\tMoscow\t55.752220\t37.615555\tRU ... 
 ...
 \n895417\tBanket\t-17.383329\t30.400000\tZW\n'

Notice the once tab seperated entries of the file are now separated with '\\t' and the lines are now separated with '\\n'.  The next line of our program defines list_of_lines, which runs a loop through contents that splits out each line (defined by '\\n') and each tab separated space (defined by '\\t').  list_of_lines now looks like this::

 [['819827', 'Razvilka', '55.591667', '37.740833', 'RU'],
  ['524901', 'Moscow', '55.752220', '37.615555', 'RU'],
  ['1271881', 'Firozpur Jhirka', '27.799999', '76.949997', 'IN'],
  .
  .
  .
  ['895417', 'Banket', '-17.383329', '30.400000', 'ZW']
 ]

So, list_of_lines is a *list of lists*, where a list contains the contents within a set of square brackets.  The problem with the current list_of_lines is that the latitude and longtitudes are strings and must be converted into floats, which is done using the for statement.  Finally, the revised list_of_lines is returned with floats for the latitude and longitude.  

Now, let's populate the TABLE *locations* in the sqlite3 database *weather_data_OWM.db*. We write another function that calls the previous function to grab the data, then it populates the *locations* TABLE with those values::

 import sqlite3
 def populate_db_w_city_codes(db='weather_data_OWM.db'):
    connection = sqlite3.connect(db)
    with connection:
        city_codes = isolate_city_codes()
        cursor = connection.cursor()
        for code in city_codes[1:-1]:
            if code == ['']:
                print('\n    Empty tuple found; skipping.\n')
                continue
            cursor.execute(
                    '''INSERT INTO locations VALUES''' +
                    str(tuple(code)))


Note that we have to import the python module sqlite3.  This module allows you to 'connect' with a specified database.  Once you have a connection, you can create a cursor object that calls its execute() method to perform SQLite3 commands.  In the function described above, we create a *connection* which connects to our database (db = 'weather_data_OWM.db').  Then we apply a context manager (the with statement) to: 

  1. Collect the information contained within *city_list_normalized_20140425-1923.txt* by calling our previous function, *isolate_city_codes()*.  The returned *list_of_lines* from *isolate_city_codes()* is now labeled as *city_codes*.  

  2. Open a *cursor* that will execute subsequent *SQLite3* commands. 

  3. Insert the values of *city_codes* into the *locations* TABLE.

Notice that the SQLite3 commands are imbedded into cursor.execute. The lists within *city_codes* are already in the order we want them (same order as the database columns were set up in, see `Part 1 </make_db.html>`_). They have been 'tuple-ized' and 'string-ified' since this is the format SQLite3 understands.

After executing, you can now check if they were inserted into your database by entering the sqlite3 repl::

 sqlite3 weather_data_OWM.db

Once in the sqlite repl type::

 SELECT * FROM locations;

The output should look something like this::

 .
 .
 .
 894413|Chakari|-18.062941|29.89246|ZW
 894460|Centenary|-16.722891|31.11462|ZW
 895057|Binga|-17.620279|27.341391|ZW
 895417|Banket|-17.383329|30.4|ZW

Your new table should have data that include: *city id|city name|latitude|longitude|two letter country code*.

Splendid!  One table down, one related table to go!  The second table is a bit more complicated.  It involves data that was downloaded through the `Open Weather Map <http://openweathermap.org/>`_ API that allows for easy access to their data products that are available in XML and JSON formats.   Since this blog is focusing on building and populating databases, I assume that you already have the data downloaded in JSON format. I will not get into how to download the data here, but for more information on how to do this, David developed a nifty little python script called `requests.py <https://raw.githubusercontent.com/WeatherStudy/weather_study/master/code/requests.py>`_ that allows you to download data using an API key that is hidden from public access (important when allowing public access to your files in Github). 

We use the JSON formatted files to populate our database.  JSON files are in the form of a dictionary, also known as an associative array.  If you are not familiar with this data structure, I recommend you read `this little ditty </dict.html>`_ before continuing. Otherwise, keep on reading!  

Below is an example of a JSON file obtained using the Open Weather Map API that has been prettified using http://jsbeautifier.org/.  The JSON file contains the forecasts and information for a single city::

 {
    'cod': '200',
    'message': 0.005,
    'city': {
        'name': 'Bay Minette',
        'id': 4046255,
        'coord': {
            'lat': 30.882959,
            'lon': -87.773048
        },
        'population': 8044,
        'country': 'US'
    },
    'list': [{
        'weather': [{
            'description': 'few clouds',
            'icon': '02d',
            'main': 'Clouds',
            'id': 801
        }],
        'temp': {
            'max': 27.32,
            'min': 18.14,
            'eve': 24.57,
            'day': 27.22,
            'night': 18.14,
            'morn': 27.22
        },
        'deg': 199,
        'clouds': 12,
        'pressure': 1020.38,
        'humidity': 42,
        'dt': 1398186000,
        'speed': 2.11
    }, {
        'weather': [{

        .
        .
        .

    }],
    'cnt': 15
 }

Now you see that it is just one giant dictionary, right?  So if we import this into python, then we can call certain values by their keys.  For example, if we call this dictionary x, then we can retrieve the latitude of the city by typing::

 x['city']['coord']['lat']

In this JSON file the 'city' key contains the information about the city itself, and the 'list' key contains information on the weather forecasts, where the first value contains information on the weather forecasts for the day the file was downloaded.  The second value in 'list' contains the forecast for the next day, etc. 

You can see that the file contains the minimum and maximum temperature, and, if it exists, also contains snow and rain amounts. 'dt' is the day the forecast is for in `Unix Time <http://en.wikipedia.org/wiki/Unix_time>`_. The 'query date'  which is the day the file was downloaded is not included in these files but is important because this will tell you which day is the day-of forecast.  We dealt with this problem by downloading the JSON files for each city into a directory with the download date.

The first thing we will need to do here is extract the information we need from these JSON files. For the sake of simplicity, I assume you know the download date and specify it in the python code (rather than extracting it from the directory name). Depending on what region you are collecting, you may have thousands of files for one download date, each corresponding to an individual location. We would like a function that 

  1. Ingests these JSON formatted files and stores the contents as a dictionary

  2. Create a smaller dictionary called *forecast_dict* that contains only the information that we need for our database.  The smaller dictionary should have a 'key' that relates to the city_id, and values that contain the forecasted values. 

I assume that you have the names of your files in a list called *files* that were collected on a specified *query_date*.  I use an example query date of 20140422::
 
 files = [yourfile1.json, yourfile2.json, yourfile3.json... ]  # example files
 
 import ast                                                    
 def retrieve_data_vals(files, query_date='20140422'):
    forecast_dict = {'query_date': query_date}                 # Assign query_date to dictionary
    files.sort()   
    for file in files:
        forecast_list_pruned = []
        try:
            with open(file, 'r') as f:
                contents = f.read()                            # Read in file as a string
        except Exception as e:
            print('Error {}\n    in file {}'.format(e, file))
        if contents == '\n':
            print('File {} empty.'.format(file))
            continue
        content_dict = ast.literal_eval(contents)              # Convert to dictionary
        city_id = (content_dict['city']['id'])                 # Assign city_id
        forecast_list_received =(content_dict['list'])         # Assign everythin in 'list' to forecast_list_received
        for i, forecast in enumerate(forecast_list_received):  # For each forecast in the dictionary
            if 'rain' in forecast:                             # Assign rain, if exists,
               rain = forecast['rain']                         # Otherwise make 0
            else:
               rain = 0
            if 'snow' in forecast:                             # Same with snow
                snow = forecast['snow']
            else:
                snow = 0
            forecast_tuple = (                                 # Assign forecast information in tuple form that is SQLite3 readable (if stringified)
                    forecast['dt'],               
                    float(forecast['temp']['max']),
                    float(forecast['temp']['min']),
                    float(rain),
                    float(snow),
                    )
            forecast_list_pruned.append(forecast_tuple)        # Collect all forecasts for that file
        forecast_dict[city_id] = forecast_list_pruned          # and assign to the forecast_dict for each city
    return forecast_dict


Phew!  Extracting the data from the JSON files and putting it into an SQLite3 friendly format is the toughest part. Now that we have forecast_dict, however, we can populate our database! Our next function will use some of the same techniques described above, which include using the sqlite3 module to make a connection with the sqlite database and execute **SQLite3** commands::

 import sqlite3
 def populate_db_w_forecasts(db='weather_data_OWM.db'):
    forecast_dict = retrieve_data_vals(files)                 # Run the function retrieve_data_vals above which returns the forecast dictionary
    query_date = forecast_dict['query_date']                  # Assign query_date
    connection = sqlite3.connect(db)                          # Create the SQLite3 connection
    with connection:
        cursor = connection.cursor()      
        for key in forecast_dict:
            if key == 'query_date':
                continue                                      # After here, "key" is a location_id.
            for i,item in enumerate(forecast_dict[key]): 
                   target_date = datetime.datetime.fromtimestamp(int(item[0])).strftime('%Y%m%d')                         # Convert the Unix time to human readable string
                   maxt, mint, rain, snow = item[1:]          # Remember forecast dict contains dt, maxT, minT, rain and snow, so we want everything past dt (hence item[1:])
                   i = str(i)
                   fields = ','.join([                        # 'fields' contains question marks that indicate where values will be inserted later in the code
                           'maxt_' + i + '=?',
                           'mint_' + i + '=?',
                           'rain_' + i + '=?',
                           'snow_' + i + '=?'
                           ])
                   try:
                       cursor.execute(                        # Insert the location_id (key) and target_date
                               '''INSERT INTO owm_values '''      
                               '''(location_id,target_date) '''
                               '''VALUES (?,?)''', (key, target_date))
                   except sqlite3.IntegrityError as e:
                       pass
                   cursor.execute(                            # Insert forecast values
                        '''UPDATE owm_values SET ''' + fields +   
                        ''' WHERE id='''
                        '''(SELECT id FROM owm_values '''
                        '''WHERE location_id=? AND target_date=?)''',
                        (maxt, mint, rain, snow, key, target_date)

Let's talk a little about *cursor.execute*. Here we do a little python trick to insert values into the SQLite code.  In cursor.execute, we state the SQLite3 commands, but we include question marks (?).  After the SQLite commands we place a comma then a tuple of values.  These tuple values are inserted into where the question marks appear in the code in the order the question marks appear.  So, in the case of::

                       cursor.execute(
                               '''INSERT INTO owm_values '''
                               '''(location_id,target_date) '''
                               '''VALUES (?,?)''', (key, target_date))

The SQLite3 command is::

 INSERT INTO owm_values (location_id, target_date) VALUES (key, target_date)

where 'key' is the location city id, and 'target_date' is the date the forecast is for.  Note the *location_id* of the *owm_values* TABLE refers to the *city_codes* of the locations TABLE.  

There you go!  You now have a relational database that has been populated with data!  Now what to do with it... Stay tuned for Part 3 Retrieving data from an SQLite Database using Python.  




