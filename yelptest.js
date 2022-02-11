//const axios = require('axios');

const fetch = require('isomorphic-fetch')
require('dotenv').config();

const yelp_API_KEY = process.env.YELP_API_KEY;
console.log(yelp_API_KEY);

const Url = "https://api.yelp.com/v3/businesses/search";
const paramsy = "?term=food&limit=50&offset=50&radius=10000&location=San+Diego";
const endpoint = Url + paramsy;
const PARAMETERS = {
	term: "food",
	limit: 50,
	offset: 50,
	radius: 10000,
	location: "San Diego",
};

fetch(endpoint, {
	method: "GET",
	headers: { 
		Authorization: "Bearer " + yelp_API_KEY, 
		'Content-Type': 'application/json',
		body : JSON.stringify(PARAMETERS)
	
	}
})
	.then((res) => {
		// console.log(res);
		return res.json();
		//throw new Error("could not access the data");
	})
	.then((json) => console.log(json))
	.catch((err) => console.error(err));
// const instance = axios.create({
//   baseURL: Url,
// 	headers: { Authorization: "Bearer " + API_KEY },

// });

// axios.get(Url, instance 	)
// 	.then((res) => res.json())
//   .then((json) => console.log(json))
// 	.catch((err) => console.log(err));
