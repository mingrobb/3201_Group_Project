/* jshint esversion: 6 */



var content = new Vue
(
    {
        el: '#content',
        data:
        {
            show_dashboard: true,
            x_style_area: "width: calc(100% - 400px);",
            generation_n: 10,
            individual_n: 3,
        },
        methods:
        {
            toggleDashboard: function()
            {
                if(this.show_dashboard==true)
                {   this.x_style_area = "width: initial;";
                    this.show_dashboard = false;
                }
                else
                {   this.x_style_area = "width: calc(100% - 400px);";
                    this.show_dashboard = true;
                }
            }
        },
    }
);

function parseCoords(map)
{
    var plotly_coords = [ [],[],[] ];
    for(let city of map)
    {
        plotly_coords[0].push(city[0]);
        plotly_coords[1].push(city[1]);
        plotly_coords[2].push(city[2]);
    }
    return plotly_coords;
}

// plot plain map //
var plain_map = null;

if(true)    //trace.description.name == "WesternSahara"
{
    plain_map = parseCoords(WesternSahara);
}
else if(trace.description.name == "Uruguay")
{
    plain_map = parseCoords(Uruguay);
}
else if(trace.description.name == "Canada")
{
    plain_map = parseCoords(Canada);
}

Plotly.plot
(
    $(".figure.map")[0],
    [
        {
            x: plain_map[1],
            y: plain_map[2],
        }
    ],
    {
        margin: { t: 0 }
    },
    {responsive: true}
);
