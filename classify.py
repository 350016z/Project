import os
import random
import shutil

# 將圖片依照比例分配train與val
def train_val_split(imagePath, labelPath, ratio):
    # 檔案順序隨機,且打亂的兩個list順序相同
    randnum = random.randint(0,100)
    random.seed(randnum)
    random.shuffle(imagePath)
    random.seed(randnum)
    random.shuffle(labelPath)

    # 分配訓練或驗證集(依照ratio比例分配)
    pic_num = len(imagePath)  # 總照片數
    train_num = int(pic_num * ratio)   # train的照片數
    train_pic_list = imagePath[:train_num]  # 賦予放入train資料夾的照片路徑
    train_voc_list = labelPath[:train_num]  # 賦予放入train資料夾的標記檔路徑
    val_pic_list = imagePath[train_num:]    # 賦予放入val資料夾的照片路徑
    val_voc_list = labelPath[train_num:]    # 賦予放入val資料夾的標記檔路徑

    print('1. 分配train與val資料集：完成')
    print('-'*50)

    return train_pic_list,train_voc_list, val_pic_list,val_voc_list

# 移動圖片到train與val資料夾
def split_images_to_train_and_val(source, train_pic_list,train_voc_list, val_pic_list,val_voc_list):
    # 創建圖片train與val資料夾以及train與val底下的image,label資料夾
    folder_t = os.path.join(source, 'train')  #train
    if not os.path.exists(folder_t):
        os.makedirs(folder_t)
    folder_t1 = os.path.join(source, 'train/image')
    if not os.path.exists(folder_t1):
        os.makedirs(folder_t1)
    folder_t2 = os.path.join(source, 'train/label')
    if not os.path.exists(folder_t2):
        os.makedirs(folder_t2)
    folder_v = os.path.join(source, 'val')
    if not os.path.exists(folder_v):
        os.makedirs(folder_v)
    folder_v1 = os.path.join(source, 'val/image')
    if not os.path.exists(folder_v1):
        os.makedirs(folder_v1)
    folder_v2 = os.path.join(source, 'val/label')
    if not os.path.exists(folder_v2):
        os.makedirs(folder_v2)

    # 移動圖片到資料夾
    for move_it in train_pic_list:
        shutil.move(move_it, move_it.replace('images', 'train/image'))  
        #shutil.move(old,new):將舊路徑的檔案移動到新路徑內
    for move_it in train_voc_list:
        shutil.move(move_it, move_it.replace('label', 'train/label'))  
    for move_it in val_pic_list:
        shutil.move(move_it, move_it.replace('images', 'val/image'))
    for move_it in val_voc_list:
        shutil.move(move_it, move_it.replace('label', 'val/label'))
    print('2. 移動圖片與voc標籤到train與val資料夾：完成')

if __name__ == '__main__':
    source = './datasets2/'
    # 讀取標籤類別
    with open(os.path.join(source, 'classes.txt'), encoding='utf-8') as f:
        classes = f.read().strip().split() # strip([char]):將str內的char刪除後返回

    # label資料夾路徑
    labelDir = os.path.join(source, 'label/')
    # label檔案路徑
    labelPath = os.listdir(labelDir)
    labelPath = [labelDir + i for i in labelPath]
    # labPath此時為儲存label資料夾底下每個label檔的完整路徑的列表

    # image資料夾路徑
    imageDir = os.path.join(source, 'images/')
    # image檔案路徑
    imagePath = os.listdir(imageDir)   # os.listdir()返回imageDir路徑底下的資料夾或檔案名稱
    imagePath = [imageDir + i for i in imagePath] 
    # imagePath此時為儲存images資料夾底下每個image的完整路徑的列表

    train_pic_list,train_voc_list, val_pic_list,val_voc_list = train_val_split(imagePath, labelPath, 0.8)
    split_images_to_train_and_val(source, train_pic_list,train_voc_list, val_pic_list,val_voc_list)