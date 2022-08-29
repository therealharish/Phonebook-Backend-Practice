import '../index.css'
const Note = ({note, toggleImportance, deleteANote}) => {
  const label = note.important ? 'make not important' : 'make important'
  return ( 
          <li className = "notes">
            <p>{note.content} <button onClick = {toggleImportance}>{label}</button> <button onClick = {deleteANote}>Delete</button></p>

          </li>
        )
}
 
export default Note;

