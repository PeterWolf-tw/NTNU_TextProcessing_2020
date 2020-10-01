#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import json

with open("example/example.txt") as f:
  content = [i.strip() for i in f.readlines()]

regex1 = r"出生 (\d+) 年 (\d+) 月 (\d+) 日（(\d+)歲）"
matches = re.finditer(regex1, str(content), re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
  birth = match.groups()
  
  regex2 = r"配偶 (.*?)（"
  matches2 = re.finditer(regex2, str(content[6]), re.MULTILINE)

  for matchNum1, match1 in enumerate(matches2, start=1):
    spouse = match1.groups()
    target = {
        "name": {"zh":content[0].split()[1], "en":content[1].replace("英文名 ", "")},
        "birth": {"year":birth[0], "month":birth[1], "date":birth[2]},
        "job": content[3].replace("職業", "").strip(),
        "language":content[4].replace("語言", "").strip().split("、"),
        "education":content[5].replace("教育程度", "").strip().split("、"),
        "spouse":spouse[0]
    }
    with open("week03_40947026s.json", 'w') as f2:
      f2.write(json.dumps(target, ensure_ascii=False) + '\n')
    with open("week03_40947026s.json", 'r') as f3:
      print([j.strip() for j in f3.readlines()][0])

