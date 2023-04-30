# Import the necessary libraries
import os
import matplotlib.pyplot as plt
# Define directory path for each of the simulated environment log files 
h = '/Users/minakabki/Desktop/Dissertation-work'
h1 = '/Users/minakabki/Desktop/Dissertation-work/Het1Logfile/REvoSim_output'
h2 = '/Users/minakabki/Desktop/Dissertation-work/Het2Logfile/REvoSim_output'
h3 = '/Users/minakabki/Desktop/Dissertation-work/Het3Logfile/REvoSim_output'
h4 = '/Users/minakabki/Desktop/Dissertation-work/Het4Logfile/REvoSim_output'
h5 = '/Users/minakabki/Desktop/Dissertation-work/Het5Logfile/REvoSim_output'

nh = '/Users/minakabki/Desktop/Dissertation-work'
nh1 = '/Users/minakabki/Desktop/Dissertation-work/NonHet1Logfile/REvoSim_output'
nh2 = '/Users/minakabki/Desktop/Dissertation-work/NonHet2Logfile/REvoSim_output'
nh3 = '/Users/minakabki/Desktop/Dissertation-work/NonHet3Logfile/REvoSim_output'
nh4 = '/Users/minakabki/Desktop/Dissertation-work/NonHet4Logfile/REvoSim_output'
nh5 = '/Users/minakabki/Desktop/Dissertation-work/NonHet5Logfile/REvoSim_output'

# Define parent directories for the two categories of environments (het and non-het)
parentDirectory = {
    'Heterogeneous': [h1, h2, h3, h4, h5],
    'Non-Heterogeneous': [nh1, nh2, nh3, nh4, nh5],
}
# Define a dictionary to hold the results 
result = {
    'Heterogeneous': [],
    'Non-Heterogeneous': [],
}
# Loop through the directories
for eachDir in parentDirectory:
    currentDir = parentDirectory[eachDir]

    for child in currentDir:
        childDir = os.fsencode(child)

        for file in os.listdir(childDir):
            myfile = file.decode('utf-8')

            # To get the correct logfile (not the end run log files): If the file doesnt contain 'end' in its name and ends with '.txt'
            # it is read and the number of living digital organisms is extracted 
            if 'end' not in myfile and myfile.endswith('.txt'):
                with open(child + '/' + myfile, encoding='utf8') as f:
                    shouldGetNumberOfLivingDigitalOrganisms = False
                    for line in f:
                        line = line.strip()

                        # If the current iteration is the one where the number of living digital organisms is desired
                        # the flag is set to True

                        if line.startswith("[I]"):
                            eachIteratioNumber = line.split(' ')[1]
                            if int(eachIteratioNumber) == int('10099'):
                                shouldGetNumberOfLivingDigitalOrganisms = True
                            else:
                                shouldGetNumberOfLivingDigitalOrganisms = False
                        elif line.startswith("[P]"):
                            # If the flag is True, the number of living digital organisms is extracted and stored in the result dictionary
                            if shouldGetNumberOfLivingDigitalOrganisms == True:
                                try:
                                    eachPopulationGridData = line.split(' ')[1]
                                    NumberOfLivingDigitalOrganisms = eachPopulationGridData.split(',')[4]
                                    result[eachDir].append(int(NumberOfLivingDigitalOrganisms))
                                except Exception as e:
                                    print('error', e)
                                    print('line',line.split(' '))

# Calculate the average number of species for each environment
hetAvg = sum(result['Heterogeneous']) / len(result['Heterogeneous'])
nonHetAvg = sum(result['Non-Heterogeneous']) / len(result['Non-Heterogeneous'])

# Create a list of data and labels for the bar chart
data = list((hetAvg, nonHetAvg))
labels = ['Heterogeneous', 'Non-Heterogeneous']

# Plot bar chart with combined data
plt.bar(labels, data, color=['purple', 'purple'], width=0.3)
plt.title('Species Richness in Heterogeneous and Non-Heterogeneous Environments After Mass Extinction Event')
plt.xlabel('Environment')
plt.ylabel('Number of Species ')
plt.show()