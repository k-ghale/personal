
import http from 'node:http'

const server = http.createServer((req, res) => {

    const url_object = new URL(req.url, `http://${req.headers.host}`)
    const query_object = Object.fromEntries(url_object.searchParams)

    console.log(query_object);

})

server.listen(8000, () => console.log("Server listenning on port:8000"))