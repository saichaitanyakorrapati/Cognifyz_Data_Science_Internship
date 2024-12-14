import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = 'Dataset.csv'
file_path = os.path.join(desktop_folder, file_name)
def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except Exception as e:
        print("Error loading dataset:", str(e))
def calculate_percentage(data):
    total_restaurants = len(data)
    table_booking = len(data[data['Has Table booking'] == 'Yes'])
    online_delivery = len(data[data['Has Online delivery'] == 'Yes'])
    
    table_booking_percentage = (table_booking / total_restaurants) * 100
    online_delivery_percentage = (online_delivery / total_restaurants) * 100
    
    return table_booking_percentage, online_delivery_percentage
def compare_average_ratings(data):
    avg_rating_with_table_booking = data[data['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
    avg_rating_without_table_booking = data[data['Has Table booking'] == 'No']['Aggregate rating'].mean()
    
    return avg_rating_with_table_booking, avg_rating_without_table_booking
def analyze_online_delivery(data):
    price_ranges = ['$','$$','$$$']
    online_delivery_availability = {}
    
    for price_range in price_ranges:
        online_delivery_count = len(data[(data['Price range'] == price_range) & (data['Has Online delivery'] == 'Yes')])
        total_restaurants_in_price_range = len(data[data['Price range'] == price_range])
        
        if total_restaurants_in_price_range > 0:
            availability_percentage = (online_delivery_count / total_restaurants_in_price_range) * 100
            online_delivery_availability[price_range] = availability_percentage
        else:
            online_delivery_availability[price_range] = 0
    
    return online_delivery_availability
def main():
    data = load_dataset(file_path)

    if data is not None:
        table_booking_percentage, online_delivery_percentage = calculate_percentage(data)
        print(f"Percentage of restaurants with table booking: {table_booking_percentage}%")
        print(f"Percentage of restaurants with online delivery: {online_delivery_percentage}%")

        avg_rating_with_table_booking, avg_rating_without_table_booking = compare_average_ratings(data)
        print(f"Average rating of restaurants with table booking: {avg_rating_with_table_booking}")
        print(f"Average rating of restaurants without table booking: {avg_rating_without_table_booking}")

        online_delivery_availability = analyze_online_delivery(data)
        print("Online delivery availability among restaurants with different price ranges:")
        for price_range, availability_percentage in online_delivery_availability.items():
            print(f"{price_range}: {availability_percentage}%")

if __name__ == "__main__":
    main()
