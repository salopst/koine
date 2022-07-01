#!/usr/bin/env python3
# ---
# title: "Scrape Mounce for Koine words"
# author: salopst
# date: 2022-06-29T07:19:29+01:00
# lastmod: NULL
# filename: "~/Projects/koine/scrape-mounce.py"
# refs:
# -  https://biblehub.com/greek/4653.htm
# - https://www.blueletterbible.org/lexicon/g4653
# ---

# ```bash
# shuf -i 1-5624 -n 1
# ```

import requests
from bs4 import BeautifulSoup
import random

STRONGS_MAX  = 5624
strongs_used = []
strongs_new  =   random.randint(1,STRONGS_MAX)
strongs_used = strongs_used.append(strongs_new)
strongs_str  = str(strongs_new) 

word_url = "https://www.blueletterbible.org/lexicon/g"+strongs_str
response = requests.get(word_url)
soup = BeautifulSoup(response.text, 'html.parser')

# blueletter
strongs_entry = soup.find('div', class_='lexStrongsDef').text
print(f"{strongs_entry}")
print(f" {word_url}\n")

# Eg output:
#
# μνῆμα mnēma, mnay'-mah; from G3415; a memorial, i.e. sepulchral monument
# (burial-place):—grave, sepulchre, tomb.
#
# https://www.blueletterbible.org/lexicon/g3418