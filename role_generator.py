from subject_verb_object_extract import findSVOs, nlp
# nlp = spacy.load("en_core_web_lg")
from allennlp.predictors.predictor import Predictor
from nltk.stem.wordnet import WordNetLemmatizer
from preprocessings  import *
from list_iocs import iocs
from lists_patterns import load_lists, fpath
main_verbs = load_lists(fpath)['verbs']
main_verbs = main_verbs.replace("'", "").strip('][').split(', ')



def colon_seprator_multiplication(stri):
    coref_reference_list = load_lists(fpath)['TFL']
    coref_reference_list = coref_reference_list.replace("'", "").strip('][').split(', ')
    stri = stri.rstrip()
    stri = stri.rstrip('.')
    result = ""
    for item in sent_tokenize(stri):
        flag = False
        for refrence in coref_reference_list:
            if refrence in item and ":" in item:
                sentence_splits = item.split(":", 1)
                y = iocs.list_of_iocs(item.split(":", 1)[1])
                if y:
                    sentence_replicas = [sentence_splits[0].rstrip(":")] * len(y)
                    for i in range(len(sentence_replicas)):
                        result += sentence_replicas[i].replace(refrence, y[i]) + " . "
                else:
                    item = sentence_splits[0].replace(refrence, sentence_splits[1])
                    result += item

                flag = True
                break
        if flag == False:
            result += item
            result += " "
    if result.rstrip("")[-1] != ".":
        result += "."
    return result

def roles(sentences):
    my_svo_triplet = []
    all_nodes = []
    for i in range(len(sentences)):
        # public SRL model https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz
        predictor = Predictor.from_path("srl-model.tar.gz")
        predictions = predictor.predict(sentences[i])
        lst = []
        nodes = []
        for k in predictions['verbs']:
            if k['description'].count('[') > 1:
                lst.append(k['description'])
        for jj in range(len(lst)):
            nodes.append([])
            for j in re.findall(r"[^[]*\[([^]]*)\]", lst[jj]):
                nodes[jj].append(j)
        print("*****sentence:",sentences[i],'*****nodes: ',nodes)

        for lis_ in nodes:
            for indx in range(len(lis_)):
                if lis_[0].split(":", 1)[0].lower().strip() == "v" and lis_[0].split(":", 1)[1].lower().strip() in main_verbs:
                    n = len(lis_)
                    for j in range(1, len(lis_)):
                        if lis_[j].split(":", 1)[0].lower() != "v":
                            if len(iocs.list_of_iocs(lis_[j].split(":", 1)[1])) > 0:
                                lis_.insert(0, " ARG-NEW: *")

        maxlength = 0
        if nodes:
            maxlength = max((len(i) for i in nodes))
        if nodes == [] or maxlength < 3:
            print("****DP SVO****")
            tokens = nlp(sentences[i])
            svos = findSVOs(tokens)
            if svos:
                for sv in range(len(svos)):
                    if len(svos[sv]) == 3:
                        print('Dependency SVO(s):', ["ARG0: " + svos[sv][0], "V: " + svos[sv][1], "ARG1: " + svos[sv][2]])
                        nodes.append(["ARG0: " + svos[sv][0], "V: " + svos[sv][1], "ARG1: " + svos[sv][2]])
            print("Dependency-SVO added nodes: ", nodes)

            print("****Naive SVO****")
            breakers = []
            subj, obj = '', ''
            doc = nlp(sentences[i])
            for token in doc:
                if token.pos_ == 'VERB':
                    breakers.append(str(token))
            if len(breakers) != 0:
                for vb in breakers:
                    subj = "subj: " + sentences[i].split(vb)[0]
                    obj = "obj: " + sentences[i].split(vb)[1]
                    vrb = "v: " + vb
                    lst = []
                    lst.append(subj)
                    lst.append(vrb)
                    lst.append(obj)
                    nodes.append(lst)
            print("Naive Nodes: ", nodes)

        if nodes != []:
            zero_dunplicate_removed = []
            for i in nodes:
                zero_dunplicate_removed.append(list(dict.fromkeys(i)))
            no_zero_nodes = []
            for i in zero_dunplicate_removed:
                if '.' in i:
                    i.remove('.')
                    no_zero_nodes.append(i)
                else:
                    no_zero_nodes = zero_dunplicate_removed

            no_zero_nodes_plus_3 = []
            for i in no_zero_nodes:
                if len(i) > 2:
                    no_zero_nodes_plus_3.append(i)


            removeable_items_list = ['both','also','that','would','could','immediately','usually','for',
                                     'when','then','will','which','first','second','third','forth',
                                     'fifth','internally','where','while', 'either','nither','when',
                                     'sever', 'successfully', 'also', 'to','above','already','recently',
                                     'may','however','can','once loaded','in fact','in this way','all',
                                     'actually','inadvertently','instead','when copying themselves',
                                     'automatically', 'should', 'can', 'could', 'necessarily', 'if found',
                                     'randomly', 'again', 'still', 'generally', 'slowly','ever','shall','newly', 'However',
                                     'when executed','subsequently']

            #lammarizer
            for i in range(len(no_zero_nodes_plus_3)):
                for index, item in enumerate(no_zero_nodes_plus_3[i]):
                    if item.split(': ')[0] == 'V':
                        word = item.split(': ')[1]
                        no_zero_nodes_plus_3[i][index] = "V: " + WordNetLemmatizer().lemmatize(item.split(": ")[1].lower(), 'v')

            for i in range(len(no_zero_nodes_plus_3)):

                if no_zero_nodes_plus_3[i]:
                    for index, item in enumerate(no_zero_nodes_plus_3[i]):

                        if 'ARGM-MOD:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'ARGM-ADV:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'ARGM-TMP:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'ARGM-MNR:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ",item)

                        if 'R-ARG1:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'R-ARG0:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ",item)

                        if 'ARGM-DIS:' in item:
                            if item.split(': ',1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ",item)

                        if 'ARGM-PRP:' in item:
                            if item.split(': ', 1)[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

            for i in range(len(no_zero_nodes_plus_3)):
                if no_zero_nodes_plus_3[i]:
                    for index, item in enumerate(no_zero_nodes_plus_3[i]):

                        if 'ARGM-MOD:' in item:
                            if item.split(': ')[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'ARGM-ADV:' in item:
                            if item.split(': ')[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'ARGM-TMP:' in item:
                            if item.split(': ')[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'ARGM-MNR:' in item:
                            if item.split(': ')[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ",item)

                        if 'R-ARG1:' in item:
                            if item.split(': ')[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ", item)

                        if 'R-ARG0:' in item:
                            if item.split(': ')[1].lower() in removeable_items_list:
                                del no_zero_nodes_plus_3[i][index]
                            else:
                                print("##### NEW Exception: ",item)


            v_unlink = ['delete', 'clear', 'remove', 'erase', 'wipe','purge','expunge']
            v_write = ['entrench','exfiltrate', 'store' , 'drop','drops', 'install', 'place', 'deploy', 'implant', 'write', 'putfile','compose','create', 'creates','copy','copies','save','saved','saves','add','adds','modify','modifies','append','appends']
            v_read = ['survey','download', 'navigate', 'locate', 'read', 'gather', 'extract','extracts','obtain','acquire','check','checks','detect','detects','record','records']
            v_exec = [ 'use', 'execute', 'executed', 'run', 'ran', 'launch', 'call', 'perform', 'list', 'invoke', 'inject', 'open', 'opened','target','resume','exec']
            v_mmap = ['allocate','assign']
            v_fork = ['clone', 'clones','spawned','spawn','spawns','issue','set']
            v_setuid = ['elevate', 'impersonated']
            v_send = ['send', 'sent','transfer','post','postsinformation','postsinformations','move', 'transmit','deliver','push','redirect','redirects']
            v_receive = ['receive','accept','take','get','gets', 'collect']
            v_connect = ['click', 'browse', 'browses', 'connect', 'connected', 'portscan', 'connects','alerts','communicates','communicate']
            v_chmod = ['chmod', 'change permission','changes permission', 'permision-modifies', 'modifies permission','modify permission']
            v_load = ['load', 'loads']
            v_exit = ['terminate', 'terminates','stop','stops','end','finish','break off','abort','conclude']
            v_2D = {'collect':('read','receive'), 'open':('exec','fork')}




            for i in range(len(no_zero_nodes_plus_3)):
                for index, item in enumerate(no_zero_nodes_plus_3[i]):
                    if item.split(': ')[0] == 'V':
                        if item.split(': ')[1] in v_unlink:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'unlink'
                        elif item.split(': ')[1] in v_write:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'write'
                        elif item.split(': ')[1] in v_read:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'read'
                        elif item.split(': ')[1] in v_exec:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'exec'
                        elif item.split(': ')[1] in v_mmap:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'mmap'
                        elif item.split(': ')[1] in v_fork:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'fork'
                        elif item.split(': ')[1] in v_setuid:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'setuid'
                        elif item.split(': ')[1] in v_send:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'send'
                        elif item.split(': ')[1] in v_receive:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'receive'
                        elif item.split(': ')[1] in v_connect:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'connect'
                        elif item.split(': ')[1] in v_chmod:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'chmod'
                        elif item.split(': ')[1] in v_load:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'load'
                        elif item.split(': ')[1] in v_exit:
                            no_zero_nodes_plus_3[i][index] = 'V: ' + 'exit'
        else:
            continue
        all_nodes += no_zero_nodes_plus_3
        if my_svo_triplet:
            all_nodes += my_svo_triplet
    print('*****all_nodes:::',all_nodes)
    return all_nodes

def fix_srl_spacing(li):
    new_lst = []
    for i in li:
        x = []
        for j in i:
            files = re.findall(load_patterns(path)['*_extension'], j)
            if files:
                for k in files:
                    j = j.replace(k, re.sub(' ', ' *', k))
                x.append(j)
            else:
                x.append(j)
        new_lst.append(x)
    return new_lst


def negation_clauses(srl_input):
    conditional_clause = ['if', 'otherwise', 'when']
    purged = []
    purged[:] = [x for x in srl_input if "ARGM-NEG" in str(x) if "if" and "when" not in str(x).lower()]
    positive_sentences = [i for i in srl_input if i not in purged]
    return positive_sentences

def group_partials(strings):
    try:
        s = ''
        it = iter(sorted(strings))
        prev = next(it)
        for s in it:
            if s.find(prev) == -1:
                yield prev
            prev = s
        yield s
    except StopIteration:
        return


def process_convert(lst):
    lst = ["/-" + i.strip() + "-/" for i in lst]
    return [i.replace(" ", "-") for i in lst]


from list_iocs import *
def astriks(lis):
    apps_process = load_lists(fpath)['APPs-PROCESS']
    apps_process = apps_process.replace("'", "").strip('][').split(' , ')
    updated_list = [[] for x in range(len(lis))]
    for jj, lst in enumerate(lis):
        for i in range(len(lst)):
            if ":" not in lst[i]:
                lst[i] = "TMP: " + lst[i]
            leftnode = lst[i].split(":", 1)[0]
            rightnode = lst[i].split(":", 1)[1]
            lOFioc = iocs.list_of_iocs(rightnode)
            found_app = [app for app in apps_process if app in rightnode.lower()]
            if len(found_app) > 1:
                found_app = list(group_partials(found_app))
                found_app = process_convert(found_app)
            else:
                found_app = process_convert(found_app)
            if not lOFioc:
                if leftnode.lower() != "v" and not found_app:
                    updated_list[jj].append(leftnode + ": *")
                elif leftnode.lower() == "v":
                    updated_list[jj].append(lst[i])
                elif leftnode.lower() != "v" and found_app:
                    for process in found_app:
                        updated_list[jj].append(leftnode + ": " + process)
            elif len(lOFioc) == 1:
                updated_list[jj].append(leftnode + ": " + lOFioc[0])
            elif len(lOFioc) >=2:
                updated_list[jj].append(leftnode + ": " + lOFioc[0])
                for index in range(1, len(lOFioc)):
                    updated_list[jj].append("ARG-NEW: " + lOFioc[index])
    return updated_list

def triplet_builder(mylist):
    triplet = []
    for i in range(len(mylist)):
        xv = mylist[i]
        if len(mylist[i]) > 3:
            for index, value in enumerate(mylist[i]):
                    l = len(mylist[i])
                    if "v" in value.lower() and index != 0 and index != l-1:
                        for k in mylist[i][:index]:
                            for j in mylist[i][index+1:]:
                                triplet.append((k, value, j))
        elif len(mylist[i]) == 3:
            triplet.append(mylist[i])
    return list(map(list, triplet))



