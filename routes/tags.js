const { query } = require('express');
const express = require('express');

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const tagRoutes = express.Router();

// This will help us connect to the database
const dbo = require('/db/mongoConn');

// This section will help you get a list of all the records.
tagRoutes.route('/businesses').get(async function (_req, res) {
  const dbConnect = dbo.getDb();
  query = _req.params;

  if(query){
    dbConnect
    .collection('tags')
    .find({query})
    .limit(10)
    .toArray(function (err, result) {
      if (err) {
        res.status(400).send('Error fetching tags!');
      } else {
        res.json(result);
      }
    });
  }
  else{
    dbConnect
    .collection('tags')
    .find({})
    .limit(50)
    .toArray(function (err, result) {
      if (err) {
        res.status(400).send('Error fetching tags!');
      } else {
        res.json(result);
      }
    });
  }
  
});
