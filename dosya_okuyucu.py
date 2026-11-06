import cv2
import pytesseract
import pandas as pd
from PIL import Image
import numpy as np

def capture_text_from_camera():
    cap = cv2.VideoCapture(0)
    text_list = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        
        if text.strip():
            text_list.append(text.strip())
        
        cv2.imshow("Live Text Capture", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return text_list

def save_text_to_excel(text_list, output_path):
    df = pd.DataFrame({'Extracted Text': text_list})
    df.to_excel(output_path, index=False)

def main(output_excel):
    text_list = capture_text_from_camera()
    save_text_to_excel(text_list, output_excel)
    print(f"Extracted text saved to {output_excel}")

# Example usage
main("output.xlsx")
