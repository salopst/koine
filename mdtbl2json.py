#!/usr/bin/env python3
# 2022-07-18T06:57:13+0100
import json

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

print(mdtbl2json(koine_table))
