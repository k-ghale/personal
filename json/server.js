import http, { get } from 'node:http'
import { getDataFromDB } from './database/db.js'

const PORT = 8000

 
const server = http.createServer((req, res) => {
    // if (req.url === '/api' && req.method === 'GET'){
    //     res.end('This is from the server')
    // }
    const destinations = await getDataFromDB()
    if (req.url === '/api' && req.method === 'GET'){

        res.setHeader('Content-Type', 'application/json')
        res.statusCode=200
        res.end(JSON.stringify(destinations))
    }
}
)

server.listen(PORT, () => console.log(`Connected on port: ${PORT}`))