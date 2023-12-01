usage: script.py [-h] [-f FILENAME] [-nfe EXTENSION] [-nft TEXT] [-cfs FILENAME] [-asc FILENAME]

options:
  -h, --help            show this help message and exit
  -f FILENAME, --file FILENAME
                        File name
  -nfe EXTENSION, --new-file-extension EXTENSION
                        Change file extension
  -nft TEXT, --new-file-text TEXT
                        Paste text into file
  -cfs FILENAME, --check-file-size FILENAME
                        Check file size
  -asc FILENAME, --a-symbol-count FILENAME
                        Get a symbol count

Зміна розширення файлів:
python .\script.py -f .\text1.txt -nfe ".log"

Заповнення файлів будь-якими даними через введення з консолі:
python .\script.py -f .\text2.txt -nft "Привіт світ!!!11111"

Перевірка розміру файлу, якщо розмір менший за 5КБ, тоді збільшити його розмір до 5КБ будь-якими текстовими даними:
python .\script.py -cfs .\text2.txt

Вивести кількість символів "а" (літера українською мовою) у файлі:
python .\script.py -asc .\text2.txt
