//1. Call mysql package
const mysql = require('mysql');
//2. Call express package
const express = require('express');
//3. Call body-parser package
const bodyparser = require('body-parser');
//4. Crear a new express app instancevar 
var app = express();
//5. Call JSON request
app.use(bodyparser.json());


//6. Create mysql database connection
var mysqlConnection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'market'
});

//7. Validate mysql database conecction
mysqlConnection.connect((err) => {
    if(!err)
        console.log('Succesfull data base connection ');
    else
        console.log('Connection failed' + JSON.stringify(err,undefined,2))
});

//8. run server
app.listen(3000, ()=>console.log(':::Express server is running at port: 3000:::'));

//9. Read all users in data base
app.get('/list_users',(req,res) => {
    mysqlConnection.query('SELECT * FROM users',(err, rows, fields)=>{
        if(!err){
            console.log(rows);
            res.send(rows);
        }else{
            console.log(err);
        }
    })
});
