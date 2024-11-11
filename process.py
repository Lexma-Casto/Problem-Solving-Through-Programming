"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv
import json


def load_data(filepath):
    data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def view_reviews_by_park(data, park):
    reviews = [row for row in data if row['Branch'] == park]
    if reviews:
        for review in reviews:
            print(review)
    else:
        print(f"No reviews found for {park}.")


def count_reviews_by_park_location(data, park, location):
    count = sum(1 for row in data if row['Branch'] == park and row['Reviewer_Location'] == location)
    print(f"{park} has {count} reviews from {location}.")


def average_score_by_year(data, park, year):
    scores = [int(row['Rating']) for row in data if row['Branch'] == park and row['Year_Month'].startswith(year)]
    if scores:
        avg_score = sum(scores) / len(scores)
        print(f"Average score for {park} in {year}: {avg_score:.2f}")
    else:
        print(f"No reviews found for {park} in {year}.")


def average_score_by_location(data):
    location_scores = {}
    for row in data:
        location = row['Reviewer_Location']
        score = int(row['Rating'])
        if location in location_scores:
            location_scores[location].append(score)
        else:
            location_scores[location] = [score]

    for location, scores in location_scores.items():
        avg_score = sum(scores) / len(scores)
        print(f"{location}: {avg_score:.2f}")


# ==============================================================================================================================
# Data Exporter class to achieve OOP

class DataExporter:
    def __init__(self, data):
        self.data = data

    def count_reviews(self, park):
        """Count the total number of reviews for a specific park."""
        return sum(1 for row in self.data if row['Branch'] == park)

    def count_positive_reviews(self, park, positive_threshold=4):
        """Count the number of positive reviews (rating >= positive_threshold) for a specific park."""
        return sum(1 for row in self.data if row['Branch'] == park and int(row['Rating']) >= positive_threshold)

    def average_review_score(self, park):
        """Calculate the average review score for a specific park."""
        scores = [int(row['Rating']) for row in self.data if row['Branch'] == park]
        return sum(scores) / len(scores) if scores else 0

    def count_countries_reviewed(self, park):
        """Count the number of unique countries that reviewed a specific park."""
        countries = set(row['Reviewer_Location'] for row in self.data if row['Branch'] == park)
        return len(countries)

    def export_data(self, park, format='csv'):
        """Export data to the specified format (CSV, TXT, or JSON)."""
        reviews_count = self.count_reviews(park)
        positive_reviews_count = self.count_positive_reviews(park)
        avg_score = self.average_review_score(park)
        countries_reviewed = self.count_countries_reviewed(park)

        export_data = {
            'Park': park,
            'Number of Reviews': reviews_count,
            'Number of Positive Reviews': positive_reviews_count,
            'Average Review Score': avg_score,
            'Number of Countries That Reviewed': countries_reviewed
        }

        if format == 'csv':
            self.export_to_csv(export_data)
        elif format == 'txt':
            self.export_to_txt(export_data)
        elif format == 'json':
            self.export_to_json(export_data)
        else:
            print("Unsupported format.")

    @staticmethod
    def export_to_csv(self, data):
        """Export data to a CSV file."""
        with open('park_reviews.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)

    @staticmethod
    def export_to_txt(self, data):
        """Export data to a TXT file."""
        with open('park_reviews.txt', mode='w') as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

    @staticmethod
    def export_to_json(self, data):
        """Export data to a JSON file."""
        with open('park_reviews.json', mode='w') as file:
            json.dump(data, file, indent=4)



# 