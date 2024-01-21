import os
import re
from bs4 import BeautifulSoup

# Directory containing company files
companyDirectory = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/SOC/"
companyFiles = os.listdir(companyDirectory)

# Function to extract company name
def extractCompanyName(soup):
    companyNameElement = soup.find('h1', {'class': "strong tightAll"})
    return companyNameElement['data-company'] if companyNameElement else 'NULL'

# Function to extract company location
def extractCompanyLocation(soup):
    locationElement = soup.find('div', {'class': "infoEntity"})
    return locationElement.span.text if locationElement and locationElement.span else 'NULL'

# Function to extract company sector
def extractCompanySector(soup):
    sectorElement = soup.find(text='Secteur').findNext('span') if soup.find(text='Secteur') else 'NULL'
    return sectorElement.text if sectorElement else 'NULL'

# Function to extract company foundation year
def extractCompanyFoundation(soup):
    foundationElement = soup.find(text=['Fondé en', 'Créé en dans les années', 'existe depuis']).findNext('span') if soup.find(text=['Fondé en', 'Créé en dans les années', 'existe depuis']) else 'NULL'
    return foundationElement.text if foundationElement else 'NULL'

# Function to extract company website
def extractCompanyWebsite(soup):
    websiteElement = soup.find('div', {'class': "infoEntity"})
    return websiteElement.text.replace('Site Web', '').strip() if websiteElement else 'NULL'

# Initialize ID counter
companyId = 0

# Output file path
outputFilePath = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/GLASSDOOR/SOC/soc.csv"

# Create and write to CSV file
with open(outputFilePath, "w", encoding="iso-8859-1") as csvFile:
    csvFile.write("id_Entreprise;Nom_Fichier;Nom_Entreprise;Site_Web;Siege_social;Secteur;Annee_Creation\n")

    # Process each file
    for fileName in companyFiles:
        with open(os.path.join(companyDirectory, fileName), "r", encoding="iso-8859-1") as file:
            fileContent = file.read()

        # Parse HTML content
        soup = BeautifulSoup(fileContent, 'lxml')

        # Extract company details
        companyName = extractCompanyName(soup)
        companyWebsite = extractCompanyWebsite(soup)
        companyLocation = extractCompanyLocation(soup)
        companySector = extractCompanySector(soup)
        companyFoundation = extractCompanyFoundation(soup)

        # Write to CSV
        csvFile.write(f"{companyId};{fileName};{companyName};{companyWebsite};{companyLocation};{companySector};{companyFoundation}\n")
        companyId += 1

        # Debugging print statements (optional)
        print(f"Processed company file: {fileName}")
        print("****************************************************************************************")

# The CSV file is automatically closed after exiting the 'with' block
