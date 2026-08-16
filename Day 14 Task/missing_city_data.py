import pandas as pd

cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000,
    "Chennai": 1500000
}

required_cities = ["Delhi", "Chennai", "Bangalore"]

S = pd.Series(cities, index=required_cities)

print(S)

print("\nCities with missing values:")
print(S[S.isna()])