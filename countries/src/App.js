import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Display from './components/Display';

function App() {
  const [countries, setCountries] = useState([]);
  const [countriesToShow, setCountriesToShow] = useState([]);
  const [filter, setFilter] = useState('');

  //axios method to import data form a link
  useEffect(() => { 
    axios
      .get('https://restcountries.com/v3.1/all')
      .then(response => {
        setCountries(response.data);
        setCountriesToShow(response.data);
      });
    }, [])
  
  const handleFilterChange = (event) => {
    setFilter(event.target.value)
    console.log(filter)
    if(filter.length === 0) setCountriesToShow(countries)
    else setCountriesToShow(countriesToShow.filter(country => country.name.common.includes(filter)))
  }

  const handleFormSubmit = (event) => {
    event.preventDefault()
  }
  

  return (
    <div className="App">
      <form onSubmit = {handleFormSubmit}>
        search:
        <input value = {filter}
          onChange = {handleFilterChange}
        />
      </form>
      
      <Display countriesToShow = {countriesToShow} setCountriesToShow = {setCountriesToShow} filter = {filter}/>
      {/* <DisplayOneCountry country = {countriesToShow[0]} /> */}
    </div>
  );
}

export default App;
