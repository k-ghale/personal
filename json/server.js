import http, { get } from 'node:http'
import { getDataFromDB } from './database/db.js'
import { error } from 'node:console'
import { data } from './data.js'
import { sendJSONresponse } from './util/sendJSONresponse.js'

const PORT = 8000

 
const server = http.createServer((req, res) => {
    // if (req.url === '/api' && req.method === 'GET'){
    //     res.end('This is from the server')
    // }
    const destinations = await getDataFromDB()
    if (req.url === '/api' && req.method === 'GET'){
        sendJSONresponse(res, 200, destinations)
    }
    else if(req.url.startsWith('/api/continent/') && req.method === 'GET'){
        const continent = req.url.split('/').pop()
        const filterData = destinations.filter((destinations) => {
            return destinations.continent.toLowerCase() === continent.toLowerCase()
        })
        sendJSONresponse(res, 200, filterData) 
    } 
    else {
        res.setHeader('Content-Type', 'application/json')
        res.statusCode=404
        res.end(JSON.stringify({error:"not found", message: "The requested route does not exist."}))
    }
}
)

server.listen(PORT, () => console.log(`Connected on port: ${PORT}`))