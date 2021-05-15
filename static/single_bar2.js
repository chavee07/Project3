
//set variables for the chart
var countries = []
var scores = []
var alcohol = []

d3.json("/data").then(function(d) {
  var countries = d.map(c => c.Country);
  var scores = d.map(c=>c.Happiness_Score);
  var alcohol =d.map(c=>c.Alcohol_Consumption);
  

console.log(alcohol)
console.log(scores)
console.log(countries)


var topcountries=countries.slice(0,10)
var topscores=scores.slice(0,10)
// console.log(topcountries)

var lowcountries=countries.slice(124,134)
var lowscores=scores.slice(124,134)
// console.log(lowcountries)

var chartcountries=topcountries.concat(lowcountries)
var chartscores=topscores.concat(lowscores)

console.log(chartcountries)



function makeResponsive() {

    // if the SVG area isn't empty when the browser loads,
    // remove it and replace it with a resized version of the chart
  var svgArea = d3.select("#chart").select("svg");

  if (!svgArea.empty()) {
    svgArea.remove();
  }

    // svg params
  var svgHeight = window.innerHeight;
  var svgWidth = window.innerWidth;

    // margins
  var margin = {
    top: 50,
    right: 75,
    bottom: 75,
    left: 75
  };

    // chart area minus margins
  var chartHeight = svgHeight - 300;
  var chartWidth = svgWidth - 300;

    // create svg container
  var svg = d3.select("#chart").append("svg")
        .attr("height", svgHeight)
        .attr("width", svgWidth);

    // shift everything over by the margins
  var chartGroup = svg.append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // scale y to chart height
  var yScale = d3.scaleLinear()
        .domain([0, d3.max(chartscores)])
        .range([chartHeight, 0]);

    // scale x to chart width
  var xScale = d3.scaleBand()
        .domain(chartcountries)
        .range([0, chartWidth])
        .padding(0.1);

    // create axes
  var yAxis = d3.axisLeft(yScale);
  var xAxis = d3.axisBottom(xScale);

    // set x to the bottom of the chart
  chartGroup.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(xAxis)
        .selectAll("text")  
    .style("text-anchor", "end")
    .attr("dx", "-.8em")
    .attr("dy", ".15em")
    .attr("transform", "rotate(-65)");

    // set y to the y axis
  chartGroup.append("g")
        .call(yAxis);


  chartGroup.selectAll("rect")
        .data(chartscores)
        .enter()
        .append("rect")
        .attr("x", (d, i) => xScale(chartcountries[i]))
        .attr("y", d => yScale(d))
        .attr("width", xScale.bandwidth())
        .attr("height", d => chartHeight - yScale(d))
        .attr("fill", "royalblue")
        // event listener for onclick event
        .on("click", function(d, i) {
          alert(`Country: ${chartcountries[i]} \r\n Happiness Score: ${chartscores[i]} \r\n Alcohol Comsunption/Capita (liter): ${alcohol[i]}`);
        })
        // event listener for mouseover
        .on("mouseover", function() {
          d3.select(this)
                .attr("fill", "purple");
        })
        // event listener for mouseout
        .on("mouseout", function() {
          d3.select(this)
                .attr("fill", "royalblue");
        });
}

makeResponsive();
});

// Event listener for window resize.
// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);
