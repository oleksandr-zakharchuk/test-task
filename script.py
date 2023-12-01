# -*- coding: utf-8 -*-
from pathlib import Path
from argparse import ArgumentParser
import math
import random

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="File name", metavar="FILENAME")
parser.add_argument("-nfe", "--new-file-extension", dest="new_file_extension", help="Change file extension", metavar="EXTENSION")
parser.add_argument("-nft", "--new-file-text", dest="new_file_text", help="Paste text into file", metavar="TEXT")
parser.add_argument("-cfs", "--check-file-size", dest="check_file_size", help="Check file size", metavar="FILENAME")
parser.add_argument("-asc", "--a-symbol-count", dest="a_symbol_count", help="Get a symbol count", metavar="FILENAME")

args = parser.parse_args()

if args.filename is not None and args.new_file_extension is not None:
    p = Path(args.filename)
    if p.is_file():
        new_filename = p.rename(p.with_suffix(args.new_file_extension))
        print(f"Extension has been successfully changed. New filename: {new_filename}")
    else:
        print(f"Error: file {args.filename} doesn't exist")
elif args.filename is not None and args.new_file_text is not None:
    with open(args.filename, "w") as f:
        contents = "".join(args.new_file_text)
        f.write(contents)
elif args.check_file_size is not None:
    p = Path(args.check_file_size)
    current_size = p.stat().st_size
    print(f"{args.check_file_size} current size: {convert_size(current_size)}")
    while p.stat().st_size <= 5120: # 5 KB = 5120 B
        with open(args.check_file_size, "a") as f:
            f.write(random.choice("АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя"))
    new_size = p.stat().st_size
    if current_size != new_size:
        print(f"{args.check_file_size} new size: {convert_size(new_size)}")
elif args.a_symbol_count is not None:
    with open(args.a_symbol_count, "r") as f:
        print(f"а (in Ukrainian) symbol count in {args.a_symbol_count} file: {f.read().count('а')}")
