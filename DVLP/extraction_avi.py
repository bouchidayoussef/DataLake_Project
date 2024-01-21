# =============================================================================
# Import Required Libraries
# =============================================================================
import os
import re
from bs4 import BeautifulSoup

# Directory for input files
input_directory = "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\1_LANDING_ZONE\\GLASSDOOR\\AVI\\"
file_list = os.listdir(input_directory)

# =============================================================================
# Function Definitions
# =============================================================================

# Function to Extract Company Name from Soup Object
def extract_company_name(soup):
    search_result = soup.find_all('div', attrs={"class": "header cell info"})[0].span.contents[0]
    return 'NULL' if search_result == [] else search_result

# Function to Extract Review Date
def extract_review_date(soup):
    search_result = soup.find_all('time', attrs={'class': 'date subtle small'})
    clean_text = 'NULL' if search_result == [] else search_result[0].text.replace(',', '')
    return clean_text

# Function to Extract Review Title
def extract_review_title(soup):
    search_result = soup.find_all('a', attrs={"class": "reviewLink"})[0].span.contents[0]
    if search_result == []:
        clean_text = 'NULL'
    else:
        clean_text = str(search_result).replace('«', '').replace('»', '')
    return clean_text.replace('\xa0', '')

# Function to Extract Advantages from Reviews
def extract_advantages(soup):
    search_result = soup.find(text='Avantages').findNext('p').text
    return 'NULL' if search_result == [] else search_result.replace(',', '.').replace('\n', '')

# Function to Extract Disadvantages from Reviews
def extract_disadvantages(soup):
    search_result = soup.find(text='Inconvénients')
    return 'NULL' if search_result is None else search_result.findNext('p').text

# Function to Extract Review Author
def extract_author(soup):
    search_result = soup.find_all('div', attrs={"class": "author minor"})[0].span.contents[0]
    return 'NULL' if search_result == [] else re.sub(r'<span (.*)">(.*)</span>(.*)', r'\2', str(search_result))

# Function to Extract Review Location
def extract_location(soup):
    search_result = soup.find_all('span', attrs={"class": "authorLocation"})
    return 'NULL' if search_result == [] else re.sub(r'<span (.*)">(.*)</span>(.*)', r'\2', str(search_result)).replace('[', '')

# Function to Extract Average Rating
def extract_average_rating(soup):
    search_result = soup.find_all('div', attrs={"class": "v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large"})
    return 'NULL' if search_result == [] else re.sub(r'<div (.*)">(.*)</div>(.*)', r'\2', str(search_result)).replace('[', '')

# Function to Extract Individual Ratings
def extract_individual_ratings(soup):
    default_list = ['null', 'null', 'null', 'null', 'null']
    try:
        search_result = soup.find_all('div', attrs={"class": "subRatings module stars__StarsStyles__subRatings"})[0]
        ratings = search_result.find_all('span', attrs={'class': "gdBars gdRatings med"})
        categories = search_result.find_all('div', attrs={'class': "minor"})
    except IndexError:
        return default_list
    if search_result == [] or len(categories) <= 4:
        return default_list
    else:
        extracted_ratings = [re.sub(r'<span class="(.*)" title="(.*)"><i>(.*)</i></span>(.*)', r'\2', str(rating)).replace('[', '') for rating in ratings]
        return extracted_ratings

# =============================================================================
# File Processing
# =============================================================================
key = 0
output_file1_path = "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\2_CURATED_ZONE\\GLASSDOOR\\AVI\\avi.csv"
output_file2_path = "D:\\TD GDM\\TD_DATALAKE\\DATALAKE\\2_CURATED_ZONE\\GLASSDOOR\\AVI\\data.csv"

with open(output_file1_path, "w", encoding="utf-8") as file1, open(output_file2_path, "w", encoding="utf-8") as file2:
    file1.write("id_avis;Nom_Fichier;Nom_Entreprise;Titre_Avis;Date_Avis;Auteur_Avis;Loc_Avis;Inconvenients;Avantages\n")
    file2.write("id_Note;Nom_Fichier;Titre_Avis;Équilibre travail/vie privée;Culture et valeurs;Opportunités de carrière;émunération et avantages;Équipe dirigeante;Note_moyenne\n")

    for filename in file_list:
        file_path = input_directory + filename
        print(filename)
        with open(file_path, "r", encoding="ISO-8859-1") as file:
            file_content = file.read()
    
        soup = BeautifulSoup(file_content, 'lxml')
        reviews = soup.find_all('li', attrs={'class': 'empReview'})

        for review in reviews:
            key += 1

            # Data for first file
            line1 = [
                key,
                filename,
                extract_company_name(soup),
                extract_review_title(soup),
                extract_review_date(soup),
                extract_author(soup),
                extract_location(soup),
                extract_disadvantages(soup),
                extract_advantages(soup)
            ]

            # Data for second file
            line2 = [
                key,
                filename,
                extract_company_name(soup),
                extract_review_title(soup),
                *extract_individual_ratings(soup),
                extract_average_rating(soup)
            ]

            # Writing data to files
            file1.write(';'.join(map(str, line1)) + '\n')
            file2.write(';'.join(map(str, line2)) + '\n')

# =============================================================================
