import os
import re

def readFile(f):
  rfile = open(f, 'r', encoding='windows-1251')
  txt = rfile.read()
  rfile.close()
  return txt

def writefile(f, txt):
  wfile = open(f, "w", encoding="cp1251")
  wfile.write(txt)

dirs = os.listdir("1")

for f in dirs:
  txt = readFile("1/"+f)
  title = re.findall(r'<title>(.+)</title>', txt)
  raw = re.findall(r'</ana>(.+)</w>(.)', txt)
  s = ''.join(title) + "\n"
  for i in range(len(raw)):
    s = s + ''.join(raw[i]).replace("`","")
  writefile(f+".txt", s)
  print(s)