import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

  save = () => {
    const input = document.getElementById("input").value;
    document.write(input);

  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Hire'lytics</h1>
        </header>
        <label>Enter Resume: </label>
        <textarea id ="input" name="input" rows="10" cols="30">
        </textarea>
        <br />

      <button type = "submit" onClick={this.save}> Submit </button>
      </div>
    );
  }
}

export default App;
