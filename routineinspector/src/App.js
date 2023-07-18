import { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the Routine Inspector! What's your routine?
        </p>
        <RoutineForm />
      </header>
    </div>
  );
}

function RoutineForm() {
  const [routine, setRoutine] = useState("");
  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`The name you entered was: ${routine}`)
  }
  return (
    <form onSubmit={handleSubmit}>
      <label> Routine: </label>
      <input type="textarea" name="routine" onChange={(e) => setRoutine(e.target.value)} />
      <input type="submit" value="Submit" />
    </form>
  );
}

export default App;
