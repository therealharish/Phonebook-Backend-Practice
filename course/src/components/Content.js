import Part from "./Part";

const Content = ({parts}) => {
    const total = parts.reduce((s,p) => s + p.exercises, 0)

    return ( 
        <div>
            <ul>
                {parts.map(part => <Part key = {part.id} part = {part} />)}
                <p>Total of {total} exercises</p>
            </ul>
        </div>
     );
}
 
export default Content;