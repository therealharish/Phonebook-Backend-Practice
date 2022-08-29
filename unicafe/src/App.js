import React from 'react'
import {useState} from 'react'
import Button from './components/Button.js'
import Statistics from './components/Statistics.js'


const App = () => {
  // save clicks of each button to its own state
  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)
  

  const incrementGood = () => {
    setGood(good+1)
  }

  const incrementNeutral = () => {
    setNeutral(neutral+1)
  }

  const incrementBad = () => {
    setBad(bad+1)
  }

  return (
    <div>
      <h1>Give Feedback</h1>
      <Button text = "good" handleClick = {incrementGood} />
      <Button text = "bad" handleClick = {incrementBad} />
      <Button text = "neutral" handleClick = {incrementNeutral} />
      <Statistics good = {good} bad = {bad} neutral = {neutral} />
      
    </div>
  )
}

export default App

