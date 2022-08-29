import contactServices from "../services/contactServices"
const PersonsToShow = (props) => {
    //function to delete a contact from the server
    const deleteContact = (id) => {
        const person = props.personsToShow.find(person => person.id === id)
        if(person) {
            
        }
        const confirmDelete = window.confirm(`Are you sure you want to delete ${person.name}?`)
        if(confirmDelete) {
            console.log("Deleting contact with id: " + id)
            contactServices
                .deletePerson(id)
                .then(response => {
                    console.log(response);
                    props.setNotification(`Contact Deleted`)
                    setTimeout(() => {
                    props.setNotification(null)
                    }, 5000)
                    props.setPersonsToShow(props.personsToShow.filter(person => person.id!==id))
                    props.setPersons(props.persons.filter(person => person.id!==id))
                }
                )
                .catch(error => {
                    props.setNotification(`The contact was already deleted from server`)
                    setTimeout(() => {
                    props.setNotification(null)
                    }, 5000)
                    props.setPersonsToShow(props.personsToShow.filter(person => person.id!==id))
                    props.setPersons(props.persons.filter(person => person.id!==id))
                }
                )
        }
        else {
            alert("Deletion cancelled")
        }
        
    }

    return ( 
        <div>
        {props.personsToShow.map(person => <li key = {person.name}>{person.name} {person.number} <button onClick ={() => deleteContact(person.id)}>Delete</button></li>)}
        </div>
     );
}
 
export default PersonsToShow;