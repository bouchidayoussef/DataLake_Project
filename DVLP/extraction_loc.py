import os
from bs4 import BeautifulSoup

# Directory containing job listing files
jobListingsDirectory = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/"
jobFiles = os.listdir(jobListingsDirectory)

# Function to extract city from job listing
def extractCity(soup):
    locationElement = soup.find('span', {'class': 'topcard__flavor topcard__flavor--bullet'})
    if locationElement:
        locationText = locationElement.text
        locationParts = locationText.split(', ')
        return locationParts[0] if len(locationParts) == 2 else 'NULL'
    return 'NULL'

# Function to extract country from job listing
def extractCountry(soup):
    locationElement = soup.find('span', {'class': 'topcard__flavor topcard__flavor--bullet'})
    if locationElement:
        locationText = locationElement.text
        locationParts = locationText.split(', ')
        return locationParts[1] if len(locationParts) == 2 else 'NULL'
    return 'NULL'

# Initialize an identifier for each location entry
locationId = 500

# Output file path for location data
outputFilePath = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/loc.csv"

# Create and open CSV file for writing
with open(outputFilePath, "w", encoding="utf-8") as csvFile:
    csvFile.write("id_localisation;Ville;Pays\n")

    # Process each job file
    for jobFileName in jobFiles:
        with open(os.path.join(jobListingsDirectory, jobFileName), "r", encoding="ISO-8859-1") as file:
            fileContent = file.read()

        # Parse HTML content
        soup = BeautifulSoup(fileContent, 'lxml')

        # Extract location information
        city = extractCity(soup)
        country = extractCountry(soup)

        # Write to CSV
        csvFile.write(f"{locationId};{city};{country}\n")
        locationId += 1

        # Debugging print statements (optional)
        print(f"Processed job file: {jobFileName}")
        print("****************************************************************************************")

