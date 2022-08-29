import DisplayOneCountry from "./DisplayOneCountry";
const Display = ({countriesToShow, setCountriesToShow, filter}) => {

    if(countriesToShow.length > 10) {
        return (
            <div>
                Too many matches, specify another filter
            </div>
        )
    }
    else if (countriesToShow.length === 1) {
        return (
            <div>
                <DisplayOneCountry country = {countriesToShow[0]} />
            </div>
        )
    }
    else {
        return ( 
            <div>
                {countriesToShow.map(country => <ul key = {country.name.common}>{country.name.common} <button onClick = {() => setCountriesToShow([country])}>Show</button></ul>)}
            </div>
         );
    }
    
}
 
export default Display;