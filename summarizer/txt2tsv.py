import pandas as pd

def txt_to_tsv():
    filename = r'./data/file.txt'
    data = pd.read_csv(filename, delimiter=',', index_col=False, header=None, error_bad_lines=False, engine='python')
    data['all'] = data[data.columns[0:]].apply(
        lambda x: ','.join(x.dropna().astype(str)),
        axis=1
    )
    data.insert(0, "label", 0)
    headers = ["label", "all"]
    data.to_csv( filename + ".csv", index=False, columns=headers, header=False)

    test_df = pd.read_csv(  filename + ".csv", header=None, encoding="ISO-8859-1")
    test_df = pd.DataFrame({
        'id': range(len(test_df)),
        'label': test_df[0],
        'alpha': ['a'] * test_df.shape[0],
        'text': test_df[1].replace(r'\n', ' ', regex=True)
    })
    print("test_df top 5 rows are:", test_df.head())
    test_df.to_csv('file.tsv', sep='\t', index=False, header=False)
    print("train_tsv save, done!")


if __name__ == '__main__':

    txt_to_tsv()

