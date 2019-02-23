# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:05:38 2019

@author: steph
"""

import re

with open('plain_story.txt', 'rt', encoding = 'utf-8') as fin:

    story = fin.readlines()

with open('Alice_thought.txt', 'wt', encoding = 'utf-8') as fout:

    lines_Alice, lines_Alice_thought = 0, 0

    for line in story:

        if re.match('Alice', line):
            lines_Alice += 1

            if re.search('thought', line):
                lines_Alice_thought += 1
                fout.write(line)

    fout.write(str(lines_Alice) + ' lines begin with the word "Alice"\n')
    fout.write(str(lines_Alice_thought) + ' lines begin with the word Alice and include the characters "thought"\n')    