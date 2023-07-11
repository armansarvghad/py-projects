import cv2
from pyzbar import pyzbar

def scan_barcodes(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        text = "{} ({})".format(barcode_data, barcode_type)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Barcode Scanner", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "path_to_your_image.jpg"
scan_barcodes(image_path)