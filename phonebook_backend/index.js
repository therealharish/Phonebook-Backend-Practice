require('dotenv').config()
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

const Contact = require('./models/contact')
const { update } = require('./models/contact')



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


app.get('/api/persons', (request, response) => {
    Contact.find({}).then(contact => {
        response.json(contact)
    })
  })

app.get('/', (request, response)=> {
  response.send("<h1>Hello World</h1>")
})

app.get("/info", (request, response)=> {
  response.send(info)
})

app.get("/api/persons/:id", (request, response, next)=> {
  const id = request.params.id

  //previous code when people were an object
  // const person = persons.find(person => person.id === id)
  // if(person == null) {
  //   response.status(400).json({
  //     error:"Person Missing"
  //   })
  // }
  // else {
  //   response.json(person)
  // }

  Contact
    .findById(id)
    .then(person => {
      if(person) {
        response.json(person)
      }
      else {
        response.status(404).end()
      }
    })
    .catch(error => next(error))
    })

app.delete("/api/persons/:id", (request, response, next)=> {

  // made when persons was an object
  // const id = Number(request.params.id)
  // persons  = persons.filter(person => person.id!==id)
  // response.status(204).end()

  id = request.params.id
  Contact
    .findByIdAndRemove(id)
    .then(result => {
      response.status(400).end()
    })
    .catch(error => next(error))
})

app.post("/api/persons", (request, response) => {
  
  const body = request.body
  console.log(body)


  // if(!body.name){
  //   return response.status(400).json({
  //     error: "Name missing"
  //   })
  // }
  // if(!body.number){
  //   return response.status(400).json({
  //     error: "Number missing"
  //   })
  // }

  // if(persons.find(person => person.name === body.name)) {
  //   return response.status(400).json({
  //     error: "name must be unique"
  //   })
  // }
  const person = new Contact({
    name: body.name,
    number: body.number,
  })

  person.save().then(savedPerson => {
    response.json(savedPerson)
  })
  
})

app.put("/api/persons/:id", (request, response, next) => {
  const body = request.body
  const id = request.params.id
  const newNum = {
    name: body.name,
    number: body.number
  }

  Contact
    .findByIdAndUpdate(id, newNum, {new: true})
    .then(updatedNum => {
      response.json(updatedNum)
    })
    .catch(error => next(error))
})

const unknownEndpoint = (request, response) => {
  response.status(404).send({ error: 'unknown endpoint' })
}

app.use(unknownEndpoint)

const errorHandler = (error, request, response, next) => {
  console.error(error.message)

  if(error.name == "CastError") {
    response.status(400).send({error: 'malformed id'})
  }
  next(error)
}

app.use(errorHandler)
const PORT = process.env.PORT || 3001
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`)
})