import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

men = 400000
women = 400000
zombies = 1000  
deaths = 0
resources = 1000000

# SEIR model parameters
exposed = 0
recovered = 0
infection_rate = 0.01
exposure_duration = 14
recovery_duration = 21

# Science group parameters
science_group_size = 1000
antidote_chance = 0.001
wipeout_chance = 0.01

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

x = [0]  # Time
population = [men + women + zombies + deaths]  # Total population
men_population = [men]  # Men population
women_population = [women]  # Women population
zombies_population = [zombies]  # Zombie population
deaths_population = [deaths]  # Death population
resources_available = [resources]  # Available resources
exposed_population = [exposed]  # Exposed population
recovered_population = [recovered]  # Recovered population
science_group_population = [science_group_size]  # Science group population

plt.xlim(0, len(x) + 100)  # Set initial x-axis limit
plt.ylim(0, men + women + zombies + deaths * 1.1)  # Set initial y-axis limit based on population

plt.xlabel('Time')
plt.ylabel('Population/Resources')

plt.title('Zombie Virus Spread')

men_line, = ax1.plot(x, men_population, label='Men')
women_line, = ax1.plot(x, women_population, label='Women')
zombies_line, = ax1.plot(x, zombies_population, label='Zombies')
deaths_line, = ax1.plot(x, deaths_population, label='Deaths')
resources_line, = ax1.plot(x, resources_available, label='Resources')
exposed_line, = ax1.plot(x, exposed_population, label='Exposed')
recovered_line, = ax1.plot(x, recovered_population, label='Recovered')
science_group_line, = ax1.plot(x, science_group_population, label='Science Group')

def update_population():
    global men, women, zombies, deaths, resources, exposed, recovered, science_group_size

    # SEIR model update
    new_exposed = min(int(infection_rate * (men + women + zombies)), men + women - exposed)
    new_recovered = min(int(recovered / recovery_duration), exposed)

    exposed += new_exposed
    recovered += new_recovered

    men -= new_exposed
    women -= new_exposed

    exposed -= new_recovered

    # Zombie infection or death
    zombie_infection_rate = 0.01 + (zombies / (men + women + zombies))
    for _ in range(men):
        if random.uniform(0, 1) < zombie_infection_rate:
            deaths += 1
            men -= 1

    for _ in range(women):
        if random.uniform(0, 1) < zombie_infection_rate:
            deaths += 1
            women -= 1

    # Repopulation and natural deaths
    repopulation_chance = min((men + women) / (men + women + zombies + deaths), 0.01)
    if random.uniform(0, 1) < repopulation_chance:
        new_babies = random.randint(0, 10)
        men += new_babies
        women += new_babies

    deaths_chance = random.uniform(0, 1)
    if deaths_chance < 0.01:  # 1% chance of deaths each time step
        deaths += random.randint(0, 10)

    # Decay of zombies
    zombies_decay = random.randint(0, 10)
    zombies = max(zombies - zombies_decay, 0)

    # Resource management
    resource_usage = random.randint(0, 100)
    resources -= resource_usage

    # Starvation
    if resources < 0:
        starvation = random.uniform(0, 1)
        if starvation < 0.7:  # 1% chance of starvation for each individual
            starved = random.randint(0, men + women)
            men -= starved
            women -= starved

    # Science group actions
    if science_group_size > 0:
        if random.uniform(0, 1) < antidote_chance:
            # Science group develops antidote
            print('Antidote developed!')
            zombies -= random.randint(0, zombies)
            science_group_size -= random.randint(0, 100)

        if random.uniform(0, 1) < wipeout_chance:
            # Science group gets wiped out
            science_group_size = 0

    # Adjust repopulation based on the number of men and women
    repopulation_chance = min((men + women) / (men + women + zombies + deaths), 0.01)
    if random.uniform(0, 1) < repopulation_chance:
        new_babies = random.randint(0, 10)
        men += new_babies
        women += new_babies

def animate(i):
    update_population()

    x.append(i)
    population.append(men + women + zombies + deaths)
    men_population.append(men)
    women_population.append(women)
    zombies_population.append(zombies)
    deaths_population.append(deaths)
    resources_available.append(resources)
    exposed_population.append(exposed)
    recovered_population.append(recovered)
    science_group_population.append(science_group_size)

    men_line.set_data(x, men_population)
    women_line.set_data(x, women_population)
    zombies_line.set_data(x, zombies_population)
    deaths_line.set_data(x, deaths_population)
    resources_line.set_data(x, resources_available)
    exposed_line.set_data(x, exposed_population)
    recovered_line.set_data(x, recovered_population)
    science_group_line.set_data(x, science_group_population)

    # Adjust the x-axis limit dynamically
    ax1.set_xlim(0, len(x) + 100)

    ax1.set_ylim(0, max(population + resources_available) * 1.1)

    # Stop animation if either humans or zombies die out
    if men + women == 0 or zombies == 0:
        ani.event_source.stop()

    print("Time: {}\tMen: {}\tWomen: {}\tZombies: {}\tDeaths: {}\tResources: {}\tExposed: {}\tRecovered: {}\tScience Group: {}".format(i, men, women, zombies, deaths, resources, exposed, recovered, science_group_size))

    return men_line, women_line, zombies_line, deaths_line, resources_line, exposed_line, recovered_line, science_group_line

ani = animation.FuncAnimation(fig, animate, interval=100, blit=True)

plt.legend()
plt.show()
