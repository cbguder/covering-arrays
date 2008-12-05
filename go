#!/bin/sh

./failure-simulator.py -f arff -o output/results input/configuration-model.xml input/2way.csv input/failure-patterns.xml
for file in `ls output/*.arff`; do
	java -cp weka/weka.jar weka.classifiers.trees.J48 -t $file -i > $file.tree
done
