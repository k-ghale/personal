import http from 'node:http'

const PORT = 8000

const server = http.createServer((req, res) => {
    res.end("Hello from the Server.")
})

server.listen(PORT, () => console.log("The server is listening on port:8000"))