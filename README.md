Proj.net---pyODBC
=================

A small code example, for connecting to a database through the ODBC driver with the language Python. In this example, I've used Mac OS 10.6.8

Assumptions:
Installed and working SQL database, with functional connection. 
   
   
Requirements:
* Any OS (Linux, Mac OS and Windows will work).
* Python +2.6 (http://www.python.org/getit/)
* pyODBC (https://github.com/mkleehammer/pyodbc)
* MySQL ODBC Driver (http://www.mysql.com/downloads/connector/odbc/)
   
   
General notes   
=============   
If you are experincing these issues with the ODBC driver, i.e.:   
   
* pyodbc.Error: ('00000', '[00000] [iODBC][Driver Manager]dlopen({MySQL ODBC 5.1 Driver}, 6): image not found (0) (SQLDriverConnect)')   
This means, that the driver is not where is should be (file reference is incorrect, or non-existent).

* pyodbc.Error: ('00000', '[00000] [iODBC][Driver Manager]dlopen(/usr/local/lib/libmyodbc5.so, 6): no suitable image found.  Did find:\n\t/usr/local/lib/libmyodbc5.so: mach-o, but wrong architecture (0) (SQLDriverConnect)')   
The driver is not the correct arhictecture. I.e. your application is 32bit, but you installed the 64bit driver, for you 64bit OS. This wont work on, i.e. Windows. Here you need a 32bit driver, for a 32bit application.

Mac OS notes
============   

* "lipo -i" will help you determine which architecture the plugin is made for. On my Mac OS 10.6.8.