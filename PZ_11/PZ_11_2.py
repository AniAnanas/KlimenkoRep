import time
from os import path
start = time.time()

file_dir = path.dirname(path.abspath(__file__))
path2file = path.join(file_dir, 'text18-13.txt')

if not (path.exists(path2file)):
    print(f"Файл по пути <{path2file}> не найден.")
    print("Создайте его в папке с исполняемым файлом")
    print("Выход..\r", end="")
    exit()

with open(path2file, "r", encoding="UTF-16 LE") as f:
    abc = f.read()
    all_lines = abc.splitlines()
    len_lines = len(all_lines)
    
    i=0
    print(f"Содержание файла:")
    for line in all_lines:
        i+=1
        print(f"[{i}] | "+line)

    num_line = -1
    while num_line < 1 or num_line > len_lines:
        try:
            num_line = int(input("\nВведите номер строки\n> ").strip())
            
            if num_line < 1:
                print("Номер строки должен быть больше 0, повторите попытку")
                continue
            
            if num_line > len_lines:
                print(f"Вы не можете ввести больше {len_lines}")
                continue
            
            break
        
        except ValueError: print("Неверно ввели число, повторите попытку.")
        except KeyboardInterrupt: print("\r", end="") or exit()
        except EOFError: print("\r", end="") or exit()

    for i in range(1, len_lines+1):
        print(all_lines[i-1])
        if i == num_line:
            print("---Hello-World----")

print(f"\n\nПрограмма завершила работу. Затраченное время:{(time.time()-start):.3f}")