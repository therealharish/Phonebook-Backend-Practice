import { useEffect, useState } from 'react'
import AddNewNumber from './components/AddNewNumber'
import Filter from './components/Filter'
import Notification from './components/Notification'
import PersonsToShow from './components/PersonsToShow'
import contactServices from './services/contactServices'
import './App.css';

const App = () => {
  const [persons, setPersons] = useState([])
  const [newName, setNewName] = useState('')
  const [newNumber, setNewNumber] = useState('')
  const [personsToShow, setPersonsToShow] = useState([])
  const [filter, setFilter] = useState('')
  const [notification, setNotification] = useState(null)
  useEffect(() => {
    contactServices
      .getAll()
      .then(persons => {
        console.log(persons)
        setPersons(persons)
        setPersonsToShow(persons)
      })
  }, [])

  const checkIfNameAlreadyExists = (name) => {
    if(persons.some(e => e.name === name)) {
      return true
    }
    else {
      return false
    }
  }

  const handleFormSubmit = (event) => {
    event.preventDefault()
    if(checkIfNameAlreadyExists(newName)) {
      if(newNumber === ""){
        alert("Number is required")
      }
      const confirmNumberChange = window.confirm(`${newName} is already in the contact list. Do you want to replace the old number with a new one?`)
      if(confirmNumberChange) {
        const id = persons.find(e => e.name === newName).id
        const obj = {name: newName, number: newNumber, id: id}
        contactServices
          .update(id, obj)
          .then(response => {
            console.log(response)
            setPersons(persons.map(e => e.name === newName ? obj : e))
            setPersonsToShow(personsToShow.map(e => e.name === newName ? obj : e))
            setNotification(`Number Updated!`)
            setTimeout(() => {
              setNotification(null)
            }, 5000)
          })
      }
    }
    else {
      if(newName === "" || newNumber === "") {
        alert("One of the fields is empty, please check")
      }
      else {
        const obj = {name: newName, number: newNumber}
        contactServices
          .create(obj)
          .then(personsRecieved => {
            setPersons(persons.concat(personsRecieved))
            setNewName('')
            setNewNumber("")
            setPersonsToShow(persons.concat(personsRecieved))
            setNotification(`Added ${obj.name}`)
            setTimeout(() => {
              setNotification(null)
            }, 5000)
          })


      }
    }
    
  }

  const handleNewNameAdd =(event) => {
    setNewName(event.target.value)
  }

  const handleNewNumberChange =(event) => {
    setNewNumber(event.target.value)
  }

  const handleFilterChange = (event) => {
    setFilter(event.target.value)
    if(filter.length === 0) {
      setPersonsToShow(persons)
    }
    else {
      console.log(persons[0].name.includes("art"));
      const filterArr = persons.filter(person => person.name.includes(filter))
      console.log(filterArr);
      setPersonsToShow(filterArr)
    }
    console.log(filter)
  }

  if(persons){
    return (
    <div className = 'desktop-1'>
      <div className = "frame-1">
        <h2 className = "phonebook">Phonebook</h2>
        <Notification message = {notification}/>
        <Filter filter = {filter} handleFilterChange = {handleFilterChange} />
        <AddNewNumber 
          newName = {newName} 
          handleNewNameAdd = {handleNewNameAdd} 
          newNumber = {newNumber} 
          handleNewNumberChange = {handleNewNumberChange} 
          handleFormSubmit = {handleFormSubmit} 
        />
        <h2>Numbers</h2>
        <PersonsToShow 
          personsToShow = {personsToShow} 
          setPersonsToShow = {setPersonsToShow} 
          setPersons = {setPersons} 
          persons = {persons}
          notification = {notification}
          setNotification = {setNotification}
        />
      </div>
    </div>
  )}
  else {
    return (
      <div>
        Loading...
      </div>
    )
  }
}

export default App