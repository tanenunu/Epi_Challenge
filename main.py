import pandas as pd
import numpy as np
from src.load_data import load_worldData
from src.clean_data import clean_data
from src.analyse_data import print_full_analysis
from src.filter_data import filter_data


def main():
    df = pd.DataFrame()
    clean_df = pd.DataFrame()

    print("=== World Data Analysis Tool ===")
    while True:
        print("\nMenu:")
        print("1. Load and clean data")
        print("2. Answer analysis questions")
        print("3. Filter and Summarise")
        print("4. Exit")
        print()

        if(clean_df.empty):
            print("❌Data not loaded to memory.")
        else:
            print("✅Data loaded.")

        choice = input("Select an option: ")
        

        # 1. Load & clean Data
        if choice == "1":
            df = load_worldData()
            clean_df = clean_data(df)
        
        # 2. Analysis questions
        elif choice == "2":
            if clean_df.empty:
                print("Please load and clean data first.")
            else: 
                print("Data is loaded and clean.")
                print_full_analysis(clean_df)
        
        elif choice == "3":
            print("\n ===== Filter Selection =====:")
            print("Choose Filter:")
            print("1. Continent")
            print("2. Region")
            print("3. Sub Region")
            print("4. Country Type")
            filter_choice = input("Select an option: ")
            
            filtered_df = pd.DataFrame()
            
            # Continent
            if filter_choice == "1":
                user_input = input("Enter Continent: ")
                filtered_df = filter_data(df=clean_df, continent=user_input)
            # Region
            elif filter_choice == "2":
                user_input = input("Enter Region: ")
                filtered_df = filter_data(df=clean_df, region=user_input)
            # Sub Region
            elif filter_choice == "3":
                user_input = input("Enter Sub Region: ")
                filtered_df = filter_data(df=clean_df, subregion=user_input)
            # Type
            elif filter_choice == "4":
                user_input = input("Enter Country Type: ")
                filtered_df = filter_data(df=clean_df, country_type=user_input)
            else:
                print("Invalid option. Try again.")
            
            if filtered_df.empty != True:
                filtered_df.drop(columns="Unnamed: 0", inplace=True)
                print(filtered_df.describe().to_string())
            else:
                print("Invalid option. Try again.")


                
                
           
        # 4. Exit
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()