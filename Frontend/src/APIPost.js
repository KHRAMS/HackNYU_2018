
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from "axios";


 post = (inputi) => {


    const test = axios.put("http://localhost:5000/test", {input: inputi}).then((response) =>
    {

        alert(response.data['output']['input']);// Remember, output is the metadata in our dictionary. The result is the result of the backend processing
                                                     // The output is already in list form(although the alert won't show it) so you can index.
                                                     // like response.data['output'][0]



        //TODO --> Render this better.
        //
        // const element = (
        //  <div className="response">
        //      [[{response.data['output']['prediction'][0]},{response.data['output']['prediction'][1]}]]
        //  </div>
        // );
        //
        // ReactDOM.render(element, document.getElementById('root'));



    }
)



    return test
}
