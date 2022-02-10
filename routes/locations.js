const express = require("express");

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const locationRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

// This section will help you get a list of all the locations.
locationRoutes.route("/location").get(async function (_req, res) {
	const dbConnect = dbo.getDb();

	dbConnect
		.collection("locations")
		.find({})
		.limit(50)
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else {
				res.json(result);
			}
		});


        
	// // await client.connect();

	// const locations_collection = client
	// 	.db("sample_locations")
	// 	.collection("locations");
	// const loc_name = "The Getty";
	// const loc_tags = ["Museum", "Art"];
	// const loc_city = "Santa Monica";

	// const cursor = locations_collection.find({ name: loc_name });

	// const loc = cursor.next();

	// loc.then((l) => {
	// 	if (l) {
	// 		console.log(`Already found location named ${loc_name}`);
	// 		console.log(l);
	// 	} else {
	// 		console.log(`Inserting ${loc_name}`);
	// 		locations_collection.insertOne(
	// 			{ name: loc_name, tags: loc_tags, city: loc_city },
	// 			(err, data) => {
	// 				if (err) return console.log(err);
	// 			}
	// 		);
	// 	}
	// });



});

module.exports = locationRoutes;