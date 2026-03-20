import pandas as pd

# Create an interface that allows users to filter down to a subset of the data 
# (E.g. filter by Continent, region, subregion, type, or some combination thereof). 
# Users should then be able to see summary statistics for each of the area_km2, pop, lifeExp and gdpPercap columns

def filter_data(
    df: pd.DataFrame,
    continent: str | None = None,
    region: str | None = None,
    subregion: str | None = None,
    country_type: str | None = None
) -> pd.DataFrame:
    
    filtered_df = df.copy()
  
    if continent:
        filtered_df = filtered_df[filtered_df["continent"].str.lower() == continent.lower()]

    if region:
        filtered_df = filtered_df[filtered_df["region_un"].str.lower() == region.lower()]

    if subregion:
        filtered_df = filtered_df[filtered_df["subregion"].str.lower() == subregion.lower()]

    if country_type:
        filtered_df = filtered_df[filtered_df["type"].str.lower() == country_type.lower()]

    return filtered_df



