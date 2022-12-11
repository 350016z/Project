#若舊資料夾裡文件內容的標籤編號在白名單內 則複製該文件到新資料夾
import shutil
import os
import numpy as np
import CopyFilesToAnotherFiles_def as df

db_lab='D:\\project\\LABEL(copy)\\P4_1200_labelled'     #舊標記檔資料夾
dst_db_lab='D:\\project\\label(20)'     #新標記檔資料夾
db_img='D:\\project\\IMG(copy)\\P4_1200_jpg'     #舊照片檔資料夾
dst_db_img='D:\\project\\image(20)'     #新照片檔資料夾

white_list=[15,24,42,43] #4,15,24,27,42,43,0,1,2,5,6,15,27,39,55,63,70,76,78,81
classes = np.zeros(100)  #[0,0,...*100]
for fname in os.listdir(db_lab):
    with open(os.path.join(db_lab, fname), 'r',encoding="utf-8") as f:
        
        if fname=='classes.txt': continue
        txt=f.read().split('\n')[:-1]
        
        if df.isExsisted(txt, white_list): #若編號在白名單內
            arr = [int(s.split(' ')[0]) for s in txt] 
            #將每一行的第一個字串(編號)轉成int並存入arr[]中

            classes[arr]+=1                  #ex.classes[編號]+1

            src_lab=os.path.join(db_lab, fname)
            dst_lab=os.path.join(dst_db_lab, fname)
            imagename=fname.replace('.txt','.jpg') #將標記檔名.txt改成.jpg,找到對應的照片
            src_img=os.path.join(db_img, imagename)
            dst_img=os.path.join(dst_db_img, imagename)

            shutil.copyfile(src_lab, dst_lab)      #複製標記檔案到指定資料夾
            shutil.copyfile(src_img, dst_img)      #複製照片檔案到指定資料夾

#print(arr)
#print(classes)
print(np.argwhere(classes>0)) #返回陣列中所有大於1的數字的索引值(矩陣形式)。
                              #也就是印出有取得1個以上的標籤號碼