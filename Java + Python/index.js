const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000

app.get('/', (req, res) => {
 // spawn new child process to call the python script
 const python = spawn('python', ['script.py','node.js','python']);
 res.send('hello')
 });
 
app.listen(port, () => console.log(`Example app listening on port ${port}!`))