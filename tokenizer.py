import spacy
from nltk import sent_tokenize
nlp = spacy.load("en_core_web_lg")
from lists_patterns import load_lists,fpath
import main
if not main.args.input_file:
    raise ValueError("usage: main.py [-h] [--asterisk ASTERISK] [--crf CRF] [--rmdup RMDUP] [--gname GNAME] [--input_file INPUT_FILE]")
else:
    f = open(main.args.input_file, encoding='iso-8859-1')
    txt = f.readlines()
    txt = " ".join(txt)
    txt = txt.replace('\n',' ')

titles_list = load_lists(fpath)['MS_TITLES']
titles_list = titles_list.replace("'", "").strip('][').split(', ')
main_verbs = load_lists(fpath)['verbs']
main_verbs = main_verbs.replace("'", "").strip('][').split(', ')

def delete_brackets(stri):
    stri = stri.replace("[","")
    stri = stri.replace("]", "")
    stri = stri.replace("<", "")
    stri = stri.replace(">", "")
    return stri
txt = delete_brackets(txt)
txt = txt.strip(" ")

def all_sentences(string):
    nltk_sentences = sent_tokenize(string)

    all_sentences_list = []
    for i in nltk_sentences:
        i.rstrip()
        if i.endswith(".") and "\n" not in i:
            all_sentences_list.append(i)
        elif "\n" in i:
            i.split("\n")
            for j in i.split("\n"):
                all_sentences_list.append(j)
    return all_sentences_list

def remove_analysis_by():
    var = "Analysis by"
    lst = all_sentences(txt)
    for i in lst:
        if i.startswith(var):
            lst.remove(i)
    return lst

def perform_following_action():  # When Virus:Win32/Funlove.4099 runs, it performs the following actions:
    perform_following_action_list = load_lists(fpath)['MS_PFA']
    perform_following_action_list = perform_following_action_list.replace("'", "").strip('][').split(', ')
    lst = remove_analysis_by()
    for i in lst:
        for j in perform_following_action_list:
            if j in i:
                lst.remove(i)
                break
    return lst

def on_the_windows_x_only():
    # on_the_windows_x_list = load_lists_microsoft.on_the_windows_x_lst()
    on_the_windows_x_list = load_lists(fpath)['MS_OTW']
    on_the_windows_x_list = on_the_windows_x_list.replace("'", "").strip('][').split(', ')
    lst = perform_following_action()
    for i in lst:
        for j in on_the_windows_x_list:
            if j == i:
                lst.remove(i)
                # break
    return lst

def removable_token():  # When Virus:Win32/Funlove.4099 runs, it performs the following actions:
    removable_token_list = load_lists(fpath)['RTL']
    removable_token_list = removable_token_list.replace("'", "").strip('][').split(', ')
    lst = on_the_windows_x_only()
    for id, value in enumerate(lst):
        for j in removable_token_list:
            if value.strip().startswith(j):  #### definetly remember we should use only startswith()for proper matching
                # lst.remove(value)
                lst[id] = value.replace(j, " ")
                # break
    return lst
all_sentences_list = removable_token()


def handle_title(mylist_):  # handles titles and "." of the previous sentence
    lst_handled_titles = []
    lst = list(filter(lambda a: a != "", mylist_))[::-1]
    lst = list(filter(lambda a: a != " ", lst))
    lst = list(filter(lambda a: a != "", lst))
    for indx, val in enumerate(lst):
        lst[indx] = val.strip()
        if val=='':
            del lst[indx]
    l = len(lst)
    for index, item in enumerate(lst):
        if index < l - 1:
            if item in titles_list:
                x = lst[index + 1]
                if lst[index + 1] not in titles_list:
                    if len(lst[index + 1].rstrip()) >=1:  # inja
                        if lst[index + 1].rstrip()[-1] != ".":
                            if lst_handled_titles:
                                if lst[index + 1] + "." != lst_handled_titles[-1]:
                                    lst_handled_titles.append(lst[index + 1] + ".")
                            else:
                                lst_handled_titles.append(lst[index + 1] + ".")
                        else:
                            if lst_handled_titles:
                                if lst[index + 1] != lst_handled_titles[-1]: # mahshid added n
                                    lst_handled_titles.append(lst[index + 1])
                            else:
                                lst_handled_titles.append(lst[index + 1])
                else:
                    pass
            else:
                if lst_handled_titles:
                    if item + "." not in lst_handled_titles and item !=  lst_handled_titles[-1]:
                        lst_handled_titles.append(item)
                else:

                    lst_handled_titles.append(item)
        else:
            if item not in titles_list:
                if item != lst_handled_titles[-1]:
                    lst_handled_titles.append(item)
    lst = lst_handled_titles[::-1]
    lst = list(filter(lambda a: a != " ", lst))
    return list(filter(lambda a: a != "", lst))

def zero_word_verb(string):
    doc = nlp(string.strip())
    if not (doc[0].tag_ == "MD") and\
            not (doc[0].tag_ == "VB" and
                 str(doc[0]).lower() in main_verbs) and\
            not (doc[0].tag_ == "VB" and
                 str(doc[0]).lower() not in main_verbs) and\
            not(str(doc[0]).lower() in main_verbs):
        return False
    else:
        return  True

def true_sentence(sentence):
    if len(sent_tokenize(sentence)) > 0:
        return True
    return False

def iscaptalized(sentence):
    if sentence.strip()[0].isupper() == True:
        return True
    else:
        return False

def sentence_characteristic(sentence):
    doc = nlp(sentence)
    if len(sentence.split(" ")) > 3:
        count_verb, count_noun = 0, 0
        for token in doc:
            if token.pos_ == "VERB":
                count_verb += 1
            if token.pos_ == "NOUN":
                count_noun += 1
        if count_verb >= 1 and count_noun >= 2:
            return True
    else:
        return False

def likely_sentence_characteristic(sentence):
    doc = nlp(sentence)
    if zero_word_verb(sentence) == True:
        if len(sentence.split(" ")) > 3:
            return True

        return "UNKNOWN"

    if iscaptalized(sentence) == True:
        if len(sentence.split(" ")) > 3:
            count_verb, count_noun = 0, 0
            for token in doc:
                if token.pos_ == "VERB":
                    count_verb += 1
                if token.pos_ == "NOUN":
                    count_noun += 1
            if count_verb >= 1 and count_noun >= 2:
                return True
    else:
        return False

def sentence_tokenizer():
    num = 0
    possible_sentence = ""
    sentnce_buffer = ""
    if len(all_sentences_list) > 1:
        handele_titles = handle_title(all_sentences_list)
    else:
        handele_titles = all_sentences_list
    sentences_list = []
    for sec in handele_titles:
        # sentences_list.append(sec.encode('ascii', errors='ignore').decode('utf8'))
        sentences_list.append(sec.replace(u'\xa0', u' '))
    sentences_list = list(filter(lambda a: a != " ", sentences_list)) # remvoe ' '  from handle list
    sentences_list = list(filter(lambda a: a != "  ", sentences_list))
    sentences_list = list(filter(lambda a: a != "   ", sentences_list))
    l = len(sentences_list)

    for i in range(len(sentences_list)):
        other_sentences = []
        if num == l:
            break
        if num < l:
            xyz = sentences_list[i]
            if sentences_list[i].rstrip()[-1] == ".":
                if sentence_characteristic(sentences_list[i]) == True:
                    possible_sentence += sentences_list[i] + " "
                    num += 1
                elif len(sentences_list[i].split(" ")) > 3 and sentences_list[i].split(" ")[0].lower() in main_verbs:
                    possible_sentence += sentences_list[i] + " "
                    num += 1
                else:
                    print("ELSE-1:", sentences_list[i])
                    possible_sentence += sentences_list[i] + " "
                    num += 1
            elif zero_word_verb(sentences_list[i]) and ":" not in sentences_list[i].strip():
                if num != l - 1:
                    if sentence_characteristic(sentences_list[i + 1]) == True or  zero_word_verb(sentences_list[i + 1]):
                        possible_sentence += sentences_list[i].strip() + " . "
                        num += 1
                    elif sentence_characteristic(sentences_list[i + 1]) == False or not zero_word_verb(sentences_list[i + 1]):
                        sentnce_buffer += sentences_list[i].strip()
                        num += 1
                        sentnce_buffer += sentences_list[i + 1]
                        num += 1
                else:
                    possible_sentence += sentences_list[i].strip() + " . "
                    num += 1

            elif zero_word_verb(sentences_list[i]) and ":" in sentences_list[i]:
                if not zero_word_verb(sentences_list[i + 1]):  ##### or [i+1] is likely_sentence_ ...
                    sentnce_buffer += sentences_list[i] + " "
                    num += 1
                    # if zero_word_verb(sentences_list[i+1]):
                    if num < l:
                        while not likely_sentence_characteristic(sentences_list[i + 1]):  #### whattttt? #######!!!!!!!!######## or sentences_list[i+1].rstrip()[-1]!="." BELOWWW
                            # or sentence_characteristic(sentences_list[i+1]) ==True and sentences_list[i+1].rstrip()[-1]!="."
                            sentnce_buffer += sentences_list[i + 1] + " "
                            num += 1
                            sentences_list[i + 1]
                            del sentences_list[i + 1]
                            if num == l:
                                break
                        sentnce_buffer += " . "
                        possible_sentence += " "
                        possible_sentence += sentnce_buffer
                        sentnce_buffer = ""

                    elif sentences_list[i].strip()[-1] == ":":
                        possible_sentence += sentences_list[i].replace(":", " . ") + " "
                        num += 1
                    else: #  Creates registry value: gigabit.exe
                        possible_sentence += sentences_list[i] + " . "
                        num += 1
                    # if num < l:
                    #     sentnce_buffer += sentences_list[i+1] + " "
                    #     num += 1
                    #     del sentences_list[i+1]
                    #     while not zero_word_verb(sentences_list[i+1]):
                    #         sentnce_buffer += sentences_list[i + 1]  + " "
                    #         num += 1
                    #         del sentences_list[i + 1]
                    #     sentnce_buffer += " . "
                    #     possible_sentence += sentnce_buffer
                    # else:
                    #     break
                elif  zero_word_verb(sentences_list[i + 1]):
                    if sentences_list[i].rstrip()[-1] == ":":
                        possible_sentence += sentences_list[i].replace(":", " . ") + " "
                        num += 1
                    else:
                        possible_sentence += sentences_list[i] + " . "
                        num += 1

            elif iscaptalized(sentences_list[i]) == True and sentences_list[i].rstrip()[-1] == ":":
                if sentences_list[i] == sentences_list[-1]:
                    possible_sentence += sentences_list[i].replace(":", " . ") + " "
                    num += 1

                elif zero_word_verb(sentences_list[i + 1]):
                    possible_sentence  += sentences_list[i].replace(":", " . ") + " "
                    num +=1
                else:
                    sentnce_buffer += sentences_list[i] + " "
                    num += 1
                    while not(sentence_characteristic( sentences_list[i + 1]))    :
                        xxx = sentences_list[i + 1]
                        if  zero_word_verb(sentences_list[i + 1]):
                            break

                        elif not zero_word_verb(sentences_list[i + 1]):
                            sentnce_buffer += sentences_list[i + 1] + " "
                            num += 1
                            del sentences_list[i + 1]
                            if num == l or num > l:
                                if sentnce_buffer.rstrip()[-1] != ".":
                                    sentnce_buffer += " . "
                                possible_sentence += sentnce_buffer
                                sentnce_buffer = ""
                                break
                    # if not sentence_characteristic(sentences_list[i + 1]):
                    #     sentnce_buffer += sentences_list[i + 1]
                    #     num += 1
                    #     del sentences_list[i + 1]
                    if sentnce_buffer:
                        if sentnce_buffer.rstrip()[-1] != ".":
                            sentnce_buffer += " . "
                    possible_sentence += sentnce_buffer
                    sentnce_buffer = ""
                    # else:
                    #     sentnce_buffer.rstrip().replace(":",".")
                    #     possible_sentence += sentnce_buffer
                    #     sentnce_buffer = " "
            elif sentence_characteristic(sentences_list[i]) == True:
                possible_sentence += sentences_list[i].strip() + " . "
                num += 1
            else:
                other_sentences.append(sentences_list[i])
                num += 1
        else:
            break
    posslist = sent_tokenize(possible_sentence)
    for indx, val in enumerate(posslist):
        if len(val.split()) < 2:
            del posslist[indx]
    possible_sentence = " ".join(posslist)
    return possible_sentence

txt_tokenized = sentence_tokenizer()
print("*****sentence_tokenizer:", len(sent_tokenize(txt_tokenized)), sentence_tokenizer())

print("*****Tokenizer*****")

for i,val in enumerate(sent_tokenize(txt_tokenized)):
    print(i,val)
