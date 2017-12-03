const SimpleBarChart =(data1) = React.createClass({
 render () {
   return (
     <BarChart width={600} height={300} data={data1}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="name"/>
       <YAxis/>
       <CartesianGrid strokeDasharray="3 3"/>
       <Tooltip/>
       <Legend />
       <Bar dataKey="yourdata" fill="#8884d8" />
       <Bar dataKey="average" fill="#82ca9d" />
      </BarChart>
    );
  }
});
