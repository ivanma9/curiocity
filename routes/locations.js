const express = require("express");
const req = require("express/lib/request");

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const locationRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

// This section will help you get a list of all the locations.
locationRoutes.route("/location").get(function (req, res) {
	const dbConnect = dbo.getDb();

	dbConnect
		.collection("locations")
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

module.exports = locationRoutes;