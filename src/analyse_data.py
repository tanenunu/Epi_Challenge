import pandas as pd

# Which continent has the most countries in the data?
def get_most_freq_continent(df: pd.DataFrame) -> dict[str, any]:
    continent_counts = df["continent"].value_counts()
    max_continent_value = continent_counts.max()
    max_continent_name = continent_counts.idxmax()
    answer = {"name": max_continent_name, "value": max_continent_value}
    return answer
    

# # Which region has the largest combined area in sq. km?
def get_biggest_km_region(df: pd.DataFrame) -> dict[str, any]:
    region_areas = df.groupby("region_un")["area_km2"].sum()
    largest_region_name = region_areas.idxmax()
    largest_region_val = region_areas.max()

    answer = {"name": largest_region_name, "value": largest_region_val}
    return answer

# # Which country has the highest life expectancy?
def get_highest_lifeExp(df: pd.DataFrame) -> dict[str, any]:
    world_lifeExp = df.groupby("name_long")["lifeExp"].sum()
    
    name = world_lifeExp.idxmax()
    value = world_lifeExp.max()

    answer = {"name": name, "value": value}
    return answer


# # Which subregion has the lowest / highest average GDP per capita?
def get_highest_gdp(df: pd.DataFrame):
    subregion_gdp = df.groupby("subregion")["gdpPercap"].mean()
    subregion_gdp.dropna(inplace=True)

    max_gdp_value = subregion_gdp.max()
    max_gdp_name = subregion_gdp.idxmax()

    answer = {"name": max_gdp_name, "value": max_gdp_value}
    return answer

def get_lowest_gdp(df: pd.DataFrame):
    subregion_gdp = df.groupby("subregion")["gdpPercap"].mean()
    subregion_gdp.dropna(inplace=True)

    min_gdp_value = subregion_gdp.min()
    min_gdp_name = subregion_gdp.idxmin()

    answer = {"name": min_gdp_name, "value": min_gdp_value}
    return answer


def print_full_analysis(df: pd.DataFrame):
    # Question 1: Most frequent Continent
    result = get_most_freq_continent(df)
    print(f"\nWhich Continent has the most countries in the data?")
    print(f"Answer:\n       {result["name"]}\n       Countries: {result["value"]}")

    # Question 2: Biggest km^2
    result = get_biggest_km_region(df)
    print(f"\nWhich region has the largest combined area in sq. km?")
    print(f"Answer:\n       {result["name"]}\n       Combined km^2: {result["value"]}")

    # Question 3: Highest lifeExp
    result = get_highest_lifeExp(df)
    print(f"\nWhich country has the highest life expectancy?")
    print(f"Answer:\n       {result["name"]}\n       Life expectancy: {result["value"]}")

    # Question 4: Highest/Lowest GDP
    print(f"\nWhich subregion has the lowest / highest average GDP per capita?")
    print(f"Answer:")
    
    result = get_highest_gdp(df)
    print(f"       Highest GDP: {result["name"]}\n                    {result["value"]} gdp per capita")

    result = get_lowest_gdp(df)
    print(f"       Lowest GDP: {result["name"]}\n                   {result["value"]} gdp per capita")







