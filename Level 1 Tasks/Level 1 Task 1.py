import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = 'Dataset.csv'
file_path = os.path.join(desktop_folder, file_name)

try:
    df = pd.read_csv(file_path)
    print("Dataset uploaded successfully!")
    num_rows = df.shape[0]
    num_cols = df.shape[1]
    print(f"Number of Rows: {num_rows}")
    print(f"Number of Columns: {num_cols}")
    print("Dataset Preview:")
    print(df)  
    print("\nMissing Values:")
    print(df.isnull().sum())
    df['Aggregate rating'] = df['Aggregate rating'].fillna(df['Aggregate rating'].mean())
    df['Rating text'] = df['Rating text'].fillna(df['Rating text'].mode()[0])
    df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'])
    plt.hist(df['Aggregate rating'], bins=5, edgecolor='black')
    plt.title('Distribution of Aggregate Rating')
    plt.xlabel('Aggregate Rating')
    plt.ylabel('Frequency')
    plt.show()
    print("\nClass Distribution:")
    print(df['Aggregate rating'].value_counts())

except FileNotFoundError:
    print(f"The file {file_name} does not exist on the Desktop.")

