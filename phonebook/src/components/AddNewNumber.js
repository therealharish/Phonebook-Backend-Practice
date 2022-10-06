const AddNewNumber = (props) => {
    return ( 
        <div className="add-new-contact">
        <h2 >Add a new</h2>
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
        </div>
    );
}
 
export default AddNewNumber;