import pandas as pd
import numpy as np

# Which continent has the most countries in the data?
def get_most_freq_continent(df: pd.DataFrame) -> dict[str, any]:
    continent_counts = df["continent"].value_counts()
    max_continent_value = continent_counts.max()
    max_continent_name = continent_counts.idxmax()
    answer = {"name": max_continent_name, "value": max_continent_value}
    return answer
    
    
    


# # Which region has the largest combined area in sq. km?
# def get_biggest_km_region():

# # Which country has the highest life expectancy?
# def get_highest_lifeExp():

# # Which subregion has the lowest / highest average GDP per capita?
# def get_gdp_range():


