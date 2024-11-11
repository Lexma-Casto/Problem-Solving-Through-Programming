"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import tui
import process
import visual
import os
from process import DataExporter


def main():
    tui.display_welcome()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data = process.load_data(os.path.join(base_dir, 'data', 'disneyland_reviews.csv'))
    print(f"Dataset loaded successfully with {len(data)} rows.")

    while True:
        user_choice = tui.display_main_menu()
        if user_choice == 'A':
            handle_view_data(data)
        elif user_choice == 'B':
            handle_visualize_data(data)
        elif user_choice == 'C':
            handle_export_data(data)
        elif user_choice == 'X':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again !")


def handle_view_data(data):
    submenu_choice = tui.display_view_data_menu()
    if submenu_choice == 'A':
        park = input("Enter park name: ")
        process.view_reviews_by_park(data, park)
    elif submenu_choice == 'B':
        park = input("Enter park name: ")
        location = input("Enter reviewer location: ")
        process.count_reviews_by_park_location(data, park, location)
    elif submenu_choice == 'C':
        park = input("Enter park name: ")
        year = input("Enter year: ")
        process.average_score_by_year(data, park, year)
    elif submenu_choice == 'D':
        process.average_score_by_location(data)
    else:
        print("Invalid choice !")


def handle_visualize_data(data):
    submenu_choice = tui.display_visualize_data_menu()
    if submenu_choice == 'A':
        visual.most_reviewed_parks(data)
    elif submenu_choice == 'B':
        visual.average_scores(data)
    elif submenu_choice == 'C':
        park = input("Enter park name: ")
        visual.park_ranking_by_nationality(data, park)
    elif submenu_choice == 'D':
        park = input("Enter park name: ")
        visual.most_popular_month_by_park(data, park)
    else:
        print("Invalid choice !")


def handle_export_data(data):
    print("\nExport Data Sub-Menu")
    print("Choose a park to export data for:")
    park = input("Enter park name: ")
    print("\nChoose export format:")
    print("1. CSV")
    print("2. TXT")
    print("3. JSON")

    format_choice = input("Enter format choice (1/2/3): ")

    # Create an exporter instance
    exporter = DataExporter(data)

    # Call the export_data method based on user choice
    if format_choice == '1':
        exporter.export_data(park, 'csv')
    elif format_choice == '2':
        exporter.export_data(park, 'txt')
    elif format_choice == '3':
        exporter.export_data(park, 'json')
    else:
        print("Invalid choice. Returning to main menu.")


if __name__ == "__main__":
    main()




#