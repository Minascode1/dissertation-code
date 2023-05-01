# Import the necessary libraries
import os
import matplotlib.pyplot as plt
import json
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
    'Heterogeneous': {},
    'Non-Heterogeneous': {},
}

finalResult = {
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
                    shouldGetNumberOfSpecies = False
                    for line in f:
                        line = line.strip()

                        # If the current iteration is the one where the number of living digital organisms is desired
                        # the flag is set to True

                        if line.startswith("[I]"):
                            eachIteratioNumber = line.split(' ')[1]
                            if int(eachIteratioNumber) >= int('8049') and int(eachIteratioNumber) < int('10049'):
                                shouldGetNumberOfSpecies = True
                            else:
                                shouldGetNumberOfSpecies = False
                        elif line.startswith("[P]"):
                            # If the flag is True, the number of living digital organisms is extracted and stored in the result dictionary
                            if shouldGetNumberOfSpecies == True:
                                try:
                                    eachPopulationGridData = line.split(' ')[1]
                                    NumberOfSpecies = eachPopulationGridData.split(',')[4]
                                    
                                    if myfile in result[eachDir]:
                                        result[eachDir][myfile].append(int(NumberOfSpecies))
                                    else:
                                        result[eachDir][myfile] = []
                                        result[eachDir][myfile].append(int(NumberOfSpecies))
                                   
                                except Exception as e:
                                    print('error', e)
                                    print('line',line.split(' '))
    print('Working on: ', eachDir)


for eachResult in result:
    currentResult = result[eachResult]
    for eachFile in currentResult:
        numberOfSpeciesList = currentResult[eachFile]
        finalResult[eachResult].append((0.75) * (sum(numberOfSpeciesList) / len(numberOfSpeciesList)))

with open('./finalResult.json', 'w') as f:
    # write the object to the file as a JSON string using json.dump()
    json.dump(finalResult, f)

print(finalResult['Heterogeneous'])

# # Create a list of data and labels for the bar chart
# data = list((iterationsListForHet, iterationsListForNonHet))
# labels = ['Heterogeneous', 'Non-Heterogeneous']

# # Plot bar chart with combined data
# # Create a figure and axis object
# fig, ax = plt.subplots()

# # Create the box plot
# ax.boxplot([iterationsListForHet, iterationsListForNonHet], labels=['Heterogeneous', 'Non-Heterogeneous'])

# # Set the y-axis label
# ax.set_ylabel('Species Recovery Rate')

# # Show the plot
# plt.show()