#!/usr/bin/env python3
# -*- coding:utf-8 -*-

fileTuple = ("example/dbp.txt", "example/pbd.txt")

def readFile(filename):
  with open(filename, encoding="utf-8") as f:
    content = f.read()
  return content

def processFile(filename):
  content = readFile(filename)
  return map(content.count, ("婦人", "土狗", "男"))

if __name__== "__main__":
  for idx, filename in enumerate(fileTuple):
    x, y, z = processFile(filename)
    print(filename, [("婦人", x), ("土狗", y), ("男", z)])
