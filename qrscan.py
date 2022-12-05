import zxing


def scan(image_path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(image_path)
    codeCotent = barcode.parsed  # type: ignore

    if codeCotent == "":
        return False
    elif(codeCotent.isdigit() and len(codeCotent) == 3):  # type: ignore
        return codeCotent
    else:
        return False
