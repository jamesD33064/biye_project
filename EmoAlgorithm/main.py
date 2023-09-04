
def get_current_emotion(emo):
    # 情緒判斷邏輯
    emotional_list = [
        434, # 平靜一 nutral
        700, # 期待 happy
        2849, # 起伏較大 激動 angry
        900, # 期待 愉悅 surprise
        1100, # 快哭了 sad
        2600, # 害怕 fear
    ]
    
    if max(emo) == 0.0:     # 全部0
        current_emotional_number = emotional_list[emotional_list.index(434)]
    elif int(max(emo)) == 1:    # 有1的
        current_emotional_number = emotional_list[emo.index(max(emo))]
    else:   # 比較複雜的
        linear = [
            2849, # 一點小激動
            900, # 期待 愉悅 surprise
            700, # 期待 happy
            434, # 平靜一 nutral
            1500, # 失望 疑惑
            2600, # 害怕 fear
            1100, # 快哭了 sad
            2077, # 小聲
        ]
        # emo weight => happy:-1 angry:-2.2 surprise:-2 sad:4 fear:3
        weight = [-1, -2.2, -2, 4, 3]
        emo_rate = 4
        # 機率＊權重
        for idx, emotional_rate in enumerate(emo):
                emo_rate += emotional_rate*weight[idx]
                break        
        if emo_rate < 0:
            emo_rate = 0
        elif emo_rate > len(linear)-1:
            emo_rate = len(linear)-1
        else:
            emo_rate = int(round(emo_rate))
        # 對應linear中的情緒
        current_emotional_number = linear[emo_rate]

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
    print(emo_table[current_emotional_number])
    return current_emotional_number
