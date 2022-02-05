const app = require('express')();
const PORT = 8080;
app.listen(
  PORT,
  () => console.log("it's alive")
)

app.get('/tshirt', (req,res) => {

})
