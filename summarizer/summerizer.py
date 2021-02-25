import re
from list_iocs import iocs
from allennlp.predictors.predictor import Predictor
from lists_patterns import load_lists, fpath
from nltk import sent_tokenize

my_svo_triplet, all_nodes = [], []
main_verbs = load_lists(fpath)['verbs']
main_verbs = main_verbs.replace("'", "").strip('][').split(', ')
sentences = r''' '''

# Abstractive
def ats():
    for sentence in range(sent_tokenize(sentences)):
        predictor = Predictor.from_path("srl-model.tar.gz")
        predictions = predictor.predict(sentence)
        lst = []
        nodes = []
        for k in predictions['verbs']:
            if k['description'].count('[') > 1:
                lst.append(k['description'])
        for jj in range(len(lst)):
            nodes.append([])
            for j in re.findall(r"[^[]*\[([^]]*)\]", lst[jj]):
                nodes[jj].append(j)
        print("*****sentence:", sentence, '*****nodes: ', nodes)

        for lis_ in nodes:
            for indx in range(len(lis_)):
                if lis_[0].split(":", 1)[0].lower().strip() == "v" and lis_[0].split(":", 1)[
                    1].lower().strip() in main_verbs:
                    n = len(lis_)
                    for j in range(1, len(lis_)):
                        if lis_[j].split(":", 1)[0].lower() != "v":
                            if len(iocs.list_of_iocs(lis_[j].split(":", 1)[1])) > 0:
                                lis_.insert(0, " ARG-NEW: *")



