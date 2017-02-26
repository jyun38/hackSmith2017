# hackSmith2017

In order to run the file access the hack directory. Run: "python3 practice.py" on the command line. In order to use the Google API, you must go to: https://developers.google.com/google-apps/realtime/realtime-quickstart and use wizard to donwload a client id. Then you must chagne each id in each html file with the corresponding client id. Go to a web server and open http://localhost:4000 in order to run the program. A valid username and password is: "jchung@smith.edu pass0". Explore. Please have fun. :)  

Details on the process:
dbmaker.py creates the database template called database.db --- Referenced: http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/, https://pythonspot.com/login-authentication-with-flask/, 
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/. 
tablemaker.py updates the template database.db with the information of data we need from "test.csv" file. 

test.csv includes information of useremail, password, type of admin 

templates directory includes the different modals of our website:
- contacts.html : the page for the TA contact info
- CSCxxxHome.html : the page for a lab queue session 
- login.html : the beginning login page 
- pageError*.html : error pages

static directory includes the css codes:
- hack.css: CSS for websites
- style.css: CSS for the login.html 


