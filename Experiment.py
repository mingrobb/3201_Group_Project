class Experiment(object):

    def __init__(self):

        self.description = {
            instance_name: "none",
            algorithm: "none",
            city_all: 0,
            generation_all: 0
        }

        self.trials = {
            stat: {
                time_cost: 0,
                final_fitness: 0,
                final_distance: 0
            },

            evolutions: []

        }