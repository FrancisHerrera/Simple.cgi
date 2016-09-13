# Comp 490 Project 1 - Primer Project/Simple.cgi 
         Status (working)

In this project, you are to create a simple web application.  This web application can be written in any programming language of your choice.  However, you must use the simple CGI interface.  I.e., you can’t use the vendor supplied libraries to read access the HTTP Header information.

The functionality of your web application is to be defined by you.  There is a minimal number of features that are required, you are free to add additional features. 

This is a simple web application for Comp 490 with Jeff Wiegley. It satisfies the minimum requirements I believe.

1. It responds to the GET verb.

2. It has a different response based upon the URI provided to the application. 

3. It returns HTML and links to one Cascading Style Sheet, on the csun server. 
  Url for css sheet:     http://www.csun.edu/~fah36765/css/simple.css 
  
4. It consumes information from the file system. Prints the SCRIPT_FILENAME on the html page. 
         /home/users15/fah36765/public_html/cgi-bin/simple.cgi

5. It consumes information from a remote web-server according to the URI provided in the query string. 

6. Web application url : http://www.csun.edu/~fah36765/cgi-bin/simple.cgi 
