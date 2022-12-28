
def addCityAndCountryToRawDF(rowDF):
    def cityFilter(x):
        return x.split("-")[0].split(",")[0].strip()

    def countryFilter(x):
        try:
            return x.split("-")[0].split(",")[1].strip()
        except:
            return "Remote"
    citySeries = rowDF["Location"].apply(cityFilter)
    countrySeries = rowDF["Location"].apply(countryFilter)
    rowDF["City"] = citySeries
    rowDF["Country/State"] = countrySeries
    return rowDF
