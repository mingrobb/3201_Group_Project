/* jshint esversion: 6 */



var content = new Vue
(
    {
        el: '#content',
        data:
        {
            instance_select: "WesternSahara",
            algorithm_select: ["basic","advanced"],
            show_dashboard: true,
            x_style_area: "width: calc(100% - 400px);",
            trial_n: 1,
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
            },
            newDraw: function()
            {
                /*
                    instance_select, rial_n, generation_n, individual_n
                    根据选择的实例、测试、世代、个体
                */
                // 重绘plain map -------------------------------------------------------------------------------
                let plain_map = null;

                if(this.instance_select == "WesternSahara")
                {
                    plain_map = plain_map_WesternSahara;    console.log(plain_map);
                }
                else if(this.instance_select == "Uruguay")
                {
                    plain_map = plain_map_Uruguay;
                }
                else if(this.instance_select == "Canada")
                {
                    plain_map = plain_map_Canada;
                }

                var plain_map_plotly =
                    {
                        text: plain_map[0],
                        x: plain_map[1],
                        y: plain_map[2],
                        mode: 'markers',
                        type: 'scatter',
                    };

                Plotly.newPlot(   $(".figure.map")[0], [plain_map_plotly], {}, {responsive: true}   );
                // 重绘experiment ------------------------------------------------------------------------------

                // 重绘evolution -------------------------------------------------------------------------------

                // 重绘generation ------------------------------------------------------------------------------

                // 重绘individual ------------------------------------------------------------------------------

            },
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

var plain_map_WesternSahara = parseCoords(WesternSahara);
var plain_map_Uruguay = parseCoords(Uruguay);
var plain_map_Canada = parseCoords(Canada);




//
