import Note from "./components/Note"
import {useEffect, useState} from 'react'
// import axios from 'axios'
import noteServices from './services/notes'
import './index.css'
import Notifications from "./components/Notifications"
import Footer from "./components/Footer"

const App = (props) => {
  const [notes, setNotes] = useState([])
  const [newNote, setNewNote] = useState(
    'a new note...'
  ) 
  const [showAll, setShowAll] = useState(true)
  const [errorMessage, setErrorMessage] = useState(null)
  const notesToShow = showAll ? notes: notes.filter(item => item.important === true)

  useEffect(()=> {
    console.log("effect...")
    noteServices
      .getAll()
      .then(initialNotes => {
        setNotes(initialNotes)
      })
  }, [])
  
  const addNote = (event) => {
    event.preventDefault()

    const noteObject = {
      content: newNote,
      date: new Date().toISOString(),
      important: Math.random() < 0.5,
      id: notes.length + 1,
    }

    noteServices
      .create(noteObject)
      .then(newThing => {
        setNotes(notes.concat(newThing))
        setNewNote("")
      })
  }

  const deleteANote = (id) => {
    console.log("deleting...")
    noteServices
      .deleteNote(id)
      .then(undeletedNotesReceieved=> {
        setNotes(notes.filter(note => note.id!==id))
      })

  }

  const handleNoteInput = (event) => {
    setNewNote(event.target.value)
  }

  const handleNotesShow = () => {
    setShowAll(!showAll)
  }

  //function to toggle importance of given note
  const toggleImportance = (id) => {
    // const url = `http://localhost:3001/notes/${id}`
    console.log("Changing importance of" +id)
    const note = notes.find(note => note.id === id)
    const changedNote = {...note, important: !note.important}

    noteServices
      .update(id, changedNote)
      .then(changedNoteReceived => {
        setNotes(notes.map(note => note.id === id?changedNoteReceived: note))
      })
      .catch(error => {
        setErrorMessage(`Note '${note.content}' has already been deleted`)
        setTimeout(() => {
          setErrorMessage(null)
        }, 5000)
        setNotes(notes.filter(note => note.id!==id))
      })
  }


  return (
    <div>
      <h1>Notes</h1>
      <Notifications message = {errorMessage} />
      <ul>
        {notesToShow.map(note => <Note 
                                    key = {note.id} 
                                    note = {note} 
                                    toggleImportance = {() => toggleImportance(note.id)} 
                                    deleteANote = {()=> deleteANote(note.id)}/>)}
      </ul>
      <button onClick = {handleNotesShow}>Show {showAll?'Important':'All'}</button>
      <form onSubmit = {addNote}>
        <input 
          value = {newNote}
          onChange = {handleNoteInput}
        />
        <button type = "submit">Save</button>
      </form>
      <Footer/>
    </div>
  )
}

export default App