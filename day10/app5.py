#EasyOCR - Deep Learning models

import easyocr

reader = easyocr.Reader(["en"], gpu=False)
print(reader)
result = reader.readtext("gpay.jpg", detail=0)
print(result)