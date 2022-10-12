const express = require('express')
const app = express()
const cors = require('cors')
app.use(express.json())
app.use(cors())
app.use(express.static('build'))
require('dotenv').config()
const Note = require('./models/note')
const mongoose = require('mongoose')

let notes = [
    {
      id: 1,
      content: "HTML is easy",
      date: "2022-05-30T17:30:31.098Z",
      important: true
    },
    {
      id: 2,
      content: "Browser can execute only Javascript",
      date: "2022-05-30T18:39:34.091Z",
      important: false
    },
    {
      id: 3,
      content: "GET and POST are the most important methods of HTTP protocol",
      date: "2022-05-30T19:20:14.298Z",
      important: true
    }
]

app.get("/", (request, response) => {
    response.send('<h1>Hello World!<h1>')
})

app.get("/api/notes", (request, response) => {
  Note.find({}).then(note => {
    response.json(note)
  }) 
})

app.get("/api/notes/:id", (request,response, next) => {
    const id = request.params.id
    Note
      .findById(id)
      .then(note => {
        if(note){
          response.json(note)
        } else {
          response.status(404).end()
        }
      })
      .catch(error => next(error))
    })

app.delete("/api/notes/:id", (request,response) => {
    const id = request.params.id
    Note
      .findByIdAndRemove(id)
      .then(result => {
        response.status(204).end()
      })
      .catch(error => next(error)) //next error is used because we now have a middleware to do it
})

const generateId = () => {
    const maxId = notes.length > 0
      ? Math.max(...notes.map(n => n.id))
      : 0
    return maxId + 1
  }

app.post('/api/notes', (request, response, next) => {
    const body = request.body
  
    if (!body.content) {
      return response.status(400).json({ 
        error: 'content missing' 
      })
    }
  
    const note = new Note({
      content: body.content,
      important: body.important || false,
      date: new Date(),
    })
  
    note
      .save()
      .then(savedNote => {
        response.json(savedNote)
      })
      .catch(error => next(error))
})

app.put('/api/notes/:id', (request, response) => {
  // this was before we started using validators intro - 3d
  // const body = request.body
  // const id = request.params.id
  // const note = {
  //   content: body.content,
  //   important: body.important
  // }
  // Note
  //   .findByIdAndUpdate(id, note, {new: true, runValidators})
  //   .then(updatedNote => {
  //     response.json(updatedNote)
  //   })
  //   .catch(error => next(error))

  const {content, important} = request.body
  const id = request.params.id
  Note
    .findByIdAndUpdate(id,
      {content,  important},
      {new: true, runValidators: true, context:'query'}
      )
    .then(updatedNote => {
      response.json(updatedNote)
    })
    .catch(error => next(error))
})  

const PORT = process.env.PORT
app.listen(PORT, () => {
    console.log(`Server running on Port: ${PORT}`)
})

const unknownEndpoint = (request, response) => {
  response.status(404).send({error: 'unknown endpoint'})
}

const errorHandler = (error, request, response, next) => {
  console.error(error.message)
  if(error.name === 'CastError') {
    return response.status(400).send({error: 'malformatted id'})
  }
  else if(error.name === "ValidationError"){
    return response.status(400).send({error: error.message  })
  }
  next(error)
}

app.use(unknownEndpoint)
app.use(errorHandler)