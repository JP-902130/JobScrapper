import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
from IPython.display import display


def graphCountryAsBarDiagram(df):
    plt.figure(figsize=(8, 6))
    fig = sns.countplot(x="Country/State",
                        data=df, order=pd.value_counts(df['Country/State']).iloc[:10].index, palette='viridis')
    fig.figure.savefig("out.png")
    return


def graphCityAsBarDiagram(df):
    plt.figure(figsize=(8, 6))
    fig = sns.countplot(x="City",
                        data=df, order=pd.value_counts(df['City']).iloc[:10].index, palette='viridis')
    fig.set_xticklabels(fig.get_xticklabels(), rotation=20, ha="right")
    fig.figure.savefig("out.png")
    return


def graphSalaryDistribution(df):
    fig = sns.distplot(df['Salary'])
    fig.figure.savefig("out.png")
    return


def graphAverageSalaryForEachState(df):
    newDF = df.groupby('Country/State')
    newDF.filter(lambda x: len(x) > 5)
    display(newDF)
    # display(dfWithOnlySufficientData)
    # newDF.sort_values(by=['Salary'], inplace=True)
    # display(newDF)
