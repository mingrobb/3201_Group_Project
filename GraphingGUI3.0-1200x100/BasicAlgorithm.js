var basic_algorithm =
{
    description:
    {
        name: "WesternSahara",
        num_of_cities: 29,
        population_size: 100,
        total_generations: 50,
    },
    evolution:
    {
        generation 0:
        {
            statistics:
            {
                lowest_fitness: 0.123455,
                average_fitness: 0.267183,
                highest_fitness: 0.356551,
                shortest_distance: 1225235238,
                average_distance: 3251689492,
                longest_distance: 8965683221,
            },
            individuals:
            {
                individual 1:
                {
                    fitness: 1/243542,
                    total_distance: 243542,
                    route: [1, 3, 8, 4, 5, 2, 6, 9, 7, 10],
                },
                individual 2:
                {
                    ...
                },
                individual 3:
                {
                    ...
                },
                .
                .
                .
                individual 100:
                {
                    ...
                },
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
    },
}
