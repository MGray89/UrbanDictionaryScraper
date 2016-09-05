# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 20:02:52 2016

@author: Matthew
"""

from lxml import html
import requests

input_word = input('Enter Word to Define: ')

page = requests.get('http://www.urbandictionary.com/define.php?term=' + input_word)
tree = html.fromstring(page.content)

word_meanings = tree.xpath('//div[@class="meaning"]/text()')

# Clear screen easy way
print("\n" * 100)

print('Resultant Definitions for "' + input_word + '"')
print(' ')

for definition_line in word_meanings:
    print(definition_line.strip())

