***CurioCity***

Yelp calls
Using Yelp Fusion API


In node run 
`npm install`
`node yelptest.js`
<br/>

In python run 
`python3 app.py`

.env variables
make sure to put `require('dotenv').config();` to use env variables.


**Sign up and log in**
<br />
To test the login and signup functions in user.js on postman:
<br />
POST: *server url*/signup
<br />
Ex:
    {
        "username": "user1",
        "password": "user1password"
    }
<br />
"signup failed" --> if username already exists in database
<br />
"signup sucessfully" --> account successfully added to database
<br />

POST: *server url*/login
<br />
Ex:
    {
        "username": "user1",
        "password": "user1password"
    }
<br />
"authorized login" --> if username and password successfully matched
<br />
"unauthorized login" --> username and password did not match
<br />
"need to register account" --> username does not exist in database

