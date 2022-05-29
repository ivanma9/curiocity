//import bus_stops_json from bus.py
const express = require("express");
const req = require("express/lib/request");
const res = require("express/lib/response");

// locationRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const locationRoutes = express.Router();

// This will help us connect to the database
const dbo = require("../db/mongoConn");

//fetch location by name
locationRoutes.route("/location").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");

	collection
		.find({name: req.query.name})
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with name ${req.query.name}`);
			} else {
				res.json(result);
			}
		});
});

//insert location into db
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

//change city name or insert tag
locationRoutes.route("/update").post(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");

	if (req.body.city.length != 0){
		collection.updateOne( { name: req.body.name },
		{
			$set: { city: req.body.city}
		})
	}

	if (req.body.tags.length != 0){
		collection.updateOne( { name: req.body.name},
			{
				$addToSet: { tags: { $each: req.body.tags}}
			})
	}
	
	console.log(`Updated ${req.body.name}`);
	res.status(204).send();
});

locationRoutes.route("/matchtag").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("locations");

	collection
		.find({tags: {$all: req.query.tags}})
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with tags: ${req.query.tags}`);
			} else {
				res.json(result);
			}
		});
});

// fetch a business from some arbritrary parameter
locationRoutes.route("/query").get(function (req, res) {
	const dbConnect = dbo.getDb();
	const collection = dbConnect.db("businesses").collection("yelp_test");

	const query = req.query;
	console.log(query);

	collection
		.find(query)
		.toArray(function (err, result) {
			if (err) {
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations found`);
			} else {
				res.json(result);
			}
		});
});


//find all locations within a certain radius of a point
locationRoutes.route("/distance").get(function(req, res){
	const dbConnect = dbo.getDb(); 
	const collection = dbConnect.db('businesses').collection('locations');

	const long = parseFloat(req.query.longitude);
	const lat = parseFloat(req.query.latitude);  
	const radius_in_miles = parseFloat(req.query.radius);
	const radius = 1609.34*radius_in_miles;

	const url = s`Hey name is ${req.query.name}`;
	useState({})	
	 collection
		.find(
			{ coordinates:{
				$near:
				{
					$geometry: {type: "Point", coordinates: [long, lat]},
					$maxDistance: radius
				}
			}}
		).toArray(function (err, result) {
			if (err) {
				console.log(err);
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with specified coordinates and radius`);
			} else {
				res.json(result);
				 console.log(result);
			}
		});



} );


locationRoutes.route("/walking").get(function(req, res){
	const dbConnect = dbo.getDb(); 
	const collection = dbConnect.db('businesses').collection('locations');

	const long = parseFloat(req.query.longitude);
	const lat = parseFloat(req.query.latitude); 
	//const radius_in_miles = req.query.radius; 
	const time = parseFloat(req.query.time) * 3600; // hours to seconds
	const walk_speed = 1.5; // average walking speed of 1.5 meters per second
	const radius = time * walk_speed;
	
	
	 collection
		.find(
			{ coordinates:{
				$near:
				{
					$geometry: {type: "Point", coordinates: [long, lat]},
					$maxDistance: radius
				}
			}}
		).toArray(function (err, result) {
			if (err) {
				console.log(err);
				res.status(400).send("Error fetching listings!");
			} else if (result.length == 0) {
				res.status(400).send(`No locations with specified coordinates and radius`);
			} else {
				res.json(result);
				 console.log(result);
			}
		});
} );

//compare locations by thier names
function logical_and(list1, list2){
	var combined_list = [];
	for(var i =0 ; i<list1.length; ++i){
		for(var j =0; j<list2.length; ++j){
			if(list1[i].name==list2[j].name){
				combined_list.push(list1[i]);
			}
		}
	}
	return combined_list; 
}

// 
function combine_unique_masterList_and_newList(masterList, newList) {
	return masterList
		.filter((value) => !newList.includes(value))
		.concat(newList);
}


//may be void
function clean_list(list){

	let uniqueNames = [];
	let uniqueList = [];
	list.forEach((c) => {
		if (!uniqueNames.includes(c.name)) {
			uniqueNames.push(c.name)
			uniqueList.push(c);
		}
	});

	return uniqueList;

}

//insert bus stop locations into db
locationRoutes.route("/insertbus").post(function (req, res) {
	const dbConnect = dbo.getDb();
	const busstops = dbConnect.db("transportation").collection("bus_stops");
	console.log("hello")
	console.log(busjsonstr);
	var busjson = JSON.parse(busjsonstr);
	for(i = 0; i < busjson.length; i++)
	{
		//console.log(busjson[i]);
		//console.log('\n');
		try{
			busstops.insertOne(busjson[i]);
			console.log("yay");
		} catch (e) {
			print(e);
		}
	}
	busstops.insertOne({type: req.body.type,
		coordinates: req.body.coordinates});
	res.json("bus stop inserted");

});

locationRoutes.route("/checkforbus").get(function (req, res) {
    const buscoorarr = new Promise((resolve, reject) => {
    const dbConnect = dbo.getDb();
    const businesses = dbConnect.db('businesses').collection('locations');
    businesses.find({})
        .project({"coordinates": 1,"_id": 0})
        .toArray(
            function (err, result) {
            if (err) {
                //res.status(400).send("Error fetching listings!");
                reject('Promise is rejected'); 
            }
            else{
                //res.json(result);
                resolve(result);
            }
        }
    );
    })
    buscoorarr.then((message) => {
        //console.log(message);
        const dbConnect = dbo.getDb();
        const buscollection = dbConnect.db('transportation').collection('bus_stops');
        buscollection.createIndex( { coordinates : "2dsphere" } );
        
        const radius = 1609.32 * 0.25; //a close bus stop is defined as within 0.1 miles radius 

        for(var i = 0; i < message.length; i++)
        {
            const long = parseFloat(message[i]['coordinates']['longitude']);
            //console.log(long);
            const lat = parseFloat(message[i]['coordinates']['latitude']);
            //console.log(lat);

            buscollection
            .find(
             { coordinates:{
                 $near:
                 {
                     $geometry: {type: "Point", coordinates: [long, lat]},
                     $maxDistance: radius
                 }
             }}
            ).toArray(function (err, result) {
             if (err) {
                 console.log(err);
                 res.status(400).send("Error fetching listings!");
             } else if (result.length == 0) {
				 console.log("No bus stop near this business");
             } else {
                 console.log("Bus stop(s) found within 0.25 radius of business");
             }
            });
        }
    }).catch((message) => {
        console.log(message);
    });



});



//this is the function that will calculate a list of places based on a given transportation
function parseTransport(transportation, distance, time, latitude, longitude){
	 return new Promise((resolve, reject) =>{
		const dbConnect = dbo.getDb();
		const businesses = dbConnect.db('businesses').collection('locations');
		const long = parseFloat(longitude);
		const lat = parseFloat(latitude); 
	
		console.log("Parse transport");
	
		if (transportation == 'Walking'){
			
			//const radius_in_miles = req.query.radius; 
			const new_time = parseFloat(time) * 3600; // hours to seconds
			const walk_speed = 1.5; // average walking speed of 1.5 meters per second
			const radius = new_time * walk_speed;
		
	
			  businesses
				.find(
					{ coordinates:{
						$near:
						{
							$geometry: {type: "Point", coordinates: [long, lat]},
							$maxDistance: radius
						}}
					}
				).toArray(function (err, result) {
					if (err) {
						console.log(err);
						console.log("Error fetching listings!");
						reject(new Error('Error')); 
					} else if (result.length == 0) {
						console.log(`No locations with specified coordinates and radius`);
						resolve(result); 
					} else {
						console.log('success');
						resolve(result);
					}
				});
		} else if (transportation == 'Bus') {
			// insert elaine's bus function here
		} else {
			const radius_in_miles = parseFloat(distance); 
			const radius = 1609.34*radius_in_miles;
			
				businesses
				.find(
					{ coordinates:{
						$near:
						{
							$geometry: {type: "Point", coordinates: [long, lat]},
							$maxDistance: radius
						}
					}}
				).toArray(function (err, result) {
					if (err) {
						console.log(err);
						console.log("Error fetching listings!");
						reject(new Error('Error')); 
					} else if (result.length == 0) {
						console.log(`No locations with specified coordinates and radius`);
						resolve(result);
					} else {
						resolve(result);
						console.log('success transport');
					}
				});
			 }
		})
	 }
	
function parseBudget(budget, distance, latitude, longitude){
	return new Promise((resolve, reject) =>{
		const dbConnect = dbo.getDb();
		const businesses = dbConnect.db('businesses').collection('locations');
		const long = parseFloat(longitude);
		const lat = parseFloat(latitude); 
		const radius_miles = parseFloat(distance);
		const radius = radius_miles*1609; 
		console.log(budget); 
		businesses
		.find(
			
			{ coordinates:{
				$near:
				{
					$geometry: {type: "Point", coordinates: [long, lat]},
					$maxDistance: radius
				}
			},
			price:budget}
		).toArray(function (err, result) {
			if (err) {
				console.log(err);
				console.log("Error fetching listings!");
				reject(new Error('Error')); 
			} else if (result.length == 0) {
				console.log(`No locations with specified coordinates and radius`);
				resolve(result);
			} else {
				resolve(result);
				console.log('success budget');
			}
		});
	})
}

function parseTags(tags, distance, latitude, longitude){
	return new Promise((resolve, reject) =>{

		const dbConnect = dbo.getDb();
		const businesses = dbConnect.db('businesses').collection('locations');
		const long = parseFloat(longitude);
		const lat = parseFloat(latitude); 
		const radius_miles = parseFloat(distance);
		const radius = radius_miles*1609; 

		businesses
		.find(
			{ coordinates:{
				$near:
				{
					$geometry: {type: "Point", coordinates: [long, lat]},
					$maxDistance: radius
				}
			},
			tags: {$all: tags}}
		).toArray(function (err, result) {
			if (err) {
				console.log(err);
				console.log("Error fetching listings!");
				reject(new Error('Error')); 
			} else if (result.length == 0) {
				console.log(`No locations with specified coordinates and radius`);
				resolve(result);
			} else {
				resolve(result);
				console.log('success tags');
			}
		});
	})
}

locationRoutes.route("/queryAll").get(async function (req, res) {

	const transport_list = clean_list(await parseTransport(req.query.transportation, req.query.radius, req.query.time, req.query.latitude, req.query.longitude)
	.catch(err=>{
		res.status(400).send("Error when querying transport");
	})
	)
	const budget_list = clean_list(await parseBudget(req.query.budget, req.query.radius, req.query.latitude, req.query.longitude)
	.catch(err=>{
		res.status(400).send("Error when querying budget");
	})
	);
	const tags_list = clean_list(await parseTags(req.query.tags, req.query.radius, req.query.latitude, req.query.longitude)
	.catch(err=>{
		res.status(400).send("Error when querying tags");
	})
	);

	//FILTER THREE PREFERENCES
	var master_list = clean_list(logical_and(logical_and(transport_list, budget_list), tags_list));

	//FILTER TWO PREFERENCES
	const transport_budget_list = clean_list(logical_and(transport_list, budget_list));
	master_list = clean_list(master_list.concat(transport_budget_list));

	const transport_tags_list = clean_list(logical_and(transport_list, tags_list));
	master_list = clean_list(master_list.concat(transport_tags_list));

	const budget_tags_list = clean_list(logical_and(budget_list, tags_list));
	master_list = clean_list(master_list.concat(budget_tags_list));
	
	//FILTER ONE PREFERENCE
	master_list = clean_list(master_list.concat(transport_list));
	master_list = clean_list(master_list.concat(tags_list));
	master_list = clean_list(master_list.concat(budget_list));

 	console.log(master_list.slice(0,10));

	if(master_list.length != 0){
		res.send(master_list.slice(0,10));
	}
	else{
		res.status(404).send("Could not find matches");
	}
});


module.exports = locationRoutes;