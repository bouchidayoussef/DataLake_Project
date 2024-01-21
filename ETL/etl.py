#ETL
import pandas as pd

def clean_encoding(text):
    # Replacing the incorrect encoding characters with the correct ones
    replacements = {
        'ÃƒÂ©': 'é', 'Ãª': 'ê', 'Ã©': 'é', 'Ã¨': 'è', 'Ã ': 'à',
        'ÂÂ': '', 'Ãƒ': ' ', 'ÃƒÂ': ' ' 
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

# Extract: Load data from CSV files
avi_df = pd.read_csv("D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\avi.csv")
loc_df = pd.read_csv("D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\loc.csv",delimiter= ";")

# Transform: Apply transformations
# Cleaning data, handling missing values, filtering
avi_df.dropna(inplace=True)  # Example: Remove rows with missing values
emp_df['ColumnName'] = emp_df['ColumnName'].str.strip() 

# Clean specific columns in avi.csv
avi_columns_to_clean = ["Équilibre travail/vie privée", "Titre_Avis_y", "Auteur_Avis", "Loc_Avis", "Avantages"]
for col in avi_columns_to_clean:
    avi_df[col] = avi_df[col].astype(str).apply(clean_encoding)

# Standardize values in loc.csv
loc_df['Pays'] = loc_df['Pays'].replace({'France': 'FR'})

# Load: Save the transformed data to new CSV files
avi_df.to_csv("D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\avi_cleaned.csv", index=False)
loc_df.to_csv("D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\3_PRODUCTION_ZONE\\BDD\\loc_cleaned.csv", index=False)