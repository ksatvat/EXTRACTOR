import re
from tokenizer import sentence_tokenizer
from passive2active import pass2act
import nltk
from nltk import sent_tokenize
from textblob import TextBlob
from pattern.text.en import conjugate,PRESENT,SG
import spacy
nlp = spacy.load("en_core_web_lg")
import signal
import neuralcoref
from lists_patterns import load_lists,fpath
preprocessing_input = sentence_tokenizer()
from load_pattern import load_patterns,path
from list_iocs import iocs
from load_lists_general import all_lst



def delete_brackets(stri):
    stri = stri.replace("[","")
    stri = stri.replace("]", "")
    return stri

def pass2acti(stri):
    result = ' '
    for i in sent_tokenize(stri):
        pa2act = pass2act(i)
        result += pa2act
    return result

def coref_(stri):
    neuralcoref.add_to_pipe(nlp)
    doc = nlp(stri)
    corefed = doc._.coref_resolved.replace("\n", "")
    if corefed:
        return corefed
    else:
        return stri

def SIGSEGV_signal_arises(signalNum, stack):
    print(f"{signalNum} : SIGSEGV arises")
signal.signal(signal.SIGSEGV, SIGSEGV_signal_arises)

def wild_card_extansions(stri):
    pat = load_patterns(path)
    files = re.findall(pat['*extension'], stri)
    for i in files:
        stri = stri.replace(i, " *" + i.strip())
    return stri

def try_to(stri):
    verb = ''
    try_to_list = ['tries to','try to', 'attempts to' , 'attempt to']
    blob = TextBlob(stri)
    sentences = sent_tokenize(stri)
    for i in range(len(sentences)):
        for element in try_to_list:
            if element in sentences[i]:
                match = re.search(element+'[ ]+(\S+)',stri) # one or more space
                if match:
                    verb = match.group(1)#+'s'

    if verb:
        for word, pos in blob.tags:
            if word == verb and "V" in pos:
                stri = stri.replace(match.group(), verb)

    return stri

def is_capable_of(stri):
    sentences = sent_tokenize(stri)
    keywords = ['is capable of', 'are capable of']
    outcome = ''
    for sent in sentences:
        for keyword in keywords:
            if keyword in sent:
                before_keyword, keyword, after_keyword = sent.partition(keyword)
                token = nltk.word_tokenize(sent)
                for i in nltk.pos_tag(token):
                        if i[0] == after_keyword.split()[0] and i[1] == 'VBG':
                            outcome += " " + before_keyword + conjugate(verb=after_keyword.split()[0],tense=PRESENT,number=SG) + " " + ' '.join(after_keyword.split()[1:])
            else:
                if sent not in outcome:
                    outcome += " " + sent
    return outcome

def ellipsis_subject(stri):
    ellipsis_verbs = load_lists(fpath)['verbs']
    ellipsis_verbs = ellipsis_verbs.replace("'", "").strip('][').split(', ')
    sent_text = nltk.sent_tokenize(stri)
    result = ""
    for sentence in sent_text:
        token = nltk.word_tokenize(sentence)
        doc = nlp(sentence)
        if nltk.pos_tag(token)[0][1] == "VB" or nltk.pos_tag(token)[0][1] == "VBZ" or doc[0].pos_ == "VERB" or doc[0].text.lower() in ellipsis_verbs:
            new_sentence = " It " + nltk.pos_tag(token)[0][0].lower() + " " + " ".join(sentence.split(" ")[1:])
            result += " " + new_sentence
        elif doc[0].dep_ == "ROOT":
            if doc[0].text.lower in ellipsis_verbs:
                new_sentence = " It " + doc[0].text.lower() + " " + " ".join(sentence.split(" ")[1:])
                result += " " + new_sentence
        elif doc[0].text.lower() in ellipsis_verbs and doc[0].dep_ != "ROOT":
            result += " " + doc.text
        else:
            result += " " + sentence
    return result

def detect_subj(sentence_list):
    # buffer_nsubj = {}
    subject = ''
    for sentence in sentence_list:
        doc = nlp(sentence)
        for token in doc:
            if token.dep_ == "nsubj":
                subject = token.text
                # buffer_nsubj[sentence] = token.text
    # return buffer_nsubj
    if subject:
        return subject

def zero_word_verb(stri):
    doc = nlp(stri.strip())
    main_verbs = load_lists(fpath)['verbs']
    main_verbs = main_verbs.replace("'", "").strip('][').split(', ')
    if not (doc[0].tag_ == "MD") and\
            not (doc[0].tag_ == "VB" and
                 str(doc[0]).lower() in main_verbs) and\
            not (doc[0].tag_ == "VB" and
                 str(doc[0]).lower() not in main_verbs) and\
            not(str(doc[0]).lower() in main_verbs):
        return False
    else:
        return True

def capitalize(line):
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))

def replcae_surrounding_subject(stri):
    sent_list = sent_tokenize(stri)
    new_text = ''
    for indx, sentence in enumerate(sent_list):
        if zero_word_verb(sentence):
           subject = detect_subj(sent_list[:indx])
           new_text += " " + capitalize(subject) + " " + sentence[0].lower() + sentence[1:]
        else:
            new_text += " " + sentence
    return new_text

def coref_the_following_colon(stri):
    sentence2 = ' '
    final_txt = ''
    fl = len(final_txt)
    # list1 = the_following_colon_lst()
    list1 = load_lists(fpath)['TFCL']
    list1 = list1.replace("'", "").strip('][').split(', ')
    sentences = sent_tokenize(stri)
    l = len(sentences)
    c = 0
    for sentence in sentences:
        c += 1
        for value in list1:
            if value in sentence:
                sentence.strip() # to get ride of possible space at the end of sentence
                if sentence[-1] == ".":
                    sentence = sentence[:-1] # removes the dot from the end
                if ":" in sentence:
                    one = sentence.split(value)[0]
                    two = sentence.split(value)[1]
                    # sentence2 = sentence.split(":")[0].replace(value[:-1],sentence.split(":",1)[1]) + ". "  # replace the token with value
                    # sentence2 = sentence.replace(value, sentence.split(value)[1]) + ". "  # replace the token with value
                    sentence2 = sentence.replace(value," ") + ". "
                    final_txt += " " + sentence2
                    p = final_txt
                    fl += 1
                break
        if c > fl:
            final_txt += " " + sentence
            fl += 1
    return final_txt

def coref_the_following_middle(stri):
    final_txt= ''
    list2 = load_lists(fpath)['TFL']
    list2 = list2.replace("'", "").strip('][').split(', ')
    sentences = sent_tokenize(stri)
    c = 0
    fl = len(final_txt)
    for sentence in sentences:
        c += 1
        for value in list2:
            if value in sentence:
                sentence.strip()
                if sentence[-1] == "." and ":" in sentence:
                    sentence = sentence[:-1]
                    sentence2 = sentence.split(":")[0].replace(value,sentence.split(":",1)[1]) + ". "
                    final_txt += ' ' + sentence2
                    fl += 1
                    break
        if c > fl:
            final_txt += ' ' + sentence
            fl += 1
    return final_txt


def obscure_vocabs():
    vb_send = ['send' ,'exfiltrate' ,'postsinformation' ,'exfiled' ,'exfil','beacon']
    vb_sends = ['sends' ,'exfiltrates', 'postsinformations', 'exfileds', 'exfils' ,'beacons']
    vb_write = ['write', 'entrench']
    vb_writes = ['writes','entrenches']
    return vb_send ,vb_sends, vb_writes ,vb_write

def translate_obscure_words(stri):
    list1 = obscure_vocabs()
    finalsent = ''
    sentences = sent_tokenize(stri)
    for index, sentence in enumerate(sentences):
        for lis in list1:
            big_regex = re.compile('|'.join(map(re.escape, lis)))
            sent = big_regex.sub(lis[0], str(sentence))
            sentence = sent
        finalsent += ' ' + sent + ' '
    return finalsent


def homogenization(stri):
    finalsent = ''
    vars = all_lst()
    # vars = load_lists(fpath)['VAR']
    # vars = vars.replace("'", "").strip('][').split(', ')
    sentences = sent_tokenize(stri)
    for index, sentence in enumerate(sentences):
        for var in vars:
            big_regex = re.compile('|'.join(map(re.escape, var)))
            sent = big_regex.sub(var[0], str(sentence))
            sentence = sent
        finalsent += ' ' +sent + ' '
    return finalsent

print("------------communicate ---------------")
def communicate_to_sr(stri):
    final_txt = ''
    c = fl = 0
    pattern = load_lists(fpath)['COMU']
    pattern = pattern.replace("'", "").strip('][').split(', ')
    sentences = sent_tokenize(stri)
    for sentence in sentences:
        c += 1
        for value in pattern:
            if value in sentence:
                sentence1 = sentence.split(value)[0] + ' receives from'+ sentence.split(value)[1]
                sentence2 = sentence.split(value)[0] + ' sends to' + sentence.split(value)[1]
                final_txt += " " + sentence1 + " " + sentence2
                fl += 2
                c += 1
                break
        if c > fl:
            final_txt += " " + sentence
            fl += 1
    return final_txt

def CـC(txt):
    pattern = load_lists(fpath)['C_C']
    pattern = pattern.replace("'", "").strip('][').split(', ')
    big_regex = re.compile('|'.join(map(re.escape, pattern)),re.IGNORECASE)
    sentence = big_regex.sub('remote ip:*', str(txt))
    return sentence

def following_subject(txt):
    following_subject_list = load_lists(fpath)['TFSL']
    txt = txt.rstrip()
    txt = txt.rstrip('.')
    result = ""
    for sent in sent_tokenize(txt):
        for item in following_subject_list:
            if item in sent and ":" in sent:
                old_subj = item
                new_sub = sent.split(":" ,1)[1]
                y = iocs.list_of_iocs(sent)
                if y:
                    sentence_replicas = [new_sub[0]] * len(y)
                    for i in range(len(sentence_replicas)):
                        k = sent.split(":", 1)[0]
                        l = k.replace(old_subj," ")
                        result += y[i] + l + " . "
                break
    return result

def verb_and_verb(txt):
    verbs_list = load_lists(fpath)['verbs']
    doc = nlp(txt)
    result = ""
    for i in range(len(doc)+2):
        if doc[i].pos_ == "VERB" and doc[i+1].pos_ == "CCONJ" and doc[i+2].pos_  == "VERB":
            if doc[i].text in verbs_list and doc[i+2].text in verbs_list:
                candidate = doc[i].text + " " + doc[i + 1].text + " " + doc[i + 2].text
                result += txt.replace(candidate, doc[i].text)+ " "
                result += txt.replace(candidate, doc[i+2].text)
            break
    return result

txt = preprocessing_input
txt = delete_brackets(txt)
txt = pass2acti(txt)
txt = re.sub(' +', ' ', txt)
print("*********8",txt)



import main

if main.args.crf == 'true':
    txt = coref_(txt)
    print("coref_",len(txt),txt)
else:
    txt = wild_card_extansions(txt)


txt = try_to(txt)
print("try_to__",txt)
txt = is_capable_of(txt)

if main.args.elip == 'true':
    txt = replcae_surrounding_subject(txt)
else:
    print("is capble of__",txt)
    txt = ellipsis_subject(txt)
    print("ellipsis_subject", len(txt), txt)

print('------------ coref_the_following_colon ------------')
out = coref_the_following_colon(txt)

for i,val in enumerate(sent_tokenize(out)):
    print(i,val)

print('------------ coref_the_following_middle ------------')

midle = coref_the_following_middle(out)

for i,val in enumerate(sent_tokenize(midle)):
    print(i,val)

out_translate = translate_obscure_words(out)
print("*****homogenization:",homogenization(out_translate))
homo = homogenization(out_translate)
comm = communicate_to_sr(homo)
print(comm)
cc = CـC(comm)
print("------------ modification ---------------")

def modification_():
    final_txt = ''
    c = fl = 0
    pattern = load_lists(fpath)['MDF']
    pattern = pattern.replace("'", "").strip('][').split(', ')

    sentences = sent_tokenize(cc)
    for sentence in sentences:
        c += 1
        for value in pattern:
            if value in sentence:
                sentence1 = sentence.split(value)[0] + ' modifies ' + sentence.split(value)[1]
                final_txt += " " + sentence1 + " "
                fl += 2
                break
        if c > fl:
            final_txt += " " + sentence
            fl += 1
    return final_txt.strip()


print('----Preprocessed:----')
for i,val in enumerate(sent_tokenize(modification_())):
    print(i,val)



