import xml.etree.ElementTree as ET


def get_info(filename):
    tree = ET.parse(filename) #открыли файл
    root = tree.getroot() #создали "родительский обьект", предсавляющий структуру <ValCurs>

    num_codes = []
    char_codes = []

    for valute in root.findall("Valute"): #ищу все теги "Valute" внутри обьекта
        num_code = valute.find("NumCode").text # find ищет тег "Numcode" внутри обьекта valute, textg получает текст внутри
        char_code = valute.find("CharCode").text

        num_codes.append(int(num_code))
        char_codes.append(char_code)

    return num_codes, char_codes


num, char = get_info("currency.xml")
print("NUMS: ")
print(*num, sep=", ")
print("CHARS: ")
print(*char, sep=", ")