require('dotenv').config();
// console.log("process.env");

const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const app = express();
const PORT = 8080;

const {MongoClient} = require('mongodb');
const uri = `mongodb+srv://${process.env.DB_USER}:${process.env.DB_PWORD}@cluster0.r5v7q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;
const client = new MongoClient(uri);

app.use(express.json());
app.use(cors());

const Account = require("./model/account.js");
let currAcct;

const db = mongoose.connection;
db.on("error", (error) => console.log(error));
db.once("open", () => console.log("connected to database"));

app.get("/", async (req, res) => {
    try {
      const accounts = await Account.find();
      res.json(accounts);
    } catch (error) {
      console.log(error);
    }
  });

app.post("/register", async (req, res) => {
    try {
        Account.find({username: req.body.username}, async(err, accs) => {
            console.log(accs);
            console.log(accs.length);
            if(accs.length != 0)
            {
                accExists = true;
                res.json("User already exists!");
            }
            else
            {
                const accountToSave = await new Account(req.body);
                await accountToSave.save(accountToSave);
                let infoToReturn = await Account.find({
                    username: req.body.username,
                });
                if(infoToReturn.length != 0){
                    res.json("User Registered Successfully");
                }
                else{
                    res.json("Something went wrong...");
                }
            }
        });
    }
    catch (error){
        console.log(error);
    }
});

app.post("/login", async (req, res) => {
    const {username, password } = req.body;
    try {
        const account = await Account.findOne({
            username: username,
        });
        if(!account) {
            res.json("No such User");
        }
        else if(account.password === password)
        {
            currAcct = account;
            res.json(account);
        }
        else{
            res.json("Wrong username or password");
        }
    }
    catch (error){
        console.log(error);
    }
});


app.listen(8080, () => console.log("Listening at localhost:8080"));

// app.listen(process.env.PORT || PORT, async () => {
// 	console.log(`Server is running`);

// 	await client.connect();

// 	const myusers = client.db("accounts").collection("userinfo");
// 	const user_name = "user1111111";
// 	const user_password = "password!";

// 	const cursor = myusers.find({ username: user_name });

// 	const user = cursor.next();

// 	user.then((u) => {
// 		if (u) {
// 			console.log(`Already found username ${user_name}`);
// 			console.log(u);
// 		} else {
// 			console.log(`Inserting ${user_name}`);
// 			myusers.insertOne(
// 				{ 
//                     username: user_name,
//                     password: user_password 
//                 },
// 				(err, data) => {
// 					if (err) return console.log(err);
// 				}
// 			);
// 		}
// 	});
// });



// async function main(){
//     // const uri = process.env.MONGODB_URI;
//     const uri = `mongodb+srv://${process.env.DB_USER}:${process.env.DB_PWORD}@cluster0.r5v7q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;
//     const client = new MongoClient(uri);

//     try{
//         await client.connect();
 
//         // await findOneUserByName(client, "Elaine Lin"); 

//         // await createMultipleUsers(client, [
//         //     {
//         //         name: "Elaine Lin",
//         //         username: "elainelin",
//         //         password: "1234"
//         //     },
//         //     {
//         //         name: "Tom Holland",
//         //         username: "tomholland2013",
//         //         password: "iloveelaine"
//         //     }
//         // ]
//         //     )

//         await createUser(client, {
//             name: "Guy2",
//             username: "myuser2",
//             password: "mypassword2",
//         })

//         //await listDatabases(client);
//     } catch(e)
//     {
//         console.error(e);
//     } finally{
//         await client.close();
//     }

// }

// main().catch(console.error); 

// async function createUser(client, newUserInfo){
//     let id;
//     const result = await client.db("accounts").collection("user_info").insertOne(newUserInfo);
//     id = result.insertedId;
//     console.log(`New Users created with the following id:` + id);
// }

// async function createMultipleUsers(client, newUserInfo){
//     const result = await client.db("accounts").collection("user_info").insertMany(newUserInfo);
//     console.log(`${result.insertedCount} new users created with the following id(s):`);
//     console.log(result.insertedIds);
// }

// async function findOneUserByName(client, nameOfUser) {
//     const result = await client.db("accounts").collection("user_info").findOne({name: nameOfUser});
//     if(result){
//         console.log(`Found a user in the collection with the name '${nameOfUser}'`);
//         console.log(result);
//     }
//     else{
//         console.log(`No listings found with the name '${nameOfUser}'`);
//     }
// }


// async function listDatabases(client){
//     const databasesList = await client.db().admin().listDatabases();

//     console.log("Databases:");
//     databasesList.databases.forEach(db => {
//         console.log(`- ${db.name}`);
//     })
// }