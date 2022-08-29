import axios from "axios";
import { useEffect, useState } from "react";

const Weather = (props) => {
    const lat = props.country.latlng[0];
    const lng = props.country.latlng[1];
    console.log(lat, lng)
    const [weather, setWeather] = useState(null);
    const [icon, setIcon] = useState("")
    const api_key = process.env.REACT_APP_API_KEY

    useEffect(() => {
        axios
            .get(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${api_key}`)
            .then(response => {
                console.log(response.data)
                setWeather(response.data)
                setIcon(`http://openweathermap.org/img/wn/${response.data.weather[0].icon}@2x.png`)
            })
    }, [lat, lng, api_key])
    
    
    if(weather){
        return ( 
            <div>
                <h2>Weather in {props.country.name.common}</h2>
                <p>Temperature: {weather.main.temp}</p>
                <br/>
                <img src = {icon} alt ="Weather Icon" />
                <br/>
                <p>Wind: {weather.wind.speed}</p>
            </div>
         );

    }
    else {
        return(
            <p>Loading weather data...</p>
        )
        
    }
}
 
export default Weather;