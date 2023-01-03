import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv("dataset3.csv"))
print(data)

concepts=np.array(data.iloc[:,0:-1])
print(concepts)

target = np.array(data.iloc[:,-1])
print(target)

def learn(concepts, target):
    print('Most Specific Hypothesis:\n')
    specific_h = ["@" for i in range(6)]
    print(specific_h)
    for i in range(len(target)):
        if target[i] == 'Yes':
            specific_h = concepts[i].copy()
            break

    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]

    print('\nMost General Hypothesis:\n')
    for g in general_h:
         print(g)
    for i, h in enumerate(concepts):

        print('\nExample', i, ': ', h, ' Target:', target[i])
        if target[i] == "Yes":
            for x in range(len(specific_h)):

                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        if target[i] == "No":
            for x in range(len(specific_h)):

                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'



        print('S:\n', specific_h)
        print('G:')
        for g in general_h:
            print(g)

    indices = [i for i, val in enumerate(general_h)
           if val == ['?', '?', '?', '?', '?', '?']]
    print(indices)

    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])

    return specific_h, general_h
s_final= learn(concepts, target)
g_final = learn(concepts, target)
print("Final S", s_final, sep="\n")
print("Final G:\n")
for g in g_final:
    print(g)
