import os
import subprocess

folder_path = r'summarizer/data/'
filename = 'file.tsv'
_dir = "{0}".format(filename[:-4])
if not os.path.exists(_dir):
    os.makedirs(_dir)
cmdCommand = r"python /bert/run_classifier.py --task_name=mrpc --do_predict=true --data_dir=./summarizer/data --vocab_file=./summarizer/bert/uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./summarizer/bert/uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=/Users/admin/bert/kia_output/model.ckpt-468 --max_seq_length=128 --output_dir=./{0}/".format(
    _dir)
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
