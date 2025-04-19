"""Вариант 13.
2. Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно вставив после строки N (N – задается пользователем)
произвольную фразу.
"""

import time
from os import path
start = time.time()

#region Config
customText = "---Hello-World----"
inputFileName = 'text18-13.txt'
outputFileName = 'text_output_2.txt'
#endregion 

file_dir = path.dirname(path.abspath(__file__))
InputFilePath = path.join(file_dir, inputFileName)
OutputFilePath = path.join(file_dir, outputFileName)

if not (path.exists(InputFilePath)):
    print(f"Файл по пути <{InputFilePath}> не найден.")
    print("Создайте его в папке с исполняемым файлом")
    print("Выход..\r", end="")
    exit()

with open(InputFilePath, "r", encoding="UTF-16 LE") as f:
    ReadedText:str = f.read()
    allLines:list[str] = ReadedText.splitlines()
    lenLines:int = len(allLines)
    
    print(f"Содержание файла:")
    i=0
    content:list[str] = []
    for l in allLines:
        i+=1
        content.append(f"[{i}] | " + l)
    print("\n".join(content))
    del content, i
    
    lineNum = -1
    while lineNum < 1 or lineNum > lenLines:
        try:
            lineNum = int(input("\nВведите номер строки\n> ").strip())
            if lineNum < 1:
                print("Номер строки должен быть больше 0, повторите попытку")
                continue
            if lineNum > lenLines:
                print(f"Вы не можете ввести больше {lenLines}")
                continue
            break
        except ValueError: print("Неверно ввели число, повторите попытку.")
        except KeyboardInterrupt: print("\r", end="") or exit()
        except EOFError: print("\r", end="") or exit()
        except Exception as e:
            print(f"{e}\nПроизошла ошибка, повторите попытку.")
    
    stringBuilder:list[str] = []
    
    for i in range(1, lenLines+1):
        text = allLines[i-1]
        stringBuilder.append(str(text))
        print(text)
        
        if i == lineNum:
            stringBuilder.append(customText)
            print(customText)
            
    with open(OutputFilePath, "w") as saveFile:
        saveFile.write("\n".join(stringBuilder))

    del stringBuilder, lineNum, allLines, lenLines
print(f"\n\nПрограмма завершила работу. Затраченное время:{(time.time()-start):.3f}")