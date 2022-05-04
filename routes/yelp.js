const express = require("express");

// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const yelpRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

//API KEY for yelp account
const yelp_API_KEY = process.env.YELP_API_KEY;

// This section will help you get a list of all the locations.
yelpRoutes.route("/business").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("business");

	collection.find({}).toArray(function (err, result) {
		if (err) {
			res.status(400).send("Error fetching listings!");
		} else {
			res.json(result);
		}
	});
});

// Adds yelp data businesses
yelpRoutes.route("/insertbusinesses").post(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");
	const resFromScraper = req.body['res'];
	var business_count = resFromScraper.length;

	for(var i =0; i<business_count; ++i){
		let business = resFromScraper[i];
        console.log(business)
		collection.updateOne(business, {$set : business}, {upsert:true})
		.then(() =>{
			console.log('inserted succesfully')
			res.status(200).send();
		})
		.catch((err) => {
            console.log(err)
            console.log("UNSUCCESSFUL")
			res.status(400).send();
		})
	}



    

	// for (let cityBusinesses in resFromScraper) {
    //     console.log(cityBusinesses);
	// 	collection
	// 		.insertMany(cityBusinesses["businesses"])
	// 		.then(() => {
    //             res.json("inserted successfully");
    //             res.status(200).send();
    //         })
	// 		.err((err) => {
    //             res.json("unsucessful");
    //             res.status(400).send();
    //         });
	// }
});

module.exports = yelpRoutes;
