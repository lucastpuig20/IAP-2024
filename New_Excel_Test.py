import xlwings as xw
from Excel_Append import check_amendment

master_wb = xw.Book("/Users/lucasg17/Documents/GitHub/Health-Innovation/Master.xlsx")
# master_sheets = master_wb.sheets
# # master_sheets[0].name = 'SV Health'
# # print(master_sheets[0].name)
# # print(master_sheets[0].range('A1').end('down').row)

# # newdata_wb = xw.Book("/Users/lucasg17/Downloads/convertcsv.xlsx")
# # new_data_raw = newdata_wb.sheets[0].range('A2').expand().value
# # print(new_data_raw)
# # temp_data = [i[:] for i in new_data_raw]
# # newrow = master_sheets[0].range('A1').end('down').row
# # master_wb.sheets['SV Health'][newrow,0].value = temp_data
# master_wb.sheets[1].clear()
# master_wb.save()

# print(check_amendment(newdata_loc_1="/Users/lucasg17/Downloads/convertcsv.xlsx", newdata_loc_2="/Users/lucasg17/Downloads/convertcsv (1).xlsx"))

print(master_wb.sheets[0].range('A1').expand().value[0])