import React, { Component } from 'react';
import './App.css';
import axios from "axios";
import ReactDOM from 'react-dom';
import {BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';

class App extends Component {

  post = (input) => {
    const test = axios.put("http://localhost:5000/test", {input: input}).then((response) =>
    {
const datas =response.data['output']['ctc'];
const datayoe =response.data['output']['yrs_exp'];

    //    alert(response.data['output']['stuff']);

const datasal = [
       {name: 'name', yourdata: datas, average: 161955.17}
   ];

 const datayears = [
          {name: 'name', yourdata: datayoe, average: 8.42}
      ];



const element = <div className="App">
  <header className="App-header">
    <img className="photo" src="https://ak6.picdn.net/shutterstock/videos/25050416/thumb/1.jpg" />
    <h1 className="App-title">Hirelytics</h1>
  </header>
  <h1 className="OutputTitle">Based on your resume you may earn ${datas}</h1>
  <h1 className="SALARY">Salary Comparison</h1>
  <BarChart title="Salary Comparison" className= "graph" width={600} height={300} data={datasal}
         margin={{top: 5, right: 30, left: 20, bottom: 5}}>
    <XAxis dataKey="Salary Comparison"/>
    <YAxis/>
    <CartesianGrid strokeDasharray="3 3"/>
    <Tooltip/>
    <Legend />
    <Bar dataKey="yourdata" fill="#8884d8" />
    <Bar dataKey="average" fill="#82ca9d" />
   </BarChart>

   <h1 className="YOE" >Years of Experience Comparison</h1>
   <BarChart title="Years of Experience Comparison" className= "graph" width={600} height={300} data={datayears}
          margin={{top: 5, right: 30, left: 20, bottom: 5}}>
     <XAxis dataKey="Years of Experience Comparison"/>
     <YAxis/>
     <CartesianGrid strokeDasharray="3 3"/>
     <Tooltip/>
     <Legend />
     <Bar dataKey="yourdata" fill="#8884d8" />
     <Bar dataKey="average" fill="#82ca9d" />
    </BarChart>
</div> ;
    ReactDOM.render(
      element,
      document.getElementById('root')
    );
    }).catch(error => {
      alert(error);
    });
    return test
  };

  save = () => {
    const input = document.getElementById("input").value;
    // document.write(input);
    this.post(input);
  }



  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img className="photo" src="https://ak6.picdn.net/shutterstock/videos/25050416/thumb/1.jpg" />
          <h1 className="App-title">Hirelytics</h1>
        </header>
        <label className ="InputTitle">Enter Resume: </label>
         <textarea  className = "input"id ="input" name="input" rows="10" cols="30">
        </textarea>

        {/*<input type="file" className = "input" id = "input" />*/}
        <br />

      <button className = "submit" type = "submit" onClick={this.save}> Submit </button>
    </div>
    );
  }
}

export default App;
