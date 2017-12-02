import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Hire'lytics</h1>
        </header>
        <label>Enter Resume: </label>
        <input type="text" name="Resume Input" placeholder="Resume Input" />
      <br />

      <button type = "submit" onClick=""> Submit </button>
      </div>
    );
  }
}

export default App;
