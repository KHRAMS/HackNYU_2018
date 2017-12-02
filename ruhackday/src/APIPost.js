
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from "axios";


export const post = () => {


    const test = axios.put("http://localhost:5000/test", {blah: ["When was Barack Obama's birthday?", "When was Barack Obama's birthday?"], num : 600}).then((response) =>
    {

        alert(response.data['output']['prediction']);// Remember, output is the metadata in our dictionary. The result is the result of the backend processing
                                                     // The output is already in list form(although the alert won't show it) so you can index.
                                                     // like response.data['output'][0]



        //TODO --> Render this better.

        const element = (
         <div className="response">
             [[{response.data['output']['prediction'][0]},{response.data['output']['prediction'][1]}]]
         </div>
        );

        ReactDOM.render(element, document.getElementById('root'));



    }
)



    return test
}