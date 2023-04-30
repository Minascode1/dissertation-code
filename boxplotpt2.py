import pandas as pd


# Read in the data from the log files
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

log_files = {'Heterogeneous': [h1, h2, h3, h4, h5],
    'Non-Heterogeneous': [nh1, nh2, nh3, nh4, nh5],
    }

data = {'Heterogeneous': [],
    'Non-Heterogeneous': [],
    }

for file in log_files:
    df = np.read_csv(file, delimiter='\t')
    data[file] = df[(df['Iteration Number'] >= 8099) & (df['Iteration Number'] <= 10049)]

# Calculate the mean number of species for each log file
mean_species = {}

for file in log_files:
    mean_species[file] = data[file]['Number of Species'].mean()

# Calculate the recovery time for each log file
recovery_time = {}

for file in log_files:
    for i in range(len(data[file])):
        if data[file]['Number of Species'].iloc[i] < mean_species[file]:
            continue
        else:
            start_time = data[file]['Iteration Number'].iloc[i]
            break
    for j in range(i, len(data[file])):
        if data[file]['species'].iloc[j] >= 0.75*mean_species[file]:
            end_time = data[file]['time'].iloc[j]
            break
    recovery_time[file] = end_time - start_time

# Print the results
for file in log_files:
    print('File:', file)
    print('Mean number of species:', mean_species[file])
    print('Recovery time:', recovery_time[file])
