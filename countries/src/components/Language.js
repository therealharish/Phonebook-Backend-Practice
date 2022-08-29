
const Langauge = (props) => {

    var newLang = []
    for (const language in props.languages) {
        newLang.push(props.languages[language])
    
    }


    

    return ( 
        <div>
        <h3>Langauages</h3>
        <div>
            {newLang.map(language => <li key = {language}>{language}</li>)}
        </div>
        </div>
     );
}
 
export default Langauge;