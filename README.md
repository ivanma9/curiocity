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

`POST: *server url* /signup`
<br />
Ex:
    {
        "username": "user1",
        "password": "user1password"
    }
<br />

`"signup failed"` --> if username already exists in database
<br />

`"signup sucessfully"` --> account successfully added to database
<br />

`POST: *server url*/login`
<br />
Ex:
    {
        "username": "user1",
        "password": "user1password"
    }
<br />

`"authorized login"` --> if username and password successfully matched
<br />

`"unauthorized login"`--> username and password did not match
<br />

`"need to register account"` --> username does not exist in database

***CurioCity***

Yelp calls
Using Yelp Fusion API


In node to run locally,
`npm install`
`node yelptest.js`
<br/>

# Schemas

In order to run the script to load the yelp API data run 

## Schema for yelp post request
`python3 getYelpAPI.py`
```
{
    "res": [
        {
            "businesses": [
                {
                    "id": "1234",
                    "name": "Uncle Af's"
                },
                {
                    "id": "5678",
                    "name": "Haggen Dauz"
                }
            ]
        },
        {
            "businesses": [
                {
                    "id": "4321",
                    "name": "Howlin Ray's"
                },
                {
                    "id": "8765",
                    "name": "Ten Ren tea"
                }
            ]
        }
    ]
}
```
Each time it says `{"businesses": [<array of results>]}` , this means that this is one yelp query did for city A.
Each entry inside `'businesses'` is represented as a shortened object of the whole location or business entry from yelp
The goal is to be able to take every single location or business entry and add that to the database. Trying to do it with `insertMany()` for every single `'businesses'`

.env variables
make sure to put `require('dotenv').config();` to use env variables.

### Curiocity API

| Verb   | Route                 | Description                                                         |
| ------ | --------------------- | ------------------------------------------------------------------- |
| POST   | `/insertbusinesses`                 | Creates an account for the user and returns the user's data         |
| GET    | `/me`                 | Login given user cookies and verifies the data aligns w/ the server |
| DELETE | `/me`                 | Removes a user's info from the database                             |
| ------ | --------------------- | ------------------------------------------------------------------- |
| POST   | `/lobby`              | Creates a new lobby and returns the lobby id w/ lobby data          |
| GET    | `/lobby`              | Returns the lobbies a user is managing and participating in         |
| ------ | --------------------- | ------------------------------------------------------------------- |
| POST   | `/lobby/:id`          | Join a lobby                                                        |
| PATCH  | `/lobby/:id`          | Update a lobbies information                                        |
| GET    | `/lobby/:id`          | Get lobby specific info                                             |
| DELETE | `/lobby/:id`          | Delete a lobby                                                      |
| DELETE | `/lobby/:id/user/:id` | Delete a user from a lobby                                          |