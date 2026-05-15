'''

识别签到：人脸识别，并在识别成功后在表格中签到
'''

#1导入库
import cv2
from tkinter import messagebox
import xlrd
import xlwt
from xlutils.copy import copy
import time
from datetime import datetime

from excel示例 import style1




#2加载级联分类器
classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
create=cv2.face_LBPHFaceRecognizer.create()
create.read('train.yml')

#初始化变量
font=cv2.FONT_HERSHEY_SIMPLEX
ID=('UNKNOWN')
conf=0
start_time=time.time()
count=0

current_idx=-1
current_name=''

#定义函数签名子函数
def sing_in(idx,name):
    student_id = stu_id[idx]  # 拿到学号
    if is_already_signed(student_id):
        messagebox.showinfo("提示", f"{name}\n今日已签到，无需重复签到！")
        return
    wb=xlrd.open_workbook('人脸签到表.xls')

    nwb=copy(wb)
    nws=nwb.get_sheet(0)
    nws.col(5).width=256*15



    style2=xlwt.easyxf('font: height 200,bold on,color_index red',num_format_str='YYYY.MM.DD HH:MM')

    nws.write(idx,4,name,style1)
    nws.write(idx,5,datetime.now(), style2)

    nwb.save('人脸签到表.xls')
    messagebox.showinfo("签到成功", f"{name} 签到成功！")

#查重函数
def is_already_signed(student_id):
    file_path = "人脸签到表.xls"
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        rb = xlrd.open_workbook(file_path)
        sheet = rb.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            id_cell = sheet.cell_value(row, 2)  # 学号在第2列
            time_cell = sheet.cell_value(row, 5)

            if str(id_cell).strip() == str(student_id).strip():
                if isinstance(time_cell, float):
                    date_tuple = xlrd.xldate_as_tuple(time_cell, 0)
                    row_date = f"{date_tuple[0]}-{date_tuple[1]:02d}-{date_tuple[2]:02d}"
                else:
                    # row_date = str(time_cell)[:10]
                    row_date = str(time_cell).split(' ')[0]

                if row_date == today:
                    return True
    except:
        pass
    return False

#3获取表格中的学号和签名与人脸识别结果进行比对
workbook=xlrd.open_workbook('人脸签到表.xls')
worksheet=workbook.sheet_by_index(0)
stu_id=worksheet.col_values(2)
stu_name=worksheet.col_values(3)


#4打开摄像头
font = cv2.FONT_HERSHEY_TRIPLEX
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print('摄像头打开成功')
else:
    print('摄像头打开失败')
while cap.isOpened():
    kk = cv2.waitKey(1)
    _,frame = cap.read()

    cv2.putText(frame, 'press "q" to quit', (15, 30), font, 1, (0, 0, 255), 2)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图像灰度转换

    faces = classifier.detectMultiScale(gray, 1.2, 4)

    if len(faces) != 0:
        for (x, y, w, h) in faces:
            cv2.putText(frame, str(ID), (x, y), font, 1.2, (50, 90, 210))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 3)

            gray1=gray[y:y+h,x:x+w]
            label,conf=create.predict(gray1)
            #print(label,conf)

            if conf < 60:  #conf置信度，越小越准确
                index=[list for list,i in enumerate(stu_id) if i==str(label)]
                #print(index)
                if len(index) != 0:
                    ID=stu_id[index[0]]
                    name=stu_name[index[0]]
                    count+=1


                else:
                    ID=('UNKNOWN')
                #print(ID, name)



    cv2.imshow('cap', frame)
    if kk==ord('q'):
        print('用户主动退出')
        break
    if count>10:
        sing_in(index[0],name)
        print('签到成功')
        count=0


    if time.time()-start_time>60:
        print('超时')
        break

#5释放资源
cap.release()
cv2.destroyAllWindows()
