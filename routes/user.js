const express = require("express");

// locationRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const userRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

// This section will help you get a list of all the users in "user_info".
userRoutes.route("/elainegetsrequed").get(function (_req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("accounts").collection("user_info");

	collection
		.find({})
		.limit(50)
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else {
				res.json(result);
			}
		});
});

// trying different collections "userinfo"
userRoutes.route("/eyo").get(function (_req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("accounts").collection("user_info");

	collection
		.db("accounts")
		.collection("userinfo")
		.find({})
		.limit(50)
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else {
				res.json(result);
			}
		});
});
module.exports = userRoutes;
