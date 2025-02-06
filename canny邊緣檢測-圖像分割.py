import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)  # 開啟筆電的鏡頭
    
    if not cap.isOpened():
        print("Error: 無法開啟攝影機")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: 無法讀取影像")
            break
        
        # 進行圖像分割 (轉為灰階並尋找輪廓)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)  # 使用 Canny 邊緣檢測來進行圖像分割
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        segmented = frame.copy()
        cv2.drawContours(segmented, contours, -1, (0, 255, 0), 2)  # 用綠色繪製輪廓
        
        cv2.imshow('Original', frame)  # 顯示原始影像
        cv2.imshow('Segmented', segmented)  # 顯示圖像分割結果
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 退出
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
