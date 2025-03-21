import time
start = time.time()
with open("text18-13.txt", "r", encoding="UTF-16 LE") as f:
    abc = f.read()
    print(f"Содержание файла:\n{abc}")

    all_lines = abc.splitlines()
    len_lines = len(all_lines)

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

print(f"\n\nПрограмма завершила работу. Затраченное время:{time.time()-start}")