#將資料夾裡的txt檔案relabel
#!!只能relabel一次 因為新的numbers也會被改動!!

import os
dst_db='E:\\project\\label_31RE'  #標記檔的資料夾

def relabel(file, label_map):
    txt=None
    with open(file, 'r') as f:           
        txt=f.read().split('\n')[:-1]    
        #txt = ['1 0.643631 0.535417 0.037760 0.043056', '1 0.611731 0.369444 0.022917 0.031481',...]
    #print(txt[i])
    
    for i in range(len(txt)):    #len(txt):表示同一個txt檔內有幾個標籤數
                                 #range(n):[0,1,2...n-1]
        
        cls_id, s=txt[i].split(' ', 1)
        #print(txt[i])   #txt[i] = 1 0.643631 0.535417 0.037760 0.043056
        #split('',num):num為分割為num+1個字符串  
        #print(cls_id)   #cls_id = 1
        #print(s)        #s = 0.643631 0.535417 0.037760 0.043056
        #cls_id = 切割出的第一個值(number) ; s = 切割出的第二個值(coordinate)

        #try 區段內的程式發生錯誤時，就會執行 except 裡的內容，如果 try 的程式沒有錯誤，就不會執行 except 的內容
        try:
            cls_id=label_map[cls_id]    #此時cls_id已經為新的編號
        except:
            cls_id=int(cls_id)

        txt[i]=f'{cls_id} {s}'          ##txt[i] = 改寫編號 0.643631 0.535417 0.037760 0.043056
    
    #存檔  
    with open(file, 'w') as f:   #'w':覆寫
        for s in txt:
            f.write(s+'\n')

        
#字典  #若輸入字串為78則轉換為數字1 
class_map={'3':31, '7':31, '8':31, '9':31, '10':31, '12':31, '13':31,  '16':31,      #0,1,2,4,5,6,15
           '17':31, '19':31, '20':31, '21':31, '22':31, '23':31, '25':31, '28':31, '29':31,  #18,24,27
           '31':31, '32':31, '34':31, '35':31, '36':31, '38':31, '40':31, '41':31,  #39,42,43
           '44':31, '45':31, '46':31, '47':31, '48':31, '50':31, '52':31, '53':31,  #55,63
           '56':31, '57':31, '58':31, '59':31, '60':31, '61':31, '62':31, '64':31,
           '66':31, '67':31, '68':31, '69':31, '71':31, '72':31, '73':31, '74':31, '76':31,  #70
           '77':31, '79':31, '80':31, '82':31, '83':31, '84':31, '85':31, '86':31, '87':31, '88':31,  #78,81
           '89':31, '90':31, '91':31, '92':31, '93':31, '94':31, '95':31, '96':31, '97':31, '99':31,  #98

           '4':3,   '5':4,   '6':5,   '78':6,  '15':7,  '18':8,  '55':9,  '98':10, '11':20, '14':21, 
           '39':12, '42':13, '43':14, '63':15, '70':16, '81':17, '27':18, '26':19, '24':11, '30':22,
           '33':23, '37':24, '49':25, '51':26, '54':27, '65':28, '75':29,
          }    

# 4 >> 3
# 5 >> 4
# 6 >> 5
# 15 >> 6
# 18 >> 7
# 24 >> 8
# 26 >> 9
# 27 >> 10
# 39 >> 11
# 42 >> 12
# 43 >> 13
# 55 >> 14
# 63 >> 15
# 70 >> 16
# 78 >> 17
# 81 >> 18
# 其他(包括76_unknown) >> 31


for fname in os.listdir(dst_db):
    file=os.path.join(dst_db, fname)  #將所有txt檔路徑存至file變數
    relabel(file, class_map)          #讓每個file檔都依照class_map 設定的變數改變