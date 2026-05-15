'''
人脸检测：熟悉opencv库
'''
#1导入库
import cv2
import numpy as np
#加载级联分类器
classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#2读取图像
img=cv2.imread('2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #图像灰度转换


'''
利用cv2库绘制各种图形
cv2.line(img,(287,290),(300,290),(0,255,0),6)#线段
cv2.line(img,(217,297),(236,290),(0,0,0),5)
#cv2.rectangle(img,(192,219),(350,410),(255,0,0),3)        #矩形
cv2.putText(img, "TYUT qhq 2024005848", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)  #文本
cv2.circle(img,(325,290),25,(0,0,0),-1)#圆
cv2.circle(img,(260,290),25,(0,0,0),-1)
#cv2.ellipse(img, (260,290), (50, 30), 0, 0, 360, (124,241,255), 3)  #椭圆
points = np.array([[125,100], [275,100],[150,200],[200,50], [250,200]],dtype=np.int32) #五角星
cv2.polylines(img,[points],True,(0,0,255),4)#无填充多边形
#cv2.fillPoly(img, [points], (0,0,255))#填充多边形
'''
#cv2.putText(img, "TYUT class2423", (50,100), cv2.FONT_HERSHEY_TRIPLEX, 4, (0,0,0), 5)  #文本
'''
cv2.FONT_HERSHEY_SIMPLEX        # 0  最常用、正常大小字体
cv2.FONT_HERSHEY_PLAIN          # 1  细小、简单字体
cv2.FONT_HERSHEY_DUPLEX         # 2  粗体（比SIMPLEX粗）
cv2.FONT_HERSHEY_COMPLEX        # 3  复杂正常字体
cv2.FONT_HERSHEY_TRIPLEX        # 4  复杂粗体
cv2.FONT_HERSHEY_COMPLEX_SMALL  # 5  小复杂字体
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX # 6  手写/脚本字体
cv2.FONT_HERSHEY_SCRIPT_COMPLEX # 7  复杂手写字体
cv2.FONT_ITALIC                # 8  斜体（可和上面叠加）
'''

faces = classifier.detectMultiScale(gray,1.1,4)  #在灰度图中检测人脸，返回人脸坐标位置
'''参数1.1是缩放比例（scaleFactor）
每次缩小图像 10% 再检测，提高不同大小人脸的检出率
常用值：1.05 ~ 1.3
参数 4是最小邻域点数（minNeighbors）
控制误检：一个区域至少被检测 4 次，才判定是人脸
数值越大：误检越少，但可能漏检
常用值：3 ~ 6'''
print(faces)   #输出人脸坐标位置
'''if len(faces)!=0:
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,255), 3)  #多人脸识别'''
#face_num = 1
for (x, y, w, h) in faces:
        # 计算人脸中心点
        centerX = x + w // 2
        centerY = y + h // 2     # 计算人脸中心点
        r = max(w, h) // 2   # 计算圆形半径（取宽高的一半）

       #  cv2.circle(img, (centerX, centerY), r, (0,255,0), 2)  #圆形框
       # face_img = img[y:y + h, x:x + w]
       # cv2.imwrite(f'grayFace{face_num}.jpg', gray[y:y+h,x:x+w])
       # face_num += 1   圆形框选人脸
'''for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)'''


cv2.rectangle(img,(faces[0,0],faces[0,1]),(faces[0,0]+faces[0,2],faces[0,1]+faces[0,3]),(255,0,0),3) #矩形框选人脸范围
cv2.imwrite('GrayFace1.jpg',gray[y:y+h,x:x+w])  #将检测到的图片裁剪成下来，保存为GrayFace1.jpg
cv2.imshow('img',img)
cv2.waitKey(0)


