const express = require('express');
const req = require("express/lib/request");

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const tagRoutes = express.Router();

// This will help us connect to the database
const dbo = require('../db/mongoConn');

// This section will help you get a list of all the records.
tagRoutes.route('/tags').get(async function (req, res) {
  const dbConnect = dbo.getDb();
  const collection = dbConnect.db('businesses').collection('tags')
  const category = req.body.category;

  if(category){
    collection
    .find({category:category})
    .limit(50)
    .toArray(function (err, result) {
      if (err) {
        res.status(400).send('Error fetching tags!');
      } else {
        res.json(result);
      }
  })
  }
  else{
    collection
    .find({})
    .limit(50)
    .toArray(function (err, result) {
      if (err) {
        res.status(400).send('Error fetching tags!');
      } else {
        res.json(result);
      }
  })
}
   
  
});


tagRoutes.route('/insert/tag').post(function (req, res) {
  const dbConnect = dbo.getDb();
  const collection = dbConnect.db('businesses').collection('tags')
  const tag = {
    name: req.body.name,
    category: req.body.category
  };

  collection
    .insertOne(tag, function (err, result) {
      if (err) {
        res.status(400).send('Error inserting tag!');
      } else {
        console.log(`Added a new tag with id ${result.insertedId}`);
        res.status(204).send(`Added a tag with name: ${req.body.name} and category ${req.body.category} `);
        res.json(tag);
      }
    });
});


module.exports = tagRoutes;
