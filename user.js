const {MongoClient} = require('mongodb');
require('dotenv').config();


async function main(){
    const uri = process.env.MONGODB_URI;
    const client = new MongoClient(uri);

    try{
        await client.connect();
 
        // await findOneUserByName(client, "Elaine Lin"); 

        // await createMultipleUsers(client, [
        //     {
        //         name: "Elaine Lin",
        //         username: "elainelin",
        //         password: "1234"
        //     },
        //     {
        //         name: "Tom Holland",
        //         username: "tomholland2013",
        //         password: "iloveelaine"
        //     }
        // ]
        //     )

        await createUser(client, {
            name: "Guy",
            username: "myuser",
            password: "mypassword",
        })

        //await listDatabases(client);
    } catch(e)
    {
        console.error(e);
    } finally{
        await client.close();
    }

}

main().catch(console.error); 

async function createUser(client, newUserInfo){
    let id;
    const result = await client.db("accounts").collection("user_info").insertOne(newUserInfo);
    id = result.insertedId;
    console.log(`New Users created with the following id:` + id);
}

async function createMultipleUsers(client, newUserInfo){
    const result = await client.db("accounts").collection("user_info").insertMany(newUserInfo);
    console.log(`${result.insertedCount} new users created with the following id(s):`);
    console.log(result.insertedIds);
}

async function findOneUserByName(client, nameOfUser) {
    const result = await client.db("accounts").collection("user_info").findOne({name: nameOfUser});
    if(result){
        console.log(`Found a user in the collection with the name '${nameOfUser}'`);
        console.log(result);
    }
    else{
        console.log(`No listings found with the name '${nameOfUser}'`);
    }
}


async function listDatabases(client){
    const databasesList = await client.db().admin().listDatabases();

    console.log("Databases:");
    databasesList.databases.forEach(db => {
        console.log(`- ${db.name}`);
    })
}