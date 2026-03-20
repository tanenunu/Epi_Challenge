import pandas as pd
import numpy as np
from src.load_data import load_worldData
from src.clean_data import clean_data
from src.analyse_data import get_most_freq_continent

def main():
    df = pd.DataFrame()
    clean_df = pd.DataFrame()

    print("=== World Data Analysis Tool ===")
    while True:
        print("\nMenu:")
        print("1. Load and clean data")
        print("2. Answer analysis questions")
        print("3. Exit")

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
                result = get_most_freq_continent(clean_df)
                print(f"{result["name"]} {result["value"]}")
                
                #print(clean_df.to_string())
           
        # 3. Exit
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()