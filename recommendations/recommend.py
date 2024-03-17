import pandas as pd
import random


def get_recommendations(favorites, consolidated_file_path):
    print("Favorites in get_recommendations:", favorites)
    #print("CSV Path:", consolidated_file_path)
    # Load the consolidated data
    df = pd.read_csv(consolidated_file_path)
    #print("DataFrame loaded, first few rows:", df.head())

    # Filter out rows where Restaurant A is in the favorites
    filtered_df = df[df['Restaurant A'].isin(favorites)]

    # Aggregate shared voter counts for each Restaurant B not in favorites
    recommendations = {}
    for _, row in filtered_df.iterrows():
        restaurant_b = row['Restaurant B']
        shared_voters = row['Shared_Voter_Count']
        if restaurant_b not in favorites:
            recommendations[restaurant_b] = recommendations.get(restaurant_b, 0) + shared_voters

    # Sort recommendations based on the total shared voter count
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    top_recommendations = [rec[0] for rec in sorted_recommendations[:5]]  # Return top 5 recommendations
    print(top_recommendations)

    # Return one random recommendation from the top 5
    if top_recommendations:
        return [random.choice(top_recommendations)]
    else:
        return []

# consolidated_file_path = '/home/jtaylor/PycharmProjects/RVARecommends/data/combined_results.csv'
# favorites = ['Perlys', 'Sub Rosa']
# recommended_restaurants = get_recommendations(favorites, consolidated_file_path)
# print(recommended_restaurants)
