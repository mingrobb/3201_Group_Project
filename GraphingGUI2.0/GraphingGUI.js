var content = new Vue
(
    {
        el: '#content',
        data:
        {
            show_dashboard: true,
            x_style_page: "width: calc(100% - 400px);",
            generation_n: 10,
            individual_n: 3,
        },
        methods:
        {
            toggleDashboard: function()
            {
                if(this.show_dashboard==true)
                {   this.x_style_page = "width: initial;";
                    this.show_dashboard = false;
                }
                else
                {   this.x_style_page = "width: calc(100% - 400px);";
                    this.show_dashboard = true;
                }
            }
        },
    }
);
