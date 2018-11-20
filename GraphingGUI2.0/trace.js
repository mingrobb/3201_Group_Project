/*
    for example, for
        population size = 100
        total generations = 50
    the data structure is:

        info:
            {
                name: String,
                num_of_cities: integer,
            },
        generation 0:
            {
                lowest_fitness: float,
                average_fitness: float,
                highest_fitness: float,
                individual 1:
                    {
                        fitness: float,
                        total_distance: integer,
                        route: [the city ids sequence]
                    }
                individual 2:
                    {
                        ...
                    }
                individual 3:
                    {
                        ...
                    }
                .
                .
                .
                individual 100:
                    {
                        ...
                    }
            },
        generation 1:
            {
                ...
            },
        generation 2:
            {
                ...
            },
        .
        .
        .
        generation 50:
            {
                ...
            },

    NOTE:
        1.The fitness could actually be computed from distance, but formally it should be provided in the data file.
        2.The individuals sorted by their fitness in descent order.
        3.Please output the generation history to a text file named trace.js
            this is a json file so I can directly make use of it.
*/




var trace =
{
    info:
        {
            name: "WesternSahara",
            num_of_cities: 29,
        },
    "0":
        {
            lowest_fitness: 0.123455,
            average_fitness: 0.267183,
            highest_fitness: 0.356551,
            "1":
                {
                    fitness: 1/243542,
                    total_distance: 243542,
                    route: [1, 3, 8, 4, 5, 2, 6, 9, 7, 10],
                },
            "2":
                {
                    fitness: 1/243542,
                    total_distance: 243542,
                    route: [1, 3, 8, 4, 5, 2, 6, 9, 7, 10],
                },
            "3":
                {
                    fitness: 1/243542,
                    total_distance: 243542,
                    route: [1, 3, 8, 4, 5, 2, 6, 9, 7, 10],
                },
            /*
            .
            .
            .
            */
            "100":
                {
                    fitness: 1/243542,
                    total_distance: 243542,
                    route: [1, 3, 8, 4, 5, 2, 6, 9, 7, 10],
                },
        },
    "1":
        {
            //...
        },
    "2":
        {
            //...
        },
    /*
    .
    .
    .
    */
    "50":
        {
            //...
        },
};
