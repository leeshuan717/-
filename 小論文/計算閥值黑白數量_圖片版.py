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
    
    # 轉為灰階並進行閥值處理
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    white_pixels = np.sum(thresh == 255)
    black_pixels = np.sum(thresh == 0)
    
    print(f'White pixels: {white_pixels}, Black pixels: {black_pixels}')
    
    cv2.imshow('Original', frame_resized)  # 顯示縮小後的原始影像
    cv2.imshow('Threshold', thresh)  # 顯示縮小後的閥值處理影像
    
    cv2.waitKey(0)  # 等待按鍵按下
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
