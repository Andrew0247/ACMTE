import pandas as pd

words = [['Optimism', 'insomnia'], ['pain', 'acceptance'], ['language', 'processing'], ['Optimism2', 'insomnia2'], ['pain2', 'acceptance2'], ['pain3', 'acceptance3']]
words_ = pd.DataFrame(words, columns=['sinonimos_1','sinonimos_2'])
n = len(words_)
words_sino = []
for i in range(n):
    s1 = words_.sinonimos_1.loc[i]
    s2 = words_.sinonimos_2.loc[i]
    words_sino.append(s1)
    words_sino.append(s2)

print(words_sino)