
# Склеивалка двух файлов

Склеиват два файла по задданному полю. Номера полей в задаются аргументом -f1k и -f2k. Результат выводится в консоль только для склеенных строк.

## Usage

    link2files -k1f 1 -k2f 1 -k [FIRST FILE] -f [SECOND FILE]
    optional arguments:
      -h, --help            show this help message and exit
      -f1k FILE1KEY, --file1key FILE1KEY
                            Key field in first file. default=1
      -f2k FILE2KEY, --file2key FILE2KEY
                            Key field in second file. default=1
      -k KEYS, --keys KEYS  File with keys
      -f DATA, --data DATA  File with data
