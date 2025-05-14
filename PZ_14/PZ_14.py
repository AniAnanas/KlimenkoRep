"""Вариант 13.
В строках исходного текстового файла (dates1.txt) все даты представить в виде
подстроки. Поместить в новый текстовый файл все даты февраля в формате
ДД/ММ/ГГГГ.
"""
from os import path
import re
content = r"""01.02.2022; 02.02.2022; 03.02.2022 
04.02.2022, 05.02.2022 05.03.2022 05.03.2022 05.03.2022 05.03.2022 
6.2.2022, 07.02.2022, 08.02.2022 
09.02.2022; 
10.02.2022; 11.02.2022; 12.02.2022, 
13.2.2022, 14.02.2022; 
15.02/2022, 16.02.2022; 17.02.2022 
18.02\2022 
1\2/2 
20.02.2022, 21.02.2022 
22.02.2022 
23.02.2022 
24.02.2022; 25.02.2022; 26.02.2022, 
27.02.2022, 28.02.2022 
"""
dirname = path.dirname(__file__)
path2file = path.join(dirname, "dates1.txt")
if (not path.exists(path2file)):
    with open(path2file, "w") as f:
        f.write(content)

with open(path2file) as orig:
    text = orig.read()

Re = re.compile(r"[0-3]?\d[.\\/][01]?\d[.\\/]\d{1,4}")
matched_dates = Re.findall(text)
print("\n", matched_dates, "\n"*3)

reFeb = re.compile(r'[0-3]?\d[.\\/]0?2[.\\/]\d{1,4}')
formated_dates = [
    "/".join([
        part.zfill(2) if i < 2 else part.zfill(4) for i, part in enumerate(re.split(r'[.\\/]', date))
    ]) 
    for date in matched_dates 
    if reFeb.fullmatch(date) is not None
]

with open(path.join(dirname, "captured_dates.txt"), "w") as wfile:
    wfile.write("\n".join(formated_dates))
print(formated_dates)
