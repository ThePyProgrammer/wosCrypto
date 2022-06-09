import requests, pandas as pd
from functools import partial

df = pd.read_html(requests.get("https://en.wikipedia.org/wiki/Rijndael_S-box").content)[0].iloc[:16].applymap(partial(
    int, base=16)).rename(columns={"Unnamed: 0": "index"}).set_index("index").rename(columns=partial(int, base=16)).stack()
df.index = df.index.map(sum)
rijndael = df.to_dict()