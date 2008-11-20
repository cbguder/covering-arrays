#!/bin/sh

./failure-simulator.py input/configuration-model.xml input/2way.csv input/failure-patterns.xml | tidy -qi -xml
