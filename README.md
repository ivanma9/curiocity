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
To test the login and signup functions in user.js on postman:

POST: *server url*/signup
Ex:
    {
        "username": "user1",
        "password": "user1password"
    }

"signup failed" --> if username already exists in database
"signup sucessfully" --> account successfully added to database

POST: *server url*/login
Ex:
    {
        "username": "user1",
        "password": "user1password"
    }

"authorized login" --> if username and password successfully matched
"unauthorized login" --> username and password did not match
"need to register account" --> username does not exist in database

