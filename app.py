
import pandas as pd
from IPython.display import display
import scrap
import dfProcessor
import visualization

# def extractCity(cityCountry):


def main():

    df = pd.read_excel('Jobs.xlsx', sheet_name='Jobs')
    visualization.graphAverageSalaryForEachState(df)
    return 0


main()
