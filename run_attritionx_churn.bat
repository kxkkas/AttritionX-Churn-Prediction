@echo off
cd /d "C:\Users\KASHIF\OneDrive\Desktop\AttritionX_App_Churn"
python attritionx_app_churn.py

:: Open the output CSV file
start "" "churn_predictions.csv"

pause