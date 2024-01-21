import os
import shutil

#Chemin de base vers le dossier 0_source_web
base_path = '/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/0_SOURCE_WEB'

#Dossiers de destination
linkedin_emp_folder = '/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/'
glassdoor_avi_folder = '/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/AVI/'
glassdoor_soc_folder = '/Users/youssefbouchida/Downloads/M2_BI&A/TD GDM/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/SOC/'

#Vérifier si les dossiers de destination existent, les créer sinon
os.makedirs(linkedin_emp_folder, exist_ok=True)
os.makedirs(glassdoor_avi_folder, exist_ok=True)
os.makedirs(glassdoor_soc_folder, exist_ok=True)

#Fonction pour copier les fichiers basés sur leur nom
def copy_files(source_folder, dest_folder, file_keyword):
    for file in os.listdir(source_folder):
        if file_keyword in file:
            shutil.copy(os.path.join(source_folder, file), dest_folder)

#Copier les fichiers dans les dossiers respectifs
copy_files(base_path, linkedin_emp_folder, "EMP-LINKEDIN")
copy_files(base_path, glassdoor_avi_folder, "AVIS-SOC")
copy_files(base_path, glassdoor_soc_folder, "INFO-SOC")