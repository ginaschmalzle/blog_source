**The Dictionary Data structure**
################################################################################

:date: 2014-07-01 14:56
:tags: dictionaries, python
:category: Home
:slug: dict
:author: **Gina Schmalzle**
:page-order: 1
:summary: **Using dictionaries in Python**

**Dictionaries**
======================================

This page briefly reviews a **dictionary**, also known as an **associative array**, a **map** or a **symbol table**. A dictionary is composed of a collection of keys and values, and each key appears only once in a collection.  JSON files, human-readable files that are commonly used for web applications, contains data objects in the form of a dictionary. 

Let's demonstrate how a dictionary is defined in **python**.  Open a **python** repl by typing on the command line: python.  Once in your repl type::

 a = { 'Hello': 'How are you?'}

'a' is a dictionary. Notice how it was defined with the curly brackets.  This dictionary contains one *key* on the left of the colon, and one *value* on the right side of the colon.  You can retrieve the *value* by typing in the repl::

 a['Hello']

and pressing enter, which returns 'How are you?'.  You can retreive the list of keys by typing::

 a.keys()

and pressing enter, which returns 'Hello'.  Now let's make this dictionary a little more complicated::

 a = { 'Hello': 'How are you?', 'Goodbye': 'See you Later!' }

Here you now have two keys that have their own associated values.  Here you can still run::

 a['Hello']

which will still return 'How are you?', but now you can type::

 a['Goodbye']

which returns 'See you Later!'  A list of keys can be obtained by typing::

 a.keys()

which returns the keys in a list form: ['Hello', 'Goodbye'].  These keys can be retrieved individually by specifying their element indices starting at 0.  For example::

 a.keys()[0]

returns 'Hello'.  Making sense?  OK, let's add one more layer of abstraction which is that the values (of the key/value pair) can be a dictionary.  Changing our dictionary again, type::

 a = { 'Hello': 'How are you?', 'Goodbye': {'a':'See you Later!','b':'Later Gator' }}

into the python repl.  Notice that the key 'Goodbye' now points to a dictionary.  If you type into the python repl:: 

 a ['Goodbye']

you now get the dictionary {'a': 'See you Later!', 'b': 'Later Gator'}.  You can choose a particular value of this sub-dictionary by specifying::
 
 a ['Goodbye']['b']

which returns 'Later Gator'.  


`Return to Populating a Database </pop_db.html>`_!