const express = require("express");
const app = express();
const PORT = 8080;

const {MongoClient} = require('mongodb');
const uri = "mongodb+srv://superuser:stdatabase@cluster0.r5v7q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
const client = new MongoClient(uri);





app.use(express.json());

//routes
app.get("/user", (req, res) => {
	res.status(200).send({
		name: "Josh",
		password: "bingBong",
	});
});

app.post("/user/:id", (req, res) => {
	const { id } = req.params;
	const { favColor } = req.body;

	if (!favColor) {
		res.status(418).send({ message: "We need a favorite Color!" });
	}

	res.send({
		name: `Bobby with your ${favColor} and ID of ${id}`,
	});
});


app.listen(8080, async () => {
	console.log(`Server is running`);
	
	await client.connect();

	const locations = client.db("sample_locations").collection("locations");

	const loc_name = "Santa Monica Pier";
	const loc_tags = ["Pier", "Beach"];
	const loc_city = "Santa Monica"

	const cursor = locations.find({name: loc_name});
	const loc = cursor.next();

	loc.then((l) => {
		if(l)
		{
			console.log(`Already found location named ${loc_name}`)
			console.log(l);
		}
		else
		{
			console.log(`Inserting ${loc_name}`);
			locations.insertOne({name: loc_name, tags: loc_tags, city: loc_city}, (err, data) => {
				if(err) return console.log(err);
			});
		}
	});
	


  });