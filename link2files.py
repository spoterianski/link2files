#!/usr/bin/env python
# coding: utf-8
# 2013 by Sergey Poterianski

import argparse
import sys

class Linker():
    """Linking class"""
    def __init__(sel):
        pass

    def LinkFiles(self, keynum1, keynum2, file1, file2):
        """
        Link two files by key fileds.
        """
        keys = {}
        keynum1 = keynum1 -1
        keynum2 = keynum2 -1
        if keynum1 < 0 or keynum2 < 0:
            sys.exit("Error: number key field < 1")

        # read first file
        k = open(file1)
        while 1:
            klines = k.readlines(100000)
            if not klines:
                break
            for line in klines:
                if len(line.strip()) == 0:
                    continue
                vals = line.strip().split('\t')
                if len(vals) < keynum1 + 1:
                    continue
                if vals[keynum1].strip() == '':
                    continue
                key = vals[keynum1].strip()
                if keys.has_key(key):
                    keys[key].append(line.strip())
                else:
                    keys[key] = [line.strip()]

        # read second file
        d = open(file2)
        while 1:
            dlines = d.readlines(100000)
            if not dlines:
                break
            for line in dlines:
                if len(line.strip()) == 0:
                    continue
                vals = line.strip().split('\t')
                if len(vals) < keynum2 + 1:
                    continue
                if vals[keynum2].strip() == '':
                    continue
                key = vals[keynum2].strip()
                if keys.has_key(key):
                    for key_val in keys[key]:
                        # print result
                        print(key_val + '\t' + line.strip())
        return 0


def main():
    # parse command line arguments
    parser = argparse.ArgumentParser(description='link2files - this is small'\
        ' tool for linking two tab-delimeted files.')
    parser.add_argument('-f1k', '--file1key', type=int, help='Key field in first file. default=1', default=1)
    parser.add_argument('-f2k', '--file2key', type=int, help='Key field in second file. default=1', default=1)
    parser.add_argument('-k', '--keys', help='File with keys', required=True)
    parser.add_argument('-f', '--data', help='File with data', required=True)
    myargs = parser.parse_args()

    # call linker
    linker = Linker()
    if linker.LinkFiles(myargs.file1key, myargs.file2key, myargs.keys, myargs.data) != 0:
        parser.print_usage()

if __name__ == '__main__':
    main()
