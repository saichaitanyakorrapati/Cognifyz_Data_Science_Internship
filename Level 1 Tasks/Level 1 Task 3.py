import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os
desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = 'Dataset.csv'
file_path = os.path.join(desktop_folder, file_name)

try:
    df = pd.read_csv(file_path)
    print("Dataset uploaded successfully!")
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)
    for index, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(m)
    m.save('restaurant_locations.html')
    city_counts = df['City'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=city_counts.index, y=city_counts.values)
    plt.title('Distribution of Restaurants Across Cities')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.show()
    country_counts = df['Country Code'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_counts.index, y=country_counts.values)
    plt.title('Distribution of Restaurants Across Countries')
    plt.xlabel('Country Code')
    plt.ylabel('Count')
    plt.show()
    X = df[['Latitude', 'Longitude']]
    y = df['Aggregate rating']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f'Correlation Coefficient: {model.coef_}')
    print(f'R-Squared Value: {model.score(X_test, y_test)}')

except FileNotFoundError:
    print(f"The file {file_name} does not exist on the Desktop.")
