import re
from load_pattern import load_patterns,path
from nltk import sent_tokenize

class iocs:

    def find_them_all(self):
        lst = []
        pat = load_patterns(path)
        for key, value in pat.items():
            files = re.findall(value, self)
            if files:
                lst.append(files)
        return lst

    def list_of_iocs(self):
        ioc_list = []
        sentences = sent_tokenize(self)
        for i in sentences:
            x = iocs.find_them_all(i)
            for i in range(len(x)):
                for ioc in x[i]:
                    if len(x[i]) == 1:
                        if type(x[i][0]) == tuple:
                            ioc_list.append(x[i][0][0])
                        break
                if len(x[i]) > 1:
                    if type(x[i][0]) == tuple:
                        for k in x[i]:
                            ioc_list.append(k[0])
                    else:
                        ioc_list.append(x[i][0])
        return ioc_list
