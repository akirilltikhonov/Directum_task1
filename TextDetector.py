import cv2
import pytesseract


class TextDetector:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def detect_text(self):
        img = cv2.imread(r".\1.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        words = pytesseract.image_to_data(img)
        # print(words)

        text = ''
        for x, word in enumerate(words.splitlines()):
            if x != 0:
                word = word.split()
                if len(word) == 12:
                    x, y, w, h = int(word[6]), int(word[7]), int(word[8]), int(word[9])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    # print(word)
                    text += word[11] + ' '

        # print(text.strip())
        # cv2.imshow('result', img)
        # cv2.waitKey(0)
        return text.strip()
