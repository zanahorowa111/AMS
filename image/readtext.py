from PIL import Image
import pytesseract
import cv2

image_path = r'E:\python\Namless_project\image\images.png'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
pil_image = Image.fromarray(threshold_image)
custom_config = r'--oem 3 --psm 6'
extracted_text = pytesseract.image_to_string(pil_image, config = custom_config)

print(extracted_text)