"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt


def most_reviewed_parks(data):
    park_counts = {}
    for row in data:
        park = row['Branch']
        park_counts[park] = park_counts.get(park, 0) + 1

    plt.pie(list(park_counts.values()), labels=list(park_counts.keys()), autopct='%1.1f%%')
    plt.title("Most Reviewed Parks")
    plt.show()


def average_scores(data):
    park_scores = {}
    for row in data:
        park = row['Branch']
        score = int(row['Rating'])
        park_scores.setdefault(park, []).append(score)

    avg_scores = {park: sum(scores) / len(scores) for park, scores in park_scores.items()}
    plt.bar(list(avg_scores.keys()), list(avg_scores.values()))
    plt.title("Average Scores by Park")
    plt.xlabel("Park")
    plt.ylabel("Average Score")
    plt.show()


def park_ranking_by_nationality(data, park):
    location_scores = {}
    for row in data:
        if row['Branch'] == park:
            location = row['Reviewer_Location']
            score = int(row['Rating'])
            location_scores.setdefault(location, []).append(score)

    avg_scores = sorted(
        [(loc, sum(scores) / len(scores)) for loc, scores in location_scores.items()],
        key=lambda x: x[1], reverse=True
    )[:10]

    locations, scores = zip(*avg_scores)
    plt.bar(locations, scores)
    plt.title(f"Top 10 Locations for {park} by Average Rating")
    plt.xlabel("Location")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.show()


def most_popular_month_by_park(data, park):
    month_scores = {}
    for row in data:
        if row['Branch'] == park:
            month = row['Year_Month'][:7]  # e.g., "2022-05"
            score = int(row['Rating'])
            month_scores.setdefault(month, []).append(score)

    avg_month_scores = {month: sum(scores) / len(scores) for month, scores in month_scores.items()}
    months, avg_scores = zip(*sorted(avg_month_scores.items()))

    plt.bar(months, avg_scores)
    plt.title(f"Average Monthly Rating for {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.show()



#