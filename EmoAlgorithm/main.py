from random import random
def get_current_emotion(emo):
    postiveFlag = None # 1正向 0中性 -1負向

    postiveLinear = [
        434, # 平靜一 nutral
        700, # 期待 happy
        900, # 期待 愉悅 surprise
        2849, # 一點小激動
    ]
    negativeLinear = [
        2077, # 小聲
        1500, # 失望 疑惑
        2600, # 害怕 fear
        1100, # 快哭了 sad
    ]

    # 分正負向
    if(emo[1]+emo[2] == emo[3]+emo[4]):
        # 平靜的話直接回傳434或2077
        return 434 if round(random()) else 2077
    else:
        postiveFlag = 1 if (emo[1]+emo[2] > emo[3]+emo[4]) else -1

    # 算權重
    weight = [-1, 2, 3, -2, -3]
    for idx, w in enumerate(weight):
        if idx==0: continue # 平靜一定要是負值        
        # 計算權重
        weight[idx] = w*emo[idx]*postiveFlag

    # 讓結果在0-3之間
    result = round(((sum(weight)+3)/6)*3)
    if postiveFlag==1:
        finalEmo = postiveLinear[result]
    else:
        finalEmo = negativeLinear[result]

    # 回傳情緒代號
    emo_table = {
        2849: '一點小激動',
        2800: '# 起伏較大 激動 angry',
        900: '# 期待 愉悅 surprise',
        700: '# 期待 happy',
        434: '# 平靜一 nutral',
        1500: '# 失望 疑惑',
        2600: '# 害怕 fear',
        1100: '# 快哭了 sad',
        2077: '# 小聲'
    }
    print(emo_table[finalEmo])
    return finalEmo