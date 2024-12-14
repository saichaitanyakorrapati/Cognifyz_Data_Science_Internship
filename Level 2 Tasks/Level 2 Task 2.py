import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the file path
desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = 'Dataset.csv'
file_path = os.path.join(desktop_folder, file_name)
def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except Exception as e:
        print("Error loading dataset:", str(e))
def most_common_price_range(data):
    price_range_counts = data['Price range'].value_counts()
    most_common_price_range = price_range_counts.idxmax()
    return most_common_price_range
def average_rating_by_price_range(data):
    average_ratings = data.groupby('Price range')['Aggregate rating'].mean().reset_index()
    return average_ratings
def color_for_highest_average_rating(data):
    average_ratings = average_rating_by_price_range(data)
    max_average_rating = average_ratings['Aggregate rating'].max()
    max_average_rating_price_range = average_ratings.loc[average_ratings['Aggregate rating'] == max_average_rating, 'Price range'].iloc[0]
    highest_average_rating_color = data.loc[data['Price range'] == max_average_rating_price_range, 'Rating color'].iloc[0]
    return highest_average_rating_color
def main():
    data = load_dataset(file_path)
    
    most_common_price_range_value = most_common_price_range(data)
    print(f"Most common price range: {most_common_price_range_value}")
    
    average_ratings = average_rating_by_price_range(data)
    print("Average ratings by price range:")
    print(average_ratings)
    
    highest_average_rating_color = color_for_highest_average_rating(data)
    print(f"Color representing the highest average rating: {highest_average_rating_color}")
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Price range', y='Aggregate rating', data=average_ratings)
    plt.xlabel('Price Range')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings by Price Range')
    plt.show()

if __name__ == "__main__":
    main()
