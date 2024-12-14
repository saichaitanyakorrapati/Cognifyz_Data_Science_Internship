import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = 'Dataset.csv'
file_path = os.path.join(desktop_folder, file_name)

try:
    df = pd.read_csv(file_path)
    print("Dataset uploaded successfully!")
    pd.set_option('display.max_columns', None)
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    print("\nBasic Statistical Measures:")
    print(df[numerical_cols].describe())
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        print(f"\nDistribution of {col}:")
        print(df[col].value_counts())
    print("\nTop Cuisines:")
    top_cuisines = df['Cuisines'].value_counts().head(10)
    print(top_cuisines)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_cuisines.index, y=top_cuisines.values)
    plt.title('Top 10 Cuisines')
    plt.xlabel('Cuisine')
    plt.ylabel('Count')
    plt.show()

    print("\nTop Cities:")
    top_cities = df['City'].value_counts().head(10)
    print(top_cities)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_cities.index, y=top_cities.values)
    plt.title('Top 10 Cities')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.show()

except FileNotFoundError:
    print(f"The file {file_name} does not exist on the Desktop.")
