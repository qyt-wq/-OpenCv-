'''
模型训练，将采集的图片进行训练并生成模型文件
'''
#1导入库
import cv2
import os
import numpy as np
from PIL import Image
#from 人脸检测 import faces

#2加载模型
create=cv2.face_LBPHFaceRecognizer.create()    #创建一个LBPH人脸识别器
#create1=cv2.face.LBPHFaceRecognizer_create()  #另一个创建LBPH人脸识别器的方法
#3数据处理
def data_translate(path):
    '''
        功能：从指定文件夹读取所有人脸图片，转换成模型能识别的数据
        path:存放人脸图片的文件夹路径
    '''
    face_data=[]     #存放处理好的人脸图片数据
    id_data=[]       #存放每个人脸对应的ID编号
    file_list = [os.path.join(path,f)for f in os.listdir(path)]    #遍历文件夹下的所有文件，生成完整文件路径
    #print(file_list)
    for file in file_list:
        PIL_image = Image.open(file).convert('L')   #打开图片并转成灰度图
        np_image = np.array(PIL_image,'uint8')  #把图片转换成opencv可以识别的np数组
        face_data.append(np_image)   #把处理好的人脸图片加入列表
        #print(file.split('.')[1])
        id=int(file.split('.')[1])   #取file名以.分割的第二段（学号）
        id_data.append(id)      #加入列表
    return face_data,id_data   #返回所有人脸的数据以及对应id

#训练模型
print('开始训练模型')
Faces,IDs=data_translate('data')     # 调用函数读取data文件夹里的人脸图片和id
create.train(Faces,np.array(IDs))    #用读到的人脸信息与id训练模型

#保存模型
create.save('train.yml')   #将训练好的模型保存为.yml文件
print('模型训练已完成，并保存模型')