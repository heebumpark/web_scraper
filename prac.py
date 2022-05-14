def solution(new_id):

    stage1_id = new_id.lower() #1단계 
    stage2_id = '' 
    stage3_id = '' 
    stage4_id = '' 
    stage5_id = '' 
    stage6_id = '' 
    stage7_id = ''
    
    for i in range(len(stage1_id)): #2단계
        if (stage1_id[i].isdecimal() == False) & (stage1_id[i].isalpha() == False) & ((stage1_id[i] in ("-","_",".")) == False):
            continue
        else:
            stage2_id += stage1_id[i]

    for i in range(len(stage2_id)):
        if i == len(stage2_id)-1:
            stage3_id += stage2_id[i]
            break
        if stage2_id[i] == stage2_id[i+1] == '.':
            continue
        stage3_id += stage2_id[i]

    if stage3_id[0] == '.' or stage3_id[len(stage3_id)-1] == '.': #4단계
        if stage3_id[0] == '.':
            stage4_id = stage3_id[1:]
        if stage3_id[len(stage3_id)-1] == '.':
            stage4_id = stage3_id[:-1]
    else:   stage4_id = stage3_id
    
    if stage4_id == '': stage5_id = 'a' #5단계 
    else: stage5_id = stage4_id
    

    if len(stage5_id) >= 16: # 6단계
        stage6_id = stage5_id[:15]
        if stage6_id[-1] == '.':
            stage6_id[:-1]
    else:
        stage6_id = stage5_id

    stage7_id = stage6_id
    while(len(stage7_id) <= 2):
        stage7_id += stage7_id[-1]
    
    result = stage7_id
    print(result)
    return result

solution('abcdefghijklmn.')