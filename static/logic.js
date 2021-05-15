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
 
  
}})
Highcharts.chart('container', {

  chart: {
      type: 'bubble',
      plotBorderWidth: 1,
      zoomType: 'xy'
  },

  legend: {
      enabled: false
  },

  title: {
      text: 'Alcohol and Happiness by Country'
  },

  // subtitle: {
  //     text: 'Source: <a href="http://www.euromonitor.com/">Euromonitor</a> and <a href="https://data.oecd.org/">OECD</a>'
  // },

  // accessibility: {
  //     point: {
  //         valueDescriptionFormat: '{index}. {point.name}, fat: {point.x}g, sugar: {point.y}g, obesity: {point.z}%.'
  //     }
  // },

  xAxis: {
      gridLineWidth: 1,
      title: {
          text: 'Alcohol Consumption per Capita'
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
              text: 'Safe fat intake 65g/day'
          },
          zIndex: 3
      }],
      accessibility: {
          rangeDescription: 'Range: 60 to 100 grams.'
      }
  },

  yAxis: {
      startOnTick: false,
      endOnTick: false,
      title: {
          text: 'World Happiness Score'
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
              text: 'Safe sugar intake 50g/day',
              x: -10
          },
          zIndex: 3
      }],
      accessibility: {
          rangeDescription: 'Range: 0 to 160 grams.'
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
    data: 
      point
    }]

});
})


