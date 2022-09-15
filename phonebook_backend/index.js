const express = require('express')
const morgan = require('morgan')
const app = express()
app.use(express.json())
const cors = require('cors')
app.use(cors())
app.use(express.static('build'))  
app.use(morgan(':method :url :status :response-time :data'))

morgan.token('data', function (req, res) {
  return JSON.stringify(req.body)
})

const d = new Date()
let persons = [
    { 
      "id": 1,
      "name": "Arto Hellas", 
      "number": "040-123456"
    },
    { 
      "id": 2,
      "name": "Ada Lovelace", 
      "number": "39-44-5323523"
    },
    { 
      "id": 3,
      "name": "Dan Abramov", 
      "number": "12-43-234345"
    },
    { 
      "id": 4,
      "name": "Mary Poppendieck", 
      "number": "39-23-6423122"
    }
]

const info = `<p>Phonebook has info for ${persons.length} people</p>
              ${d}`


const generateID = () => {
  const min = 1
  const max = 1000
  return Math.floor(Math.random() * (max - min + 1) + min); 
}

const unknownEndpoint = (request, response) => {
  response.status(404).send({ error: 'unknown endpoint' })
}

// app.use(unknownEndpoint)



app.get('/api/persons', (request, response) => {
    response.json(persons)
  })

app.get('/', (request, response)=> {
  response.send("<h1>Hello World</h1>")
})

app.get("/info", (request, response)=> {
  response.send(info)
})

app.get("/api/persons/:id", (request, response)=> {
  const id = Number(request.params.id)
  const person = persons.find(person => person.id === id)
  if(person == null) {
    response.status(400).json({
      error:"Person Missing"
    })
  }
  else {
    response.json(person)
  }
})

app.delete("/api/persons/:id", (request, response)=> {
  const id = Number(request.params.id)
  persons  = persons.filter(person => person.id!==id)
  response.status(204).end()
})

app.post("/api/persons", (request, response) => {
  
  const body = request.body


  if(!body.name){
    return response.status(400).json({
      error: "Name missing"
    })
  }
  if(!body.number){
    return response.status(400).json({
      error: "Number missing"
    })
  }

  if(persons.find(person => person.name === body.name)) {
    return response.status(400).json({
      error: "name must be unique"
    })
  }

  const person = {
    id: generateID(),
    name: body.name,
    number: body.number,
  }

  persons = persons.concat(person)
  response.json(person)
})


const PORT = process.env.PORT || 3001
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`)
})