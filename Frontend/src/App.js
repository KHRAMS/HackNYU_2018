import React, { Component } from 'react';
import './App.css';
import axios from "axios";

class App extends Component {

  post = (input) => {
    const test = axios.put("http://localhost:5000/test", {input: input}).then((response) =>
    {

        alert(response.data['output']['input']);
    }).catch(error => {
      alert(error);
    });
    return test
  };

  save = () => {
    const input = document.getElementById("input").value;
    document.write(input);
    this.post(input);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
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
