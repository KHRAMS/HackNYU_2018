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
          <img className="photo" src="https://ak6.picdn.net/shutterstock/videos/25050416/thumb/1.jpg" />
          <h1 className="App-title">Hire'lytics</h1>
        </header>
        <label className ="InputTitle">Enter Resume: </label>
        <textarea  className = "input"id ="input" name="input" rows="10" cols="30">
        </textarea>
        <br />

      <button className = "submit" type = "submit" onClick={this.save}> Submit </button>
      </div>
    );
  }
}

export default App;
