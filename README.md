Proj.net---pyODBC
=================

A small code example, for connecting to a database through the ODBC driver with the language Python. In this example, I've used Mac OS 10.6.8

1. Basicly what you want to do, is download the ODBC Driver (from MySQL) & the source of pyODBC
2. Compile the pyODBC connecter (enabling Python to communicate with the ODBC driver).
3. Install the ODBC driver (according to your host OS). This enables you to talk with a SQL server directly.
4. Test code within the script: "pyODBC.py". The rest is example code.

Assumptions:
* Installed and working SQL database, with a functional connection. 
* Python 2.6 installed with working interpreter.
* Knowledge of ODBC, and how it's setup on your specific OS.
* Eclipse or another IDE, to debug/test my code. However you can also run the script from within a terminal, by calling interpreter binary & path_to_script. Like so: "python /opt/bin/pyODBC.py".
   
   
Requirements:
* Any OS (Linux, Mac OS and Windows will work).
* Python +2.6 (http://www.python.org/getit/)
* pyODBC (https://github.com/mkleehammer/pyodbc)
* MySQL ODBC Driver (http://www.mysql.com/downloads/connector/odbc/)
   
   
General notes   
=============   

* To install the Python ODBC module, navigate to the root directory of the source. Then type in to compile and install the .ogg extension: "Python setup.py build install" from the terminal.
   
If you are experincing these issues with the ODBC driver, i.e.:   
* pyodbc.Error: ('00000', '[00000] [iODBC][Driver Manager]dlopen({MySQL ODBC 5.1 Driver}, 6): image not found (0) (SQLDriverConnect)')   
   
This means, that the driver is not where is should be (file reference is incorrect, or non-existent).

* pyodbc.Error: ('00000', '[00000] [iODBC][Driver Manager]dlopen(/usr/local/lib/libmyodbc5.so, 6): no suitable image found.  Did find:\n\t/usr/local/lib/libmyodbc5.so: mach-o, but wrong architecture (0) (SQLDriverConnect)')   
   
The driver is not the correct arhictecture. I.e. your application is 32bit, but you installed the 64bit driver, for you 64bit OS. This wont work on, i.e. Windows. Here you need a 32bit driver, for a 32bit application.

Mac OS notes
============   

* "lipo -i" will help you determine which architecture the plugin is made for.   
On Mac OS 10.6.8, with forced 64bit kernel - It was required of me to use the x86_64 driver architecture, extracted from the contents within the .DMG package installer (took me a few hours to get working).

* "iodbctest" is also a nice tool, to test ODBC DSN connections listed within /Library/ODBC/odbc.ini & /Library/ODBC/odbcinst.ini