import pandas as pd

# File paths of the uploaded CSV files
files = [
    "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\loc.csv",
    "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\soc.csv",
    "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\avi.csv",
    "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\emp.csv"
]

# Reading the first column from each CSV file
columns = []
for file in files:
    df = pd.read_csv(file, usecols=[0])
    columns.append(df)


# Re-reading the CSV files with automatic delimiter detection
columns = []
for file in files:
    try:
        df = pd.read_csv(file, usecols=[0], sep=None, engine='python')
    except UnicodeDecodeError:
        df = pd.read_csv(file, usecols=[0], sep=None, engine='python', encoding='ISO-8859-1')
    columns.append(df.iloc[:, 0])

# Creating the new DataFrame with correct columns
fact_table_corrected = pd.concat(columns, axis=1)
fact_table_corrected.columns = ['id_localisation', 'id_Entreprise', 'id_avis', 'id_Emploi']  

# Adding an ID column
fact_table_corrected.insert(0, 'ID', range(1, 1 + len(fact_table_corrected)))

# Display the first few rows of the new DataFrame to verify
fact_table_corrected.head()
