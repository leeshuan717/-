import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)  # 開啟鏡頭
    
    if not cap.isOpened():
        print("Error: 無法開啟攝影機")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: 無法讀取影像")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉為灰階
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 閥值處理
        
        white_pixels = np.sum(thresh == 255)
        black_pixels = np.sum(thresh == 0)
        
        print(f'White pixels: {white_pixels}, Black pixels: {black_pixels}')
        
        cv2.imshow('Original', frame)  # 顯示原始影像
        cv2.imshow('Threshold', thresh)  # 顯示閥值處理後影像
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 退出
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
