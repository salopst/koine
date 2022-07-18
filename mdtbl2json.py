#!/usr/bin/env python3
# 2022-07-18T06:57:13+0100
import getopt, sys
import json
from os.path import exists as file_exists


koine_table='''| s_no | m_no | Freq. | lexeme     | Gen.. | Art.  | POS       | gloss_en                                                               |
| ---- | ---- | ----- | ---------- | ----- | ----- | --------- | ---------------------------------------------------------------------- |
| 716  | 41   | 55    | ἀρχή       | ῆς    | ἡ     | s1f       | beginning, first, authority, ruler                                     |
| 1041 | 42   | 1041  | γάρ        | --    | --    | con       | (postpositive) for, indeed, because                                    |
| 0000 | 43   | 708   | εἶπεν      | --    | __    | vaia3s    | he said (from εἶπον with movable nu.)                                  |
| 1519 | 44   | 1768  | εἰς        | --    | --    | p+acc     | into                                                                   |
| 1849 | 45   | 102   | ἐξουσία    | ας    | ἡ     | s1f       | authority, power, jurisdiction                                         |
| 2098 | 46   | 76    | εὐαγγέλιον | ου    | τό    | s2n       | gospell, good news                                                     |'''

def mdtbl2json(table):
  lines = table.split('\n')
  ret=[]
  keys=[]
  for i,l in enumerate(lines):
    if i==0:            # first line is the header
      keys=[_i.strip() for _i in l.split('|')]
    elif i==1: continue # second line is the header seperator. i.e. "---"
    else:               # subsequent lines are data
      # ignore first and last '|'
      ret.append({keys[_i]:v.strip() for _i,v in enumerate(l.split('|')) if  _i>0 and _i<len(keys)-1})
  return json.dumps(ret, indent = 2, ensure_ascii=False)

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
     opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
     print ('mdtbl3json.py -i <inputfile> -o <outputfile>')
     sys.exit(2)
  for opt, arg in opts:
     if opt == '-h':
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit()
     elif opt in ("-i", "--ifile"):
        inputfile = arg
     elif opt in ("-o", "--ofile"):
        outputfile = arg
  print(f'inputfile: {inputfile}')
  print(f'outputfile: {outputfile}')

  if file_exists(inputfile):
    inp = open(inputfile, "r")
    data = inp.read()
    print(f'Input: {data}\n=========================')
    json_data = mdtbl2json(data)
    print(f'Output: {json_data}\n=========================')
    with open(outputfile, 'w', encoding='utf-8') as f:
      json.dump(json_data, f, indent = 2, ensure_ascii=False)
    inp.close()
  else:
    print(f'File {inputfile} does not exist')
  
import json


if __name__ == "__main__":
  main(sys.argv[1:])
