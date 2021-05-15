// Parse the Data
d3.json("/data").then(function(data) {

  console.log(data)
  var countries = data.map(c => c.Country);
  var scores = data.map(c=>c.Happiness_Score);
  var alcohol = data.map(c=>c.Alcohol_Consumption)

  var result = {};
  countries.forEach((key, i) => result[key] = scores[i]);
  console.log(result);

function makeResponsive() {
// set the dimensions and margins of the graph
var margin = {top: 20, right: 30, bottom: 40, left: 90},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#chart")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  // Add X axis
  var x = d3.scaleLinear()
    .domain([0,8])
    .range([ 0, width]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .style("text-anchor", "end");

  // Y axis
  var y = d3.scaleBand()
    .range([ 0, height ])
    .domain(data.map(function(d) { return d.Country; }))
    .padding(.1);
  svg.append("g")
    .call(d3.axisLeft(y))

  //Bars
  svg.selectAll("rect")
    .data(data)
    .enter()
    .append("rect")
    .attr("x", x(0) )
    .attr("y", function(d) { return y(d.Country); })
    .attr("width", function(d) { return x(d.Happiness_Score); })
    .attr("height", y.bandwidth() )
    .attr("fill", "#69b3a2")
    .on("click", function(d, i) {
      alert(`Country: ${countries[i]} \r\n Happiness Score: ${scores[i]} \r\n Alcohol Comsunption/Capita (liter): ${alcohol[i]}`);
    })
    .on("mouseover", function() {
      d3.select(this)
            .attr("fill", "red");
    })
    // event listener for mouseout
    .on("mouseout", function() {
      d3.select(this)
            .attr("fill", "#69b3a2");
    });


}

makeResponsive();

});
