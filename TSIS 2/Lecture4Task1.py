import re
import csv


file = open("raw.txt","r", encoding="utf 8")
text = file.read()


BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)" 
ZNMPattern = r"\nЗНМ.*(?P<ZNM>\b.+)"
KASSAPatern = r"\nКасса\s(?P<KASSA>\b.+)"
BILLPattern = r"\nЧек\s*(?P<BILL>\b.+)"
DATEANDTIMEPattern = r"\nВремя\s*(?P<DATEANDTIME>\b.+)\n{1}(?P<ADRESS>.*)"

BINText = re.search(BINPattern, text).group("BIN")
ZNMText = re.search(ZNMPattern, text).group("ZNM")
KASSAText = re.search(KASSAPatern, text).group("KASSA")
BILLText = re.search(BILLPattern, text).group("BILL")
DATEANDTIMEText = re.search(DATEANDTIMEPattern, text).group("DATEANDTIME")
ADRESSText = re.search(DATEANDTIMEPattern, text).group("ADRESS")

itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)


items = [["БИН","ЗНМ","Касса","Чек","Наименование товара","Цена за единиц","Кол-во","Сумма","Дата и Время","Адрес"]]

for m in re.finditer(itemPattern, text):
    items.append([BINText,ZNMText,KASSAText,BILLText,m.group("name").strip(),m.group("price").strip(), m.group("count").strip(),m.group("total1").strip(),DATEANDTIMEText,ADRESSText])

with open('file.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)

file.close()