import os
from bs4 import BeautifulSoup

# Define the directory for job listing files
jobFilesDirectory = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/"
jobFileList = os.listdir(jobFilesDirectory)

# Function to extract job title
def extractJobTitle(soup):
    titleElements = soup.find_all('h1', attrs={'class': 'topcard__title'})
    return titleElements[0].text.strip() if titleElements else 'NULL'

# Function to extract company name
def extractCompanyName(soup):
    companyElements = soup.find_all('span', attrs={'class': 'topcard__flavor'})
    return companyElements[0].text.strip().replace(',', '') if companyElements else 'NULL'

# Function to extract job location
def extractJobLocation(soup):
    locationElements = soup.find_all('span', attrs={'class': 'topcard__flavor topcard__flavor--bullet'})
    return locationElements[0].text.strip().replace(',', '') if locationElements else 'NULL'

# Function to extract job description
def extractJobDescription(soup):
    descriptionElements = soup.find_all('div', attrs={"description__text description__text--rich"})
    return descriptionElements[0].text.strip() if descriptionElements else 'NULL'

# Initialize a counter for job IDs
jobId = 500

# Path for the output CSV file
outputCSVPath = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/emp.csv"

# Open the CSV file and write headers
with open(outputCSVPath, "w", encoding="utf-8") as csvFile:
    csvFile.write("id_Emploi;Nom_Fichier;Nom_Soc;Libele_Poste;description_Poste;ville\n")

    # Process each job listing file
    for fileName in jobFileList:
        with open(os.path.join(jobFilesDirectory, fileName), "r", encoding="ISO-8859-1") as file:
            fileContent = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(fileContent, 'lxml')

        # Extract job details
        jobTitle = extractJobTitle(soup)
        companyName = extractCompanyName(soup)
        jobLocation = extractJobLocation(soup)
        jobDescription = extractJobDescription(soup)

        # Write job details to the CSV file
        csvFile.write(f"{jobId};{fileName};{companyName};{jobTitle};{jobDescription};{jobLocation}\n")

        # Increment the job ID
        jobId += 1

        # Debugging print statements (optional)
        print(f"Processed job file: {fileName}")
        print("****************************************************************************************")
