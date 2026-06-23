import http from 'node:http'

const PORT = 8000

const server = http.createServer((req, res) => {

    const url = req.url
    if (url == "/api" && req.method == 'GET'){
        res.end("Hello from the Server.", 'utf8', () => console.log('response ended'))
    }
})

server.listen(PORT, () => console.log("The server is listening on port:8000"))