import cv2
import numpy as np

def main():
    image_path = "image/1.jpg"
    frame = cv2.imread(image_path)  # 讀取圖片
    
    if frame is None:
        print("Error: 無法讀取圖片")
        return
    
    # 調整視窗大小
    scale_percent = 50  # 設定縮放比例 (50% 大小)
    width = int(frame.shape[1] * scale_percent / 500)
    height = int(frame.shape[0] * scale_percent / 500)
    dim = (width, height)
    
    frame_resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    
    # 進行圖像分割 (轉為灰階並尋找輪廓)
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)  # 使用 Canny 邊緣檢測來進行圖像分割
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    segmented = frame_resized.copy()
    cv2.drawContours(segmented, contours, -1, (0, 255, 0), 2)  # 用綠色繪製輪廓
    
    cv2.imshow('Original', frame_resized)  # 顯示縮小後的原始影像
    cv2.imshow('Segmented', segmented)  # 顯示縮小後的圖像分割結果
    
    cv2.waitKey(0)  # 等待按鍵按下
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
