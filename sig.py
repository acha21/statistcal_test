import scipy
import os
import numpy as np
from scipy import stats

rng = np.random.default_rng()



# alternative: rvs1 < rvs3

def testing(rvs1, rvs3):
    rs = stats.ttest_rel(rvs1, rvs3, alternative='less')
    print(rs)

    if rs.pvalue < 0.01:
        print("significant at 0.01 (1%)")
    elif rs.pvalue < 0.05:
        print("significant at 0.05 (5%)")
    elif rs.pvalue < 0.1:
        print("significant at 0.1 (10%)")





for eval_type in ['rel', 'int', 'kno']:
    for model in ['ram', 'bart', 'rag', "poly", "human"]:
        with open(f"sig_data/{eval_type}_{model}.txt", "r") as f:
            Ascores, Bscores = [], []
            for line in f.readlines():
                B_score, A_score = line.split("\t")
                B_score = int(B_score.strip())
                A_score = int(A_score.strip())
                Ascores.append(A_score)
                Bscores.append(B_score)
                # print(B_score, A_score)
            
        B = np.array(Bscores)
        A = np.array(Ascores)
        print(">")
        print(f"{eval_type}_{model}")
        testing(B, A)

        print("---------------------")
    print("========================")