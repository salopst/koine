#!/usr/bin/env python3
# ---
# title: "Scrape Mounce for Koine words"
# author: salopst
# date: 2022-06-29T07:19:29+01:00
# lastmod: NULL
# filename: "~/Projects/koine/scrape-mounce.py"
# refs:
# -  https://www.billmounce.com/greek-dictionary/toc/alpha
# ---

from cgitb import text
import json
import requests
from bs4 import BeautifulSoup

# Strong's Numbers are an index of every word in the original Hebrew and Greek texts of the Bible.

# GK Numbers (Goodric-Colenberger III) An alternative, an attempt at rectifying some deficiencies of the strong's numbers. https://www.ph4.org/strong_gkstrong.php

base_url = 'https://www.billmounce.com/greek-dictionary/toc/'

GREEK_LETTERS=['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']

for greek_letter in GREEK_LETTERS:
  letter_url = base_url + greek_letter
  print(letter_url)
  # scrape the letter
  # response = requests.get(letter_url)

letter_url = base_url + 'gamma'
response = requests.get(letter_url)
soup = BeautifulSoup(response.text, 'html.parser')


# create word object:
greek_words = [] 
table = soup.find('table')
for row in table.tbody.find_all('tr'):    
  # Find all data for each column
  columns    = row.find_all('td')
  greek_words.append({"strongs": columns[0].text,
                      "GK": columns[1].text,
                      "link": base_url+columns[3].a['href'],
                      "greek": columns[2].span.text,
                      "roman": columns[3].text,
                      "gloss": columns[4].text,
                      })
for w in greek_words:
  print(f"FUCKER....{w}")

with open("words_from_mounce.json", "w") as writeJSON:
   json.dump(greek_words, writeJSON, ensure_ascii=False)

with open("words_from_mounce.md", "w") as f:
  for k,v in greek_words:
    write("%s:%s\n" % (k,v))
