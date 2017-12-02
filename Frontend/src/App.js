import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

  save = () => {
    const input = document.getElementById("input").value;

  }
  
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Hire'lytics</h1>
        </header>
        <label>Enter Resume: </label>
        <input type="text" id="input" name="input" placeholder="Resume" />
      <br />

      <button type = "submit" onClick={this.save}> Submit </button>
      </div>
    );
  }
}

export default App;
