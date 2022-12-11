#統計該資料夾裡的txt檔標籤的Numbers總數

import os
from re import X
import matplotlib.pyplot as plt

folder_path = 'D:\\project\\label(20)'    #存放Labels路徑
classes_file = "D:\\project\\classes.txt" #存放類別文件路徑
#E:\\魚類標記\\classes.txt
#E:\\魚類標記\\relabelclasses.txt
classes_data = []
file_list=os.listdir(folder_path)
white_list=[0,1,2,4,5,6,15,18,24,26,27,39,42,43,55,63,70,76,78,81]  #圖中會顯示的種類

#生成 [['0_Chromis_fumea', 0], ['1_Pomacentrus_coelestis', 0]......,['87_Mugil_cephalus', 0]]
for classes in open(classes_file,'r',encoding="utf-8").readlines():
    dr = [classes.replace("\n", ""), 0]   #將原先內建的兩個換行替換成一個      
    classes_data.append(dr)               #將所有種類的列表包裝成一個大列表(classes_data[][])
    

#統計的數量並加入列表中
for item in file_list:
    #print(item)                 #P4-2021-09-24-12-00.mp4_002910.400.txt  #item為label路徑內各.txt黨的名稱
    #print(item.split('.')[3])   #txt  #括弧內數字需觀察檔案名來判斷
    if item.split('.')[1] == "txt" and item != "classes.txt":
        for line in open(folder_path+"/"+item,'r').readlines():  #讀取每一筆.txt檔資料
            for i in range(len(classes_data)):  #len(classes_data) = 99 
                if line.split(' ')[0] == str(i):
                    classes_data[i][1] += 1     #每次進入if迴圈,將['1_Pomacentrus_coelestis', 0]中的0+1

for i in range(len(classes_data)):
    if int(classes_data[i][0]) in white_list:
        print(classes_data[i])



fig = plt.figure()
fig.canvas.manager.set_window_title('data statistics')  
#版本問題可更改為fig.canvas.set_window_title('data statistics')
#plt.rcParams["font.sans-serif"]=['simhei']
#plt.rcParams['font.family']='sans-serif'   #新增的 
#plt.rcParams['axes.unicode_minus'] = False #新增的

plt.title("data statistics")
plt.xlabel("class")
plt.ylabel("number")
for i in range(len(classes_data)):
    if int(classes_data[i][0]) in white_list:
            plt.bar(classes_data[i][0], classes_data[i][1])
plt.show()

#replace()方法语法：str.replace(old, new[, max])
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串。
# max -- 可选字符串, 替换不超过 max 次

#append() 方法用于在列表末尾添加新的对象(dr)