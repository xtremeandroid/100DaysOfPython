travel_log = [
    {
    "country" : "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon4"]
    },
    {
    "country" : "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },    
]

#write function to add to travel log
def add_new_country(countryName, noOfVisits, visitedCities):
    travel_log.append(
        {
        "country" : countryName,
        "visits": noOfVisits,
        "cities": visitedCities
        }
    )


add_new_country("Russia",2,["Moscow", "Saint"])
print(travel_log)