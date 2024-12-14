import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = 'Dataset.csv'
file_path = os.path.join(desktop_folder, file_name)
def load_dataset(file_path):
    try:
        print("Loading dataset...")
        dataset = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return dataset
    except Exception as e:
        print("Error loading dataset:", str(e))
def extract_additional_features(data):
    print("Extracting additional features...")
    data['Restaurant Name Length'] = data['Restaurant Name'].apply(len)
    data['Address Length'] = data['Address'].apply(len)
    data['City'] = data['Address'].apply(lambda x: x.split(',')[-1].strip() if isinstance(x, str) else '')
    data['Locality'] = data['Address'].apply(lambda x: x.split(',')[0].strip() if isinstance(x, str) else '')
    data['Cuisines Count'] = data['Cuisines'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)
    data['Rating Count'] = data['Rating text'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)
    data['Average Cost for two'] = data['Average Cost for two'].apply(lambda x: float(x.replace(',', '')) if isinstance(x, str) else 0)
    print("Additional features extracted successfully.")
    return data
def create_new_features(data):
    print("Creating new features...")
    # One-hot encoding for categorical variables
    categorical_cols = ['Type', 'Price range', 'Currency', 'Rating color']
    categorical_cols = [col for col in categorical_cols if col in data.columns]
    data = pd.get_dummies(data, columns=categorical_cols)
    binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']
    for col in binary_cols:
        if col in data.columns:
            data[col] = data[col].map({'Yes': 1, 'No': 0})
    data['Cuisines'] = data['Cuisines'].fillna('Unknown')
    cuisines_mapping = {cuisine: index for index, cuisine in enumerate(data['Cuisines'].unique())}
    data['Cuisines'] = data['Cuisines'].map(cuisines_mapping)
    print("New features created successfully.")
    return data
def main():
    data = load_dataset(file_path)

    if data is not None:
        print("Dataset shape:", data.shape)
        data = extract_additional_features(data)
        data = create_new_features(data)
        print("Dataset shape after feature engineering:", data.shape)
        print("All rows of the dataset:")
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(data)

if __name__ == "__main__":
    main()
