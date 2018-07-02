
#把测试数据从excel读取出来

from openpyxl import load_workbook

class DoExcel:
    def __init__(self,file_path,sheet_name):
        self.file_path=file_path
        self.sheet_name=sheet_name
    def

    wb=load_workbook('tase_case.xlsx')
    sheet=wb['test_data']

    #每一行数据存在一个列表里面，然后所有行的数据存在大列表里面
    test_data=[]   #存储所有行的数据
    for i in range(2,sheet.max_row+1):
        sub_data=[]
        for j in range(1,8):
            sub_data.append(sheet.cell(i,j).value)
        test_data.append(sub_data)
    print(test_data)
