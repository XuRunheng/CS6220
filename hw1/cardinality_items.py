import pandas as pd
def cardinality_items(file):
    df = pd.read_csv(file)
    ret = df.reset_index().nunique()
    print(ret)
    return ret;

cardinality_items("example.csv")
