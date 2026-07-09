import http, { get } from 'node:http'
import { getDataFromDB } from './database/db.js'
import { error } from 'node:console'
import { data } from './data.js'

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
    else if(req.url.startsWith('/api/continent/') && req.method === 'GET'){
        const continent = req.url.split('/').pop()
        const filterData = destinations.filter((destinations) => {
            return destinations.continent.toLowerCase() === continent.toLowerCase()
        }) 
        res.setHeader('Content-Type', 'application/json')
        res.statusCode=200
        res.send(JSON.stringify(filterData))
    } 
    else {
        res.setHeader('Content-Type', 'application/json')
        res.statusCode=404
        res.end(JSON.stringify({error:"not found", message: "The requested route does not exist."}))
    }
}
)

server.listen(PORT, () => console.log(`Connected on port: ${PORT}`))