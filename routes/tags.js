const { query } = require('express');
const express = require('express');

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const tagRoutes = express.Router();

// This will help us connect to the database
const dbo = require('../db/mongoConn');

// This section will help you get a list of all the records.
tagRoutes.route('/tags').get(async function (_req, res) {
  const dbConnect = dbo.getDb();
  const collection = dbConnect.db('businesses').collection('tags')

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
  
});


tagRoutes.route('/insert').post(function (req, res) {
  const dbConnect = dbo.getDb();
  const tag = {
    name: req.body.name,
    category: req.body.category
  };

  dbConnect
    .collection('tags')
    .insertOne(tag, function (err, result) {
      if (err) {
        res.status(400).send('Error inserting tag!');
      } else {
        console.log(`Added a new tag with id ${result.insertedId}`);
        res.status(204).send();
        res.json(tag);
      }
    });
});


tagRoutes.route('/tag/update/:id').put((req, res, next) =>{//update/edit a tag by ID
  const dbConnect = dbo.getDb();
  let id = {
    _id: ObjectId(req.params.id)
  };
  if(req.body.category.length != 0 && req.body.name.length != 0){
    dbConnect.collection("tags").update({_id: id}, {$set:{'category': req.body.category, 'name': req.body.name}}, (err, result) => {
      if(err) {
        throw err;
      }
      res.send('tag updated sucessfully');
    });
  }
  else if(req.body.category.length != 0){
    dbConnect.collection("tags").update({_id: id}, {$set:{'category': req.body.category}}, (err, result) => {
      if(err) {
        throw err;
      }
      res.send('tag category updated sucessfully');
  })
}
else if(req.body.name.length != 0){
  dbConnect.collection("tags").update({_id: id}, {$set:{'name': req.body.name}}, (err, result) => {
    if(err) {
      throw err;
    }
    res.send('tag name updated sucessfully');
}
)}
else{
  res.status(400).send("We need a tag or category to update!");
}
});

module.exports = tagRoutes;
