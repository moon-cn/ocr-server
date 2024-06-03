from paddleocr import PaddleOCR




def parse(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    result = ocr.ocr(image_path, cls=True)
    return result


if __name__ == '__main__':
    jpg = "test/1.pdf"
    parse(jpg)