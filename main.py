import pandas as pd
import numpy as np

def main():
    print("=== World Data Analysis Tool ===")
    while True:

 
        print("\nMenu:")
        print("1. Load and clean data")
        print("2. Answer analysis questions")
        print("3. Exit")

        choice = input("Select an option: ")

        # 3. Exit
        if choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()