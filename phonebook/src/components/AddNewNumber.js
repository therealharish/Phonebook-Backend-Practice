const AddNewNumber = (props) => {
    return ( 
        <form onSubmit = {props.handleFormSubmit}>
            <div>
                name: 
                <input
                    value = {props.newName}
                    onChange = {props.handleNewNameAdd} 
                />
            <br />
            number: 
                <input 
                    value = {props.newNumber}
                    onChange = {props.handleNewNumberChange}
                />
            </div>
            <div>
                <button type="submit">add</button>
            </div>
        </form>
    );
}
 
export default AddNewNumber;