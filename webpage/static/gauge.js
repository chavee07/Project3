

///////DROPDOWN//////////
function init() {
    d3.json("/landing").then((data)=> {
    // console.log( data);
    

    //set dropdown menu w/ id//
    data.forEach((d) => {
        var countries = data.map(d => d.Country);
        // console.log(countries)

        var scores =data.map(d =>d.Score);
        // console.log(scores)

d3.select("#selDataset").append("option").text(d.Country).property("value");


});


plots(data[0].Country)
scoreInfo(data[0].Country);



    
})
};




//create function demographic data//
function scoreInfo(id) {
    d3.json("/landing").then((data)=> {
        //call in metadata to demographic panel//
    
    
   result = data.filter(s => s.Country.toString() === id)[0];
        //select demographic panel from html//
    var info = d3.select("#sample-metadata");
        //empty the demographic panel for new data//
    info.html("");
   
    
    
    
    Object.entries(result).forEach(([key,value]) => {   
        console.log(key,value)
        info.append("h5").text(key+ ": " + value);   
        });


        
    });

};



//create function for data//
function plots(id) {
    d3.json("/landing").then((data)=> {
        // console.log(data)

       
   console.log(data)

     
        
var countryScore = data.filter(s => s.Country.toString() === id);
console.log(countryScore)
    




        //guage chart//
    var data_guage = [{
        domain: {x: [0, 1], y: [0, 1]},
        value: parseFloat(countryScore[0].Score),
        title: {text: `Country Happiness`},
        type: "indicator",
        mode: "gauge+number",
        gauge: { axis: { range: [null, 9], },
        bar : { color: "rgb(31, 233, 172)" },
        borderwidth: 5,
        bordercolor: "darkblue",
        steps: [
        {range: [0, 2], color: "royalblue"},
        {range: [2, 7], color: "rgb(194, 4, 178)"},
        {range: [7, 9], color: "rgb(14, 59, 126)"},
    ],

    threshold: {
        line: {
          color: "red",
          width: 4
        },
        thickness: 0.75,
        value: 8.9
      }




}
}];




    var layout_guage = { 
    width: 600, 
    height: 500, 
    margin: { t: 25, b: 45, l:25, r:25 } 
    };

    Plotly.newPlot("gauge", data_guage, layout_guage);




//// copy gauge chart above and chance Score from value to alchol consumtiion////////
///// call in alcohol consumption [0]["Alchol Constu from data exact name"]////////


        //guage chart//
        var data_guage = [{
            domain: {x: [0, 1], y: [0, 1]},
            value: parseFloat(countryScore[0]["Alcohol Consumption per Capita (liter)"]),
            title: {text:`Alcohol Consumption `},
            type: "indicator",
        mode: "gauge+number",
        gauge: { axis: { range: [null, 15] },
        bar : { color: "  rgb(31, 233, 172)"},
        borderwidth: 5,
        bordercolor: "darkblue",
        steps: [
        {range: [0, 3], color: "royalblue"},
        {range: [3, 12], color: "rgb(194, 4, 178)"},
        {range: [12, 15], color: " rgb(14, 59, 126)"},
        ],
        threshold: {
            line: {
              color: "red",
              width: 4
            },
            thickness: 0.75,
            value: 14.8
          }
    
    }
        }];

    
        var layout_guage = { 
        width: 600, 
        height: 500, 
        margin: { t: 25, b: 25, l:25, r:25 } 
        };
    
        Plotly.newPlot("gauge2", data_guage, layout_guage);





});
}  


init();

//change function// 
    function optionChanged(id){
    scoreInfo(id);
    plots(id);
}