@echo off
SETLOCAL EnableDelayedExpansion

REM Define the paths to your Python executable and scripts
set PYTHON_EXE=C:\Users\PC_Gamer\AppData\Local\Programs\Python\Python39\python.exe
set SCRIPTS_DIR=D:\TD GDM\TD_DATALAKE\DVLP
set HTML_DIR=D:\TD GDM\TD_DATALAKE\DATALAKE\0_SOURCE_WEB
set BDD_DIR=D:\TD GDM\TD_DATALAKE\DATALAKE\3_PRODUCTION_ZONE\BDD

REM Separate HTML files into folders
echo Separating HTML files...
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\separation_html.py" "!HTML_DIR!"

REM Extract data from Glassdoor and LinkedIn HTML files to CSV
echo Extracting data from Glassdoor...
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\extraction_soc.py" "!HTML_DIR!\glassdoor"
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\extraction_avi.py" "!HTML_DIR!\glassdoor"
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\extraction_loc.py" "!HTML_DIR!\glassdoor"

echo Extracting data from LinkedIn...
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\extraction_emp.py" "!HTML_DIR!\linkedin"

REM Perform ETL operations and create the final clean CSV files
echo Performing ETL operations...
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\etl.py" "!BDD_DIR!"

REM Any additional metadata extraction or cleanup scripts
echo Extracting additional metadata...
call "!PYTHON_EXE!" "!SCRIPTS_DIR!\metadonnees.py" "!BDD_DIR!"

REM Move the final CSV files to the BDD directory
echo Moving final CSV files to BDD directory...
move /Y "*.csv" "!BDD_DIR!"

REM End of script
echo Automation process completed!
ENDLOCAL
