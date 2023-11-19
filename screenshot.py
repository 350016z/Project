import cv2
import os

# 定義影片路徑和圖像儲存路徑
video_path ="C:/Users/longlong_dick/Desktop/desktop/novel/bang_vs_rj_20230216.mp4"
image_path ="C:/Users/longlong_dick/Desktop/desktop/novel/ddd"

# 確保圖像儲存路徑存在
if not os.path.exists(image_path):
    os.makedirs(image_path)

# 定義擷取圖像的時間間隔（以幀為單位）
interval = 300

# 使用OpenCV讀取影片
cap = cv2.VideoCapture(video_path)

# 計數器，用於命名圖像文件
count = 0

# 迴圈遍歷影片幀，每隔一段時間擷取一個圖像
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        count += 1
        
        if count % (interval) == 0:
            # 將幀轉換為灰度圖像
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 儲存圖像文件
            cv2.imwrite(os.path.join(image_path, f"image_{count}.jpg"), gray)
            
    else:
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()