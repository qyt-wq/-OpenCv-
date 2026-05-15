'''

人脸采集：打开摄像头，按下S键保存人脸图像
'''
#1，导入库
import cv2
import os
#from PIL.ImageOps import mirror
#加载级联分类器
classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#2初始化

count=0
font = cv2.FONT_HERSHEY_TRIPLEX   #OpenCv内置字体常量
stu_id=input('请输入你的学号:\n')
stu_name=input('请输入你的姓名:\n')

#创建人脸数据目录
if not os.path.exists('data'):
    os.mkdir('data')

#3打开摄像头
cap = cv2.VideoCapture(0)    #调用摄像头，参数0表示电脑默认摄像头
if cap.isOpened():
    print('摄像头打开成功')
else:
    print('摄像头打开失败')
while cap.isOpened():
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图像灰度转换
    cv2.putText(frame,'press "q" to quit',(15,30),font,1,(0,0,255),2)

    kk = cv2.waitKey(2)
    faces = classifier.detectMultiScale(gray, 1.2, 4)
    #print(faces)
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 3)
            cv2.putText(frame, 'press "s" to save', (x,y), font, 1.2, (0, 0, 255), 2)
            if kk==ord('s'):
                cv2.imwrite('data/'+str(stu_name)+'.'+str(stu_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
                count+=1
                print('采集了'+str(count)+'张图片')
    # 打开摄像头，实时显示画面
    # 自动检测人脸，画出紫红色框
    # 按S键 → 保存人脸图片
    # 按Q键 → 退出程序
    # 图片自动命名：姓名.学号.序号.jpg

#    mirror1=cv2.flip(frame,-1)  #0—垂直反转，1—水平反转，-1—水平+垂直反转
#    mirror2 = cv2.flip(frame, 0)
#    mirror3 = cv2.flip(frame, 1)

    cv2.imshow('cap',frame)
#    cv2.imshow('cap1',mirror1)
#    cv2.imshow('cap2', mirror2)
#    cv2.imshow('cap3', mirror3)
    if kk==ord('q'):
        print('共采集了学号为：'+str(stu_id)+','+'姓名为'+str(stu_name)+'的同学'+','+str(count)+'张图像'+'.jpg')
        break
cap.release()   #释放资源
cv2.destroyAllWindows()
