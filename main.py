import matplotlib.pyplot as plt
import pandas as pd
import exercici_1
import exercici_2


# Exercici 1
print("Exercici 1")
exercici_1.function1()
# Exercici 2
print("Exercici 2")
exercici_2.function2()

def grafica():

    print('Imprimimos la grafica 1: ')
    data = pd.read_csv("data.csv", usecols=['NAME','NOTES','YEAR'])
    data = data.dropna()
    data = data.groupby(by='NAME').mean('NOTES')
    data = pd.DataFrame(data, columns=['NAME', 'NOTES'])
    colors = ["blue"]
    name = data.pop("NAME")
    notes = data.pop("NOTES")
    plt.bar(notes, name, width=0.4 , color=colors)
    plt.set_ylabel('NOTES')
    plt.set_title('ALUMNAT')
    plt.legend(title='Guillem Jimenez')
    plt.show()


    print('Imprimimos la grafica 2: ')
    data = pd.read_csv("data.csv", usecols=['NAME','GROUP','MODULE','ABSENCES'])
    data = data.dropna()
    plt.set_ylabel('Faltes en %')
    plt.set_title('ALUMNAT')
    plt.legend(title='% de faltes DAW2')
    plt.show()

grafica()