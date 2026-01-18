import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

    const randomNumber = Math.floor(Math.random() * 100) + 1;

    const [userGuess, setUserGuess] = useState(0);
    const [feedback, setFeedback] = useState('');

    const handleInputChange = (e) => {
        setUserGuess(e.target.value);
    };

    const handleGuess = () => {
        const guess = parseInt(userGuess, 10);
        if (guess < 1 || guess > 100 || isNaN(guess)) {
            setFeedback('Please enter a number between 1 and 100.');
        } else if (guess < randomNumber) {
            setFeedback('Too low! Try again.');
        } else if (guess > randomNumber) {
            setFeedback('Too high! Try again.');
        } else {
            setFeedback('Congratulations! You guessed the number!');
        }
    };


    console.log('Random Number (for testing purposes):', randomNumber);

  return (
    <>
        <input className="card" type="number" onChange={handleInputChange} value={userGuess} />
        <button className="card" onClick={handleGuess}>Guess</button>
        <div className="card">{feedback}</div>

    </>

  )
}

export default App
