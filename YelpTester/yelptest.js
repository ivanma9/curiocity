import axios from 'axios';
import { readFile } from 'fs/promises';
import fetch from 'node-fetch';
const credJson = JSON.parse(
  await readFile(
    new URL(
        './credentials.json', 
        import.meta.url
      )
  )
);
const API_KEY = credJson["API_KEY"];
console.log(API_KEY);

const Url = "https://api.yelp.com/v3/businesses/search";
const paramsy = "?term=food&limit=50&offset=50&radius=10000&location=San+Diego";
const PARAMETERS = {
	term: "food",
	limit: 50,
	offset: 50,
	radius: 10000,
	location: "San Diego",
};
fetch(Url, {
	method: "GET",
	headers: { Authorization: "Bearer " + API_KEY },
  
})
	.then((res) => res.json())
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

