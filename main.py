import pandas as pd
import numpy as np
from src.load_data import load_worldData
from src.clean_data import clean_data
from src.analyse_data import print_full_analysis
from src.filter_data import filter_data


def main():
    df = pd.DataFrame()
    clean_df = pd.DataFrame()

    print("\n====== World Data Analysis Tool ======")
    while True:
        if(clean_df.empty):
            print("❌Data not loaded to memory. Select option 1. to load.")

        else:
            print("✅Data loaded.")
        print("\n======= Menu =======")
        print("1. Load and clean data")
        print("2. Answer analysis questions")
        print("3. Filter and Summarise")
        print("4. Export Cleaned Data to CSV file")
        print("5. Exit")
        print()

        choice = input("Select an option: ")
        
        # 1. Load & clean Data
        if choice == "1":
            df = load_worldData()
            clean_df = clean_data(df)
        
        # 2. Analysis questions
        elif choice == "2":
            if clean_df.empty:
                print("⚠️ Please load and clean data first.")
            else: 
                print("Data is loaded and clean.")
                print_full_analysis(clean_df)
        
        # 3. Filter Data and Summarise Stats
        elif choice == "3":
            if clean_df.empty:
                print("⚠️ Please load and clean data first.")
            else:
                print("\n ===== Filter Selection =====:")
                print("Choose Filter:")
                print("1. Continent")
                print("2. Region")
                print("3. Sub Region")
                print("4. Country Type")
                filter_choice = input("Select an option: ")
        
                filtered_df = pd.DataFrame()
    
                # Filter by Continent:
                if filter_choice == "1":
                    user_input = input("Enter Continent: ")
                    filtered_df = filter_data(df=clean_df, continent=user_input)

                # Filter by Region:
                elif filter_choice == "2":
                    user_input = input("Enter Region: ")
                    filtered_df = filter_data(df=clean_df, region=user_input)

                # Filter by Sub Region:
                elif filter_choice == "3":
                    user_input = input("Enter Sub Region: ")
                    filtered_df = filter_data(df=clean_df, subregion=user_input)

                # Filter by Type:
                elif filter_choice == "4":
                    user_input = input("Enter Country Type: ")
                    filtered_df = filter_data(df=clean_df, country_type=user_input)

                else:
                    print("Invalid option. Try again.")
                

                # Print summary statistics:
                if filtered_df.empty != True:
                    filtered_df.drop(columns="Unnamed: 0", inplace=True)
                    print(filtered_df.describe().to_string())
                else:
                    print("Invalid option. Try again.")

        # 4. Export Cleaned Data as CSV
        elif choice == "4":
            if clean_df.empty:
                print("⚠️ Please load and clean data first.")
            else: 
                user_input = input("Export cleaned dataset as csv?\n 1. Yes\n 2. No\nSelect Option:  ")
                if user_input == "1":
                    filename = input("Enter filename (default: cleaned_data.csv): ").strip()
            
                    if not filename:
                        filename = "cleaned_data.csv"
            
                    if not filename.endswith(".csv"):
                        filename += ".csv"

                    try:
                        clean_df.to_csv(filename, index=False)
                        print(f"Data successfully exported to {filename}")
                    except Exception as e:
                        print(f"Error exporting file: {e}")

                else:
                    print("Export cancelled.")

                

        # 5. Exit
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()