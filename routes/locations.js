const express = require("express");
const req = require("express/lib/request");

// locationRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const locationRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

//fetch location by name
locationRoutes.route("/location").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");

	collection
		.find({name: req.body.name})
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with name ${req.body.name}`);
			} else {
				res.json(result);
			}
		});
});

//insert location into db
locationRoutes.route("/insert").post(function (req, res) {
	const dbConnect = dbo.getDb();

	const location = {
		name: req.body.name,
		tags: req.body.tags,
		city: req.body.city,
	};

	dbConnect
		.collection('locations')
		.find({name: req.body.name})
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length != 0){
				console.log(`Already found location named ${req.body.name}`)
				console.log(result);
				// res.json(result);
				res.status(400).send('Error inserting matches!');
			} else {
				dbConnect
					.collection("locations").insertOne(location, function (err, result) {
						if (err) {
							res.status(400).send('Error inserting matches!');
						} else {
							console.log(`Added a new match with id ${result.insertedId}`);
							// res.json(result);
							res.json(location);
							res.status(204).send();
						}
					});
			}
		});
		
});

//change city name or insert tag
locationRoutes.route("/update").post(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");

	if (req.body.city.length != 0){
		collection.updateOne( { name: req.body.name },
		{
			$set: { city: req.body.city}
		})
	}

	if (req.body.tags.length != 0){
		collection.updateOne( { name: req.body.name},
			{
				$addToSet: { tags: { $each: req.body.tags}}
			})
	}
	
	console.log(`Updated ${req.body.name}`);
	res.status(204).send();
});

locationRoutes.route("/matchtag").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");

	collection
		.find({tags: {$all: req.body.tags}})
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with tags: ${req.body.tags}`);
			} else {
				res.json(result);
			}
		});
});

// fetch a business from some arbritrary parameter
locationRoutes.route("/query").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("yelp_test");

	const query = req.body;
	console.log(query);

	collection
		.find(query)
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations found`);
			} else {
				res.json(result);
			}
		});
});


//find all locations within a certain radius of a point
locationRoutes.route("/distance").get(function(req, res){
	const dbConnect = dbo.getDb(); 
	const collection = dbConnect.db('businesses').collection('yelp_test');
	collection.createIndex( { coordinates : "2dsphere" } );

	const point = req.body.coordinates;
	const radius_in_miles = req.body.radius; 
	const radius = 1609.34*radius_in_miles;
	
	//trying to set result of query to a list
	const list = collection
		.find(
			{ coordinates:{
				$near:
				{
					$geometry: {type: "Point", coordinates: point},
					$maxDistance: radius
				}
			}}
		).toArray(function (err, result) {
			if (err) {
				console.log(err);
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with specified coordinates and radius`);
			} else {
				res.json(result);
				return result;
			}
		});
	
		//trying to print but i think this is printing before the query finishes executing
		//this is why the .toArray has a callback function so it will execute right after the query is done
		console.log(list)
} );


locationRoutes.route("/walking").get(function(req, res){
	const dbConnect = dbo.getDb(); 
	const collection = dbConnect.db('businesses').collection('yelp_test');
	collection.createIndex( { coordinates : "2dsphere" } );

	const point = req.body.coordinates;
	//const radius_in_miles = req.body.radius; 
	const time = req.body.time * 3600; // hours to seconds
	const walk_speed = 1.5; // average walking speed of 1.5 meters per second
	const radius = time * walk_speed;
	

	collection
		.find(
			{ coordinates:{
				$near:
				{
					$geometry: {type: "Point", coordinates: point},
					$maxDistance: radius
				}
			}}
		).toArray(function (err, result) {
			if (err) {
				console.log(err);
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with specified coordinates and radius`);
			} else {
				res.json(result);
			}
		});
} );

locationRoutes.route("/checkforbus").get(function (req, res) {
    const dbConnect = dbo.getDb();
    const businesses = dbConnect.db('businesses').collection('locations');
    businesses.find({"name": "Savoy Kitchen"}).project({"coordinates": 1}).toArray(function (err, result) {
        if (err) {
            res.status(400).send("Error fetching listings!");
        }
        else{
            console.log(result);
            res.json(result);
        }
    })
});

//this is the function that will calculate a list of places based on a given transportation
function parseTransport(transportation, distance, time, coordinates){
	const dbConnect = dbo.getDb();
    const businesses = dbConnect.db('businesses').collection('locations');
	businesses.createIndex( { coordinates : "2dsphere" } );
	var list;
	const point = coordinates;

	console.log("Parse transport");

	if (transportation == 'Walking'){
		
		//const radius_in_miles = req.body.radius; 
		const new_time = time * 3600; // hours to seconds
		const walk_speed = 1.5; // average walking speed of 1.5 meters per second
		const radius = new_time * walk_speed;
	

		businesses
			.find(
				{ coordinates:{
					$near:
					{
						$geometry: {type: "Point", coordinates: point},
						$maxDistance: radius
					}}
				}
			).toArray(function (err, result) {
				if (err) {
					console.log(err);
					console.log("Error fetching listings!");
				} else if (result.length == 0) {
					console.log(`No locations with specified coordinates and radius`);
				} else {
					list = result;
				}
			});
	} else if (transportation == 'Bus') {
		// insert elaine's bus function here
	} else {
		const radius_in_miles = distance; 
		const radius = 1609.34*radius_in_miles;


		list = businesses
			.find(
				{ coordinates:{
					$near:
					{
						$geometry: {type: "Point", coordinates: point},
						$maxDistance: radius
					}
				}}
			).toArray(function (err, result) {
				if (err) {
					console.log(err);
					console.log("Error fetching listings!");
				} else if (result.length == 0) {
					console.log(`No locations with specified coordinates and radius`);
					console.log(result);
				} else {
					console.log("success");
					console.log(result);
				}
			});

			console.log(list);
	}

	// console.log(typeof list);
	// console.log(list);

}

locationRoutes.route("/queryAll").get(function (req, res) {
    const dbConnect = dbo.getDb();
    const businesses = dbConnect.db('businesses').collection('locations');

	parseTransport(req.body.transportation, req.body.distance, req.body.time, req.body.coordinates);
   


});

module.exports = locationRoutes;