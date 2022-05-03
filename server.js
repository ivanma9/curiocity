require("dotenv").config();
console.log(process.env);

const express = require("express");
const app = express();
const PORT = process.env.PORT || 8080;
const db = require("./db/mongoConn");

app.use(express.json());
app.use(require("./routes/locations"));
app.use(require("./routes/user"));
app.use(require("./routes/tags"));
app.use(require("./routes/yelp"));

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

db.connectToServer( (err) => {
	app.listen(PORT, async () => {
		console.log(`Server is running on ${PORT}`);
	});

});
