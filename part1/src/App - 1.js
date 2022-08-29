import React from 'react'
import { useState } from 'react'

const History = (props) => {
  if(props.allClicks.length === 0){
    return(
      <div>
        The app works by clicking on any of the button.
      </div>
    )
  }
  return(
    <div>
      Button press history: {props.allClicks.join(' ')}
    </div>
  )

}

const Button = (props) => {
  return (
    <div>
      <button onClick = {props.handleClick}>{props.text}</button>
    </div>
  )
}

const App = () => {
  const [click, setClick] = useState({
    left: 0, 
    right: 0
  })
  const [allClicks, setAllClicks] = useState([])

  const handleLeftClick = () => {
    const newClicks = {
      ...click,
      left: click.left+1
    }
    setAllClicks(allClicks.concat('L'))
    setClick(newClicks)
  }

  const handleRightClick = () => {
    const newClicks = {
      ...click,
      right: click.right+1
    }
    setAllClicks(allClicks.concat('R'))
    setClick(newClicks)
  }

  return (
    <div>
    {click.left} {click.right}
    <Button handleClick = {handleLeftClick} text = "Left" />
    <Button handleClick = {handleRightClick} text = "Right" />
    <History allClicks = {allClicks}/>
    </div>
  )
}

export default App