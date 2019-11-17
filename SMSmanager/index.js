const express = require('express')
const app = express();
var request = require('request');
var bodyParser = require("body-parser");
var session_url = 'https://api.46elks.com/a1/SMS';
const dotenv = require('dotenv');
dotenv.config();

var uname = process.env.UNAME
var pass = process.env.PASS
var sender = "Stara";

app.set('views', __dirname + '/public');
app.engine('html', require('ejs').renderFile);
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.render('index.html')
});

app.listen(4000, () => {
  console.log('App listening on port 4000!')
});

app.get('/msg', (req, res) => {
    res.render('msg.html')
  });
  app.get('/spam', (req, res) => {
    res.render('spam.html')
  });

app.post('/submit', function (req, res) {
    var name = req.body.msg+ ' ' + req.body.nmbr;
    console.log(name)
    let message = sendSMS(req.body.nmbr, req.body.msg);
    res.send({ status: message });
});

function sendSMS(target_sms, message_sms) {
    request.post(session_url, {
        auth: {
          username: uname,
          password: pass
        },
        form: {
          from : sender, 
          to : target_sms, 
          message : message_sms, 
        }
      }, function(err, res, body) {
        if (res.statusCode == 200) {
          console.log("Sent! The API responded:")
          console.log(JSON.parse(body))
          return "Success"
        } else {
          console.log("Error:")
          console.log(body)
          return "Failure"
        }
      })
};

  