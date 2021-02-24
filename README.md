# EXTRACTOR

EXTRACTOR helps to extract the system level attack behavior from unstructured threat reports. EXTRACTOR leverages Natural Language Processing (NLP) techniques to transform a raw threat report into a graph representation.

## Instructions
### Requirements

This repository uses `python 3.5+` and has the following requirements:
```
nltk == 3.4.5
spaCy == 2.1.0
allennlp == 0.8.4
neuralcoref == 4.0.0
graphviz == 0.13.2
textblob == 0.15.3
pattern == 3.6
numpy == 1.18.1
```
You can directly install the requirements using `pip install -r requirements.txt`


### Usage 

Run EXTRACTOR with `python3 main.py [-h] [--asterisk ASTERISK] [--crf CRF] [--rmdup RMDUP] [--elip ELIP] [--gname GNAME] [--input_file INPUT_FILE]`.

Depending on the usage, each argument helps to provide a different representation of the attack behavior. `[--asterisk true]` creates ab abstraction and can be used to replace anything that is not perceived as IOC/system entity into a wild-card. This representation can be used to be searched within the audit-logs.  
Through `[--crf true/false]`, you can activate co-referencing. `[--rmdup true/false]` enables removal of duplicate nodes-edge. `[--elip true/false]` is to choose whether to replace ellipsis subjects using the surrounding subject or not.



#### Example
`python3 main.py --asterisk true --crf true --rmdup true --elip true --input_file input.txt --gname mygraph`
