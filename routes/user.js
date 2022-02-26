const express = require("express");
// const req = require("express/lib/request");


// userRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const userRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

// This section will help you get a list of all the users in "user_info".
userRoutes.route("/elainegetsrequed").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("accounts").collection("user_info");

	collection
		.find({})
		// .limit(50)
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else {
				res.json(result);
			}
		});
});

userRoutes.route("/test").post(function (req, res) {
	const dbConnect = dbo.getDb();
	
	const users = dbConnect.db("accounts").collection("user_info");
	
	users.insertOne({username: req.body.username,
					password: req.body.password,
					email: req.body.email,
					firstname: req.body.firstname,
					lastname: req.body.lastname });
	res.json("just inserted something");

});

userRoutes.route("/signup").post(function (req, res) {
	const dbConnect = dbo.getDb();
	
	const users = dbConnect.db("accounts").collection("user_info");
	const cursor = users.find({username: req.body.username});
	const user = cursor.next();
	user.then((u) => {
		if(u)
		{
			console.log(u);
			

			res.json("sign up failed");
		}
		else
		{
			users.insertOne({username: req.body.username,
				password: req.body.password,
				email: req.body.email,
				firstname: req.body.firstname,
				lastname: req.body.lastname}, (err, data) => {
				if(err) return console.log(err);
			})

			res.json("sign up successfully!");
		}
	});
});

userRoutes.route("/login").post(function (req, res) {
	const dbConnect = dbo.getDb();
	
	const users = dbConnect.db("accounts").collection("user_info");
	const cursor = users.find({username: req.body.username});
	const user = cursor.next();

	user.then((u) => {
		if(u)
		{
			if(req.body.password == u.password)
			{

				res.json("authorized login");
			}
			else
			{

				res.json("unauthorized login");
			}
		}
		else
		{

			res.json("need to register account");
		}
	});
});




module.exports = userRoutes;
