// set up json url
// url = "http://127.0.0.1/landing"
var point
d3.json("/landing").then(function(data) {
  // console.log(data);
  
var Countries = data.map(d => d.Country);
// console.log(Countries)

var Score= data.map(d => d.Score);
// console.log(Score)

var Ccode= data.map(d => d["Country Code"]);
// console.log(Ccode)

var Aconsumption = data.map(d => d["Alcohol Consumption per Capita (liter)"]);
// console.log(Aconsumption)

// Use `Object.keys` and `forEach` to iterate through keys
// var Happy = Object.values(data).forEach(value => console.log(value));

point=data.map(d=>{ return {
  x: d["Alcohol Consumption per Capita (liter)"],
  y: d.Score,
  z: d["Health life expectancy"],
  name: d["Country Code"],
  country: d.Country,
  freedom: d["Freedom to make life choices"],
  gdp:d["GDP per capita"],
  generosity: d.Generosity,
  perceptions: d["Perceptions of corruption"],
  socialSupport: d["Social support"]
  
  // var decTwo = Math.round(point[i] * 100) / 100
  
}})
var upperZ = []
var midZ = []
var lowZ = []
for (var i = 0; i < point.length; i++) {
            
    if (point[i].z >= .66) {
        upperZ.push(point[i])
    }
    else if (point[i].z>=.33) {
        midZ.push(point[i])
    }
    else {
        lowZ.push(point[i])
      }
}
console.log(upperZ)
Highcharts.chart('container', {

  chart: {
      type: 'bubble',
      backgroundColor: "#D7E3B8",
      plotBorderWidth: 1,
      zoomType: 'xy'
  },

//   legend: {
//     bubbleLegend: {
//         enabled: true,
//         minSize: 1,
//         maxSize: 16,
//         ranges: [{
//             value: 20
//         }, {
//             value: 20
//         },{value: 60

//         }]
//     }
//   },

  title: {
      text: 'Alcohol and Happiness by Country',
      style: {
        color: "#0B589D",
        fontSize: "25px",
        fontWeight:"bold"
    }
  },

    
  xAxis: {
      gridLineWidth: 1,
      title: {
          text: 'Alcohol Consumption per Capita',
          style: {
            color: "#0B589D",
            fontSize: "15px",
            fontWeight:"bold"
        }
      },
      labels: {
          format: '{value}'
      },
      plotLines: [{
          color: 'black',
          dashStyle: 'dot',
          width: 2,
          value: 65,
          label: {
              rotation: 0,
              y: 15,
              style: {
                  fontStyle: 'italic'
              },
              text: ''
          },
          zIndex: 2
      }],
      accessibility: {
          rangeDescription: ''
      }
  },

  yAxis: {
      startOnTick: false,
      endOnTick: false,
      title: {
          text: 'World Happiness Score',
          style: {
              color: "#0B589D",
              fontSize: "15px",
              fontWeight:"bold"
          }

      },
      labels: {
          format: '{value}'
      },
      maxPadding: 0.2,
      plotLines: [{
          color: 'black',
          dashStyle: 'dot',
          width: 2,
          value: 50,
          label: {
              align: 'right',
              style: {
                  fontStyle: 'italic'
              },
              text: '',
              x: -10
          },
          zIndex: 3
      }],
      accessibility: {
          rangeDescription: ''
      }
  },

  tooltip: {
      useHTML: true,
      headerFormat: '<table>',
      pointFormat: '<tr><th colspan="2"><h3>{point.country}</h3></th></tr>' +
          '<tr><th>Alcohol Consumption per Capita:</th><td>{point.x}</td></tr>' +
          '<tr><th>World Happiness Score:</th><td>{point.y}</td></tr>' +
          '<tr><th>Health Life Expectancy:</th><td>{point.z}</td></tr>',
      footerFormat: '</table>',
      followpointer: true
  },

  plotOptions: {
      series: {
          dataLabels: {
              enabled: true,
              format: '{point.name}'
          }
      }
  },

  series: [{
        minSize: 35,
        maxSize: 50,
        data:upperZ,
        name: "Upper Life Expectancy",
        opacity: 10
    },
    {
        minSize: 25,
        maxSize: 30,
        data:midZ,
        name: "Mid Life Expectancy"
    },
        
    {
        minSize: 10,
        maxSize: 20,
        data:lowZ,
        name: "Lower Life Expectancy",
        color: "#CA08C1",
        opacity: "5"
    }]
    

});
})


