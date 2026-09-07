

def solution(data, ext, val_ext, sort_by):
    answer = []

    ext_list = ['code','date','maximum','remain']
    index_ext = ext_list.index(ext) # 어떤 인덱스를 기준으로 비교하는가
    index_sort_by = ext_list.index(sort_by) # 오름차순 기준

    for i in range(len(data)):
        if data[i][index_ext] <= val_ext:
            answer.append(data[i])

    answer = sorted(answer, key = lambda x: x[index_sort_by])

    return answer