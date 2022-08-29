import Language from './Language';
import Weather from './Weather';
const DisplayOneCountry = (props) => {
    console.log(props.country)
    return ( 
        <div>
            <h2>{props.country.name.common}</h2>
            <div>
                Capital: {props.country.capital}
                <br />
                Area: {props.country.area}
            </div>
            <Language languages = {props.country.languages} />
            <br/>
            <img src = {props.country.flags.png} alt = "flag" width = "100" height = "100"/>
            <Weather country = {props.country} />
        </div>
     );
}
 
export default DisplayOneCountry;