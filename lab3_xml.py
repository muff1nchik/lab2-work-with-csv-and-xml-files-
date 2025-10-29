import xml.etree.ElementTree as ET


def get_info(file):
    tree = ET.parse(file)
    root = tree.getroot()

    num_codes = []
    char_codes = []

    for valute in root.findall("Valute"):
        num_code = valute.find("NumCode").text
        char_code = valute.find("CharCode").text

        num_codes.append(int(num_code))
        char_codes.append(char_code)

    return num_codes, char_codes

num, char = get_info("currency.xml")
print("NUMS: ")
print(*num, sep=", ")
print("CHARS: ")
print(*char, sep=", ")