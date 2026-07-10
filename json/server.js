import http, { get } from 'node:http'
import { getDataFromDB } from './database/db.js'
import { error } from 'node:console'
import { data } from './data.js'
import { sendJSONresponse } from './util/sendJSONresponse.js'
import { sendFilterData } from './util/sendFilterData.js'

const PORT = 8000

 
const server = http.createServer((req, res) => {
    const destinations = await getDataFromDB()
    if (req.url === '/api' && req.method === 'GET'){
        sendJSONresponse(res, 200, destinations)
    }
    else if(req.url.startsWith('/api/continent/') && req.method === 'GET'){
        const filteredData = sendFilterData(destinations, 'continent', continent) 
        sendJSONresponse(res, 200, filterData) 
    }
    else if(req.url.startsWith('/api/country') && req.method === 'GET'){
        const continent = req.url.split('/').pop()
        const filteredData = sendFilterData(destinations, 'continent', continent) 
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