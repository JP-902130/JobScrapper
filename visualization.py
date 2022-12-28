import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display


def updateAllPlots(df):
    graphAverageSalaryForEachState(df)
    graphCityAsBarDiagram(df)
    graphCountryAsBarDiagram(df)
    graphSalaryDistribution(df)


def graphCountryAsBarDiagram(df):
    plt.figure(figsize=(16, 10))

    fig = sns.countplot(x="Country/State",
                        data=df, order=pd.value_counts(df['Country/State']).iloc[:10].index, palette='viridis')
    plt.title('Number of current openings in each state/country', fontweight='bold',
              color='orange', fontsize='20', horizontalalignment='center')
    plt.xlabel('State/country', fontweight='bold',
               color='black', fontsize='15', horizontalalignment='center')
    plt.ylabel('Number of jobs', fontweight='bold',
               color='black', fontsize='15', verticalalignment='center', labelpad=20)
    fig.figure.savefig("plots/countryVScount.png")
    return


def graphCityAsBarDiagram(df):
    plt.figure(figsize=(16, 10))
    plt.title('Number of current openings in each city', fontweight='bold',
              color='orange', fontsize='20', horizontalalignment='center')
    fig = sns.countplot(x="City",
                        data=df, order=pd.value_counts(df['City']).iloc[:10].index, palette='viridis')
    plt.title('Number of current openings in each city', fontweight='bold',
              color='orange', fontsize='20', horizontalalignment='center')
    plt.xlabel('City', fontweight='bold',
               color='black', fontsize='15', horizontalalignment='center')
    plt.ylabel('Number of jobs', fontweight='bold',
               color='black', fontsize='15', verticalalignment='center', labelpad=20)

    fig.figure.savefig("plots/cityVSCount.png")
    return


def graphSalaryDistribution(df):
    plt.figure(figsize=(16, 10))
    fig = sns.histplot(df['Salary'], kde=True)

    plt.title('Salary distribution', fontweight='bold',
              color='orange', fontsize='20', horizontalalignment='center')
    plt.xlabel('Salary (USD)', fontweight='bold',
               color='black', fontsize='15', horizontalalignment='center')
    plt.ylabel('Number of jobs', fontweight='bold',
               color='black', fontsize='15', verticalalignment='center', labelpad=20)
    fig.figure.savefig("plots/salaryDistribution.png")
    return


def graphAverageSalaryForEachState(df):
    def fun(row):
        if newDF[row["Country/State"]] > 5:
            return True
        else:
            return False
    plt.figure(figsize=(16, 10))
    newDF = df["Country/State"].value_counts()
    newDF2 = df.groupby(
        "Country/State").median(numeric_only=True).reset_index()
    m = newDF2.apply(fun, axis=1)
    newDF2 = newDF2[m]
    newDF2 = newDF2.sort_values(by=['Salary'], ascending=False)
    fig = sns.barplot(x='Country/State', y='Salary',
                      data=newDF2, palette='viridis')

    plt.xlabel('Average salary for each state/country', fontweight='bold',
               color='black', fontsize='15', horizontalalignment='center')
    plt.ylabel('Average hourly salary (USD)', fontweight='bold',
               color='black', fontsize='15', verticalalignment='center', labelpad=20)
    plt.title('State/Country', fontweight='bold',
              color='orange', fontsize='20', horizontalalignment='center')
    fig.figure.savefig("plots/stateVSsalary.png")
