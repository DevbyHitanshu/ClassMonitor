import gspread
from oauth2client.service_account import ServiceAccountCredentials
#email to add as editor "classroomapp@western-arch-321815.iam.gserviceaccount.com"
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds_app.json",scope)
client=gspread.authorize(creds)
sheet=client.open("testing").sheet1 # testing
#sheeesh=client.open("form_test").sheet1 # form 
data = sheet.get_all_records()
from random import randint
from datetime import date
today = date.today()
'''
a=sheeesh.col_values(2)
for i in a[1:]:
    print(i)
'''
#dae=today.strftime("%d/%m/%Y")


#cell = sheet.cell(1,2).value  # Get the value of a specific cell
#col = sheet.col_values(3)  # Get a specific column
#row = sheet.row_values(3)  # Get a specific row

#insertRow = ["hello", 5, "red", "blue"]
#sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

#sheet.update_cell(3,3, dae)  # Update one cell
#numRows = sheet.row_count  # Get the number of rows in the sheet

name=['james','bond','jack','daniels','wo','chang']
size=[2,3,4,5,6,7]

sheet.update_cell(1,1,"Serial")
sheet.update_cell(1,2,"Names")
sheet.update_cell(1,3,"Marks")


for i,j in zip(name,size):
    sheet.update_cell(j,2,i)
    sheet.update_cell(j,1,j-1)
    sheet.update_cell(j,3,randint(0,100))


