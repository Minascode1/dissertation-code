import matplotlib.pyplot as plt
import numpy as np 

# Create empty lists to store data read from the input file
time_points = []
num_species = []

# Open the input file for reading
with open('./Dissertation-work/NonHet2LogFile/REvoSim_output/REvoSim_log_run_0031.txt', encoding='utf8') as f:
    # Read the file line by line
    for line in f: 
        # Strip leading and trailing whitespaces from the line
        line = line.strip()
        
        # Check if the line contains information about the iteration number
        if line.startswith("[I]"):
            # Extract the iteration number and convert it to a float
            eachIteratioNumber = line.split(' ')[1]
            time_points.append(float(eachIteratioNumber))
        
        # Check if the line contains information about the population grid data
        elif line.startswith("[P]"):
            # Extract the relevant data and convert the number of species to a float
            eachPopulationGridData = line.split(' ')[1]
            numberOfSpecies = eachPopulationGridData.split(',')[4]
            num_species.append(float(numberOfSpecies))

# Create a plot using matplotlib
plt.plot(time_points, num_species, color='plum')

# Set the labels and title for the plot
plt.xlabel('Time (Iterations Number)')
plt.ylabel('Number of Species')
plt.title('Assessing the Resilience of Species Diversity: Pre- and Post-Extinction Analysis and Recovery Rates')

# Display the plot on the screen
plt.show()