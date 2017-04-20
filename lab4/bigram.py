from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    sentences = lines.glom() \
                  .map(lambda x: " ".join(x)) \
                  .flatMap(lambda x: x.split("."))

    #Your code goes here
    Mycoll = sentences.collect()
    def GenBig(Coll):
    	prevWord = None
    	result =[ ]
   	for sentence in Coll:
        	sentence = sentence.strip()
        	Isfirst = True
       	 	words = sentence.split(' ')
        	for word in words:
            		if(Isfirst):
                		prevWord = word
               	 		Isfirst = False
            		else: 
                		result.append(((prevWord,word),1))
                		prevWord = word
    	return result    

    temp = GenBig(Mycoll)
    t2 = sc.parallelize(temp)
    t3 = t2.reduceByKey(lambda x,y: x+y)
    t3.saveAsTextFile("FullBigram.out")
    t4 = t3.sortBy(lambda x: x[1], False)  
    ToText = t4.take(100)  
    ToTxt = sc.parallelize(ToText)
    ToTxt.saveAsTextFile("Bigram.out")





    sc.stop()
