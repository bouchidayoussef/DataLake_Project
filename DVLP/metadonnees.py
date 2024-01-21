import os
import re
import fnmatch
from datetime import datetime

# Define input and output paths
inputPath = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/"
outputPath = "/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/"
directoryList = ['GLASSDOOR/AVI/', 'GLASSDOOR/SOC/', 'LINKEDIN/EMP/']

# Function to get file size
def calculateFileSize(filePath):
    fileSize = os.path.getsize(filePath)
    return str(fileSize) + ' KO'

# Function to get file creation date
def fetchCreationDate(filePath):
    creationTime = os.path.getctime(filePath)
    return datetime.fromtimestamp(creationTime).strftime('%Y-%m-%d %H:%M:%S')

# Function to get file modification date
def fetchModificationDate(filePath):
    modificationTime = os.path.getmtime(filePath)
    return datetime.fromtimestamp(modificationTime).strftime('%Y-%m-%d %H:%M:%S')

# Function to get current datetime
def getCurrentDateTime():
    currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return currentDateTime

# Process each directory
for directory in directoryList:
    # Clean and prepare file names
    cleanedText = re.sub(r'(.*)/(.*)/', r'\2', directory)
    csvFilePath = outputPath + directory + 'meta.csv'
    
    # Create and open CSV file
    with open(csvFilePath, "w", encoding="utf-8") as file:
        file.write("ID;Filename;Website;CreationDate;ModificationDate;IngestionDate;FileSize\n")

        # List files in directory
        fileList = os.listdir(inputPath + directory)
        for index, fileName in enumerate(fileList):
            lineData = []
            lineData.append(index + 1)
            lineData.append(fileName)
            
            # Determine website based on filename
            if fnmatch.fnmatch(fileName, '*GLASSDOOR*'):
                lineData.append("GLASSDOOR")
            elif fnmatch.fnmatch(fileName, '*LINKEDIN*'):
                lineData.append("LINKEDIN")

            # Add file metadata to line
            fullPath = inputPath + directory + fileName
            lineData.append(fetchCreationDate(fullPath))
            lineData.append(fetchModificationDate(fullPath))
            lineData.append(getCurrentDateTime())
            lineData.append(calculateFileSize(fullPath))

            # Handle missing data
            lineData = ['null' if not item else item for item in lineData]
            formattedLine = ';'.join(map(str, lineData))

            print(formattedLine)
            print("*" * 90)
            file.write(formattedLine + '\n')
