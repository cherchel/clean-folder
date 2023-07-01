from clean import rename_files, sort

if __name__ == '__main__':
    path = input("Введи пусть к папке: ")
    rename_files(path)                      # все файлы в указанной папке - стандартизируются(нормализируются)
    sort(path)                              # происходит сортировка файлов по папкам согласно их расширениям
