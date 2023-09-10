import os

# Получаем список файлов в папке
folder_path = r'C:\Users\Пк\Desktop\py-homework-basic-files\2.4.files\sorted'
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Создаем пустой список для хранения содержимого файлов
file_contents = []

# Читаем содержимое каждого файла и сохраняем информацию о количестве строк и содержимое вместе
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:  #  указываем корректную кодировку файла
        lines = f.readlines()
        num_lines = len(lines)
        file_contents.append((file_name, num_lines, lines))

# Сортируем содержимое файлов по количеству строк
file_contents.sort(key=lambda x: x[1])

# Записываем отсортированное содержимое в результирующий файл
result_file_path = r'C:\Users\Пк\Desktop\py-homework-basic-files\2.4.files\sorted\text'
with open(result_file_path, 'w', encoding='utf-8') as f:  # указываем корректную кодировку файла
    for file_info in file_contents:
        file_name, num_lines, lines = file_info
        f.write(file_name + '\n')
        f.write(str(num_lines) + '\n')
        f.writelines(lines)

print('Объединение файлов завершено.')