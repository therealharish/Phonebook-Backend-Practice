import Hello from "./components/Hello.js"

const footer = () => {
  return (
    <div>
      greeting app created by <a href="https://github.com/mluukkai">mluukkai</a>
    </div>
  )
}

const App = () => {
  const name = "Harish"
  const age = 20
  return (
  <div>
    <Hello name = {name} age = {age}/>
    <footer />
  </div>
)}




export default App