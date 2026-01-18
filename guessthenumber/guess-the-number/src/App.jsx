import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function App() {

  const [randomNumber, setRandomNumber] = useState(Math.floor(Math.random() * 100) + 1 );

  const [userGuess, setUserGuess] = useState("");
  const [feedback, setFeedback] = useState("enter a number");

  const handleUserGuess= (e) => {
    setUserGuess(e.target.value)
  }

  const handleFeedback= () => {
    let guess = Number(userGuess) 
    if(guess < randomNumber ) {
      setFeedback(" too low, try again")
    }
    else if(guess> randomNumber) {
      setFeedback(" too high, try again")
    }
    else
    {
      setFeedback( " 7 CROREEEEEEEEEEE!")
    }
  }

  


  return (
    <>
      <div>Guess the number</div>
      <div>

      <input value={userGuess} onChange={handleUserGuess}  type="number" />
      <button onClick={handleFeedback}>Guess</button>


      </div>

      <div onChange={handleFeedback} > {feedback} {console.log()} </div>
    </>
  );
}



export default App
