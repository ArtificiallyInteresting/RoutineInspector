const http = require('http');
const express = require('express')
const app = express()


const hostname = '127.0.0.1';
const port = 3001;

// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello World');
// });

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

app.get('/routine', (req, res) => {
    console.log(req);
    res.send('Hello World!')
  })
