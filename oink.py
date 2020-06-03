#!/usr/bin/python3

#pig script it's calling:

"""
lines = LOAD '/home/chuck/test.txt' AS (line:chararray);
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) as word;
grouped = GROUP words BY word;
wordcount = FOREACH grouped GENERATE group, COUNT(words);
STORE wordcount INTO '/home/chuck/python_piggy/result.txt' using PigStorage(';');
"""
import subprocess as s
pigpath = [ "pig","/home/chuck/output.pig"]
oink = s.run(pigpath)

print("Th-Th-The, Th-Th-The, Th-Th... That's all, folks!")

