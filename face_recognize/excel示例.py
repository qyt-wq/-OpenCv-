'''
excel示例：用于处理xls版本excel文件学习xlrd，xlwt，xlutils，表格制作与修改
'''
#1导入库
import xlrd   #读取excel文件
import xlwt   #写入表格内容
from xlutils.copy import copy  #复制已有表格实现追加内容

#2xlwt新建表格+写入数据

workbook=xlwt.Workbook()
sheet1=workbook.add_sheet('第一个表')
sheet1.write(0,0,'人脸识别')

'''biaotou=['序号','班级','学号','姓名','签名','签到时间']
ID=['001','002','003','004','005','006','007','008']
for i in range(0,6):
    sheet1.write(2,i,biaotou[i])

for i in range(len(ID)):
    sheet1.write(i + 3, 2, ID[i])'''
workbook.save('face_recognize.xls')
style=xlwt.XFStyle()
font = xlwt.Font()  #创建设置文字外观
font.name="楷体"
font.bold=True
font.height=420
font.colour_index=0  #0-黑色 1-白色 2-红色 3-绿色  4-蓝色
align=xlwt.Alignment()
align.horz=xlwt.Alignment.HORZ_CENTER
align.vert=xlwt.Alignment.VERT_CENTER
style.font = font
style.alignment=align

sheet1.write(1,0,'人脸识别项目',style)


style1=xlwt.XFStyle()
align=xlwt.Alignment()
align.horz=xlwt.Alignment.HORZ_CENTER
align.vert=xlwt.Alignment.VERT_CENTER
style1.alignment=align


borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
style1.borders=borders
style.borders=borders


sheet1.write(2,4,'姓名',style1)

style3=xlwt.XFStyle()
pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=22  #42浅黄   0透明
style3.pattern=pattern

sheet1.write(6,8,'1234',style3)
sheet1.col(0).width=256*20
sheet1.col(1).width=256*3
sheet1.row(0).height_mismatch=True
sheet1.row(0).height=25*20
workbook.save('face_recognize.xls')

#3xlrd读取表格数据
readbook=xlrd.open_workbook('face_recognize.xls')
readsheet=readbook.sheet_by_index(0)
h=readsheet.nrows
l=readsheet.ncols
#print(h,l)
col_data=readsheet.col_values(1)
#print(col_data)
row_data=readsheet.row_values(2)
#print(row_data)
cell_data=readsheet.cell_value(1,1)
#print(cell_data)

#4xlutils复制修改表格
nwb=copy(readbook)    #复制表格
#nwb.add_sheet('新工作表')   #新建一张表
ns=nwb.get_sheet(0)
ns.write_merge(0,1,0,8,'签到表格',style)

biaotou=['序号','班级','学号','姓名','签到','签到时间','签退','签退时间','备注']  #表头信息
ID=['001','002','003','004','005','006','007','008']
name=['张三','李四','王五','赵六','钱七','孙八','孙悟空','李逵']
Class=['2026','2026','2026','2026','2026','2026','2026','2026']
for i in range(len(biaotou)):
    ns.write(2,i,biaotou[i],style1)
ns.col(1).width = 256 * 18  # 班级   #列宽
ns.col(2).width = 256 * 22  # 学号
for i in range(len(ID)):
    ns.write(i+3,3,name[i],style1)
    ns.write(i + 3, 2, ID[i],style1)
    ns.write(i + 3, 1, Class[i],style1)
    ns.write(i + 3, 0, i+1,style1)
    ns.write(i + 3, 4, '', style1)
    ns.write(i + 3, 5, '', style1)
    ns.write(i + 3, 6, '', style1)
    ns.write(i + 3, 7, '', style1)
    ns.write(i + 3, 8, '', style1)

nwb.save('人脸签到表.xls')

