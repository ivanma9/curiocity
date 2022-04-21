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
locationRoutes.route("insert").post(function (req, res) {
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

locationRoutes.route("/distance").get(function(req, res){
	const dbConnect = dbo.getDb(); 
	const collection = dbConnect.db('businesses').collection('yelp_test');
	collection.createIndex( { coordinates : "2dsphere" } );

	const point = req.body.coordinates;
	const radius_in_miles = req.body.radius; 
	const radius = 1609.34*radius_in_miles;

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

module.exports = locationRoutes;