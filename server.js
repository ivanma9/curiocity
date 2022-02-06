const express = require("express");
const app = express();
const PORT = 8080;
app.listen(process.env.PORT || PORT, () => console.log("it's alive"));

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
