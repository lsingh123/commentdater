commentdater
=======================

commentdater is a command line tool that reminds you to update your comments when you change a line of code.

Installation
-----------------------
`pip install commentdater`

Usage
-----------------------
    usage: commentdater [-h] -f FILE

    Check if your comments are out of date

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  file to check

Dependencies 
-----------------------
commentdater uses git. to install git command line tools, https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
      
Tests
-----------------------
Modify the infiles in commentdater/test_data/ as indicated in the code 
    
    python test.py
   

Author
-----------------------
<lsingh@college.harvard.edu>
