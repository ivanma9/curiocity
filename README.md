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

For GET requests, use query string to specify parameters. For POST requests, use the request body to specify parameters.

Parameters column is organized as follows: PARAM1 (value type), PARAM2 (value type), ... 


| Verb   | Route                 | Description                                                         | Parameters |
| ------ | --------------------- | ------------------------------------------------------------------- | ---------- |
| `user.js`     |
| POST   | `/signup`             | Creates an account for the user and returns the user's data         | username (str), password (str), firstname (str), lastname (str), email (str)|
| POST   | `/login`              | Login given user cookies and verifies the data aligns w/ the server | username (str), password (str) |
| `tags.js`     |
| POST   | `/insert/tag`         | Insert a custom tag into the database                               | name (str), category (str) |
| GET    | `/tags`               | Returns complete list of tags or optionally specify a category to return tags within that category        | category (str) [optional]|
| `locations.js`     |
| GET   | `/location`            | Fetch a location by its name                                        |  name (str)|
| POST  | `/insert`              | Insert a location into the database                                 |  name (str), tags (array of str), city (str) |
| POST    | `/update`             | Edit a location's city name or insert tags                          |  name (str), tags (array of str), city (str) |
| GET | `/query`                 | Fetch a list of locations through any arbitrary parameters          | any combination of parameters (view sample location body below for available parameters) |
| GET | `/distance` | Find all locations within a certain radius of some coordinates                   | longitude (float), radius (float in miles), latitude (float) |
| GET | `/walking`  | Find all locations within a walkable distance from some coordinates              | longitude (float) , latitude (float), time (float in hours) |
| GET | `/queryAll`  | Find up to 10 locations that best match the given parameters              | longitude (float) , latitude (float), radius (float in miles) time (float in hours), budget ('$' OR '$$' OR '$$$'), tags (array of str), transportation ('Walking' OR 'Bus' OR anything else will have same functionality as /distance)|




### Sample Location Body
```
{
        "_id": "6272329e407e013fb454bbf8",
        "coordinates": {
            "longitude": -118.120988635685,
            "latitude": 34.078585203502
        },
        "hours": [
            {
                "open": [
                    {
                        "is_overnight": false,
                        "start": "1100",
                        "end": "2100",
                        "day": 0
                    },
                    {
                        "is_overnight": false,
                        "start": "1100",
                        "end": "2100",
                        "day": 1
                    },
                    {
                        "is_overnight": false,
                        "start": "1100",
                        "end": "2100",
                        "day": 2
                    },
                    {
                        "is_overnight": false,
                        "start": "1100",
                        "end": "2100",
                        "day": 3
                    },
                    {
                        "is_overnight": false,
                        "start": "1100",
                        "end": "2100",
                        "day": 4
                    },
                    {
                        "is_overnight": false,
                        "start": "1100",
                        "end": "2100",
                        "day": 5
                    }
                ],
                "hours_type": "REGULAR",
                "is_open_now": false
            }
        ],
        "is_closed": false,
        "location": {
            "address1": "138 E Valley Blvd",
            "address2": "",
            "address3": "",
            "city": "Alhambra",
            "zip_code": "91801",
            "country": "US",
            "state": "CA",
            "display_address": [
                "138 E Valley Blvd",
                "Alhambra, CA 91801"
            ]
        },
        "name": "Savoy Kitchen",
        "phone": "+16263089535",
        "photos": [
            "https://s3-media1.fl.yelpcdn.com/bphoto/BZhWr4kEW3KTwNb5wBxL_A/o.jpg",
            "https://s3-media2.fl.yelpcdn.com/bphoto/dkjM6azDkJ6-CXhM1kAqpg/o.jpg",
            "https://s3-media3.fl.yelpcdn.com/bphoto/YVAu5PWWavh4os7EZE0Dyw/o.jpg"
        ],
        "price": "$$",
        "special_hours": null,
        "tags": [
            "Restaurants",
            "Chinese ",
            "Singaporean"
        ]
    }
```
