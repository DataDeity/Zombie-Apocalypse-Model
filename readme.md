# Simulation of Zombie Virus Spread

This code is a simulation of the spread of a zombie virus in a population. It utilizes the SEIR (Susceptible-Exposed-Infected-Recovered) model to simulate the dynamics of the virus spread. The simulation is visualized using the matplotlib library in Python.

## Required Libraries
The code relies on the following Python libraries:

- matplotlib.pyplot: Used to create plots and visualize the simulation.
- matplotlib.animation: Used to animate the plots.
- numpy: Used for numerical calculations and array manipulation.
- random: Used to generate random numbers.

Make sure these libraries are installed in the Python environment where the code is being run.

## Simulation Parameters
The simulation has several parameters that can be adjusted to control the behavior of the virus spread and other aspects of the simulation. The parameters and their initial values are as follows:

- men: Initial number of men in the population.
- women: Initial number of women in the population.
- zombies: Initial number of zombies in the population.
- deaths: Initial number of deaths in the population.
- resources: Initial number of available resources.
- exposed: Initial number of individuals exposed to the virus.
- recovered: Initial number of individuals who have recovered from the virus.
- infection_rate: Rate at which the virus spreads from infected individuals to susceptible individuals.
- exposure_duration: Duration of the exposure period to the virus.
- recovery_duration: Duration of the recovery period from the virus.
- science_group_size: Size of a science group working on finding a cure for the virus.
- antidote_chance: Chance of the science group developing a cure.
- wipeout_chance: Chance of the science group being wiped out.

These parameters can be adjusted to explore different scenarios and observe the effects on the virus spread.

## Plot Initialization
The code initializes a plot using matplotlib.pyplot. It creates a figure and adds a single subplot to it. The X-axis represents time, and the Y-axis represents population/resources. The plot will display multiple lines representing different population groups and resource levels over time.

The initial limits for the X-axis and Y-axis are set based on the initial population values.

## Population Data Initialization
The code initializes lists to store population and resource data over time. These lists are used to update the plot during the animation. The initial values for the population data are added to their respective lists.

## Plot Lines
The code creates several plot lines that will display the population and resource data on the plot. Each line is associated with a specific data list.

## Population Update
The `update_population()` function is called in each animation round to update the population based on specific rules and models. The function includes the following logic:

- SEIR model update: Calculates the number of new exposed and new recovered based on the infection rate and recovery duration. Also updates the exposed and recovered populations and subtracts the number of new exposed from the men and women populations.

- Zombie infection and death: Calculates the infection rate for zombies and checks if each person becomes infected. If a person gets infected, deaths increase, and the number of men or women decreases.

- Repopulation and natural deaths: Calculates the probability of repopulation based on the number of men, women, zombies, and deaths. If the chance of repopulation occurs, newborn babies are added to the men and women populations. Also calculates the probability of natural deaths and increases deaths by a random amount.

- Zombie decay: Subtracts a random number of zombies to simulate decay.

- Resource management: Subtracts a random number of resources to simulate consumption.

- Starvation: If resources fall below zero, checks for starvation for each individual. If starvation occurs, the number of men and women decreases.

- Actions from the science group: If the science group is present, checks if

 they develop a cure or get wiped out based on given chances.

- Adjusting repopulation based on the number of men and women: Calculates the probability of repopulation again and adds newborn babies if the chance occurs.

## Animation Function
The `animate()` function is an animation callback function that updates the plot in each round. It calls the `update_population()` function to update the population and resource values. Then it adds the updated values to their respective lists for plotting. Finally, it updates the plot lines with the new data.

The function also dynamically adjusts the limits for the X-axis and Y-axis based on the current data.

The animation stops if either all humans or zombies die out.

## Starting the Animation
The code creates an animation object using `animation.FuncAnimation()` and specifies the `animate()` function to be called in each round. The interval between each round is set to 100 milliseconds. The animation is displayed using `plt.show()`.

## Conclusion
This code implements a simulation of the spread of a zombie virus using the SEIR model. It displays population changes over time and provides a visual representation of the virus spread. By adjusting the parameters, you can explore different scenarios and observe the consequences of changes in the spread rate, recovery duration, and other factors.
