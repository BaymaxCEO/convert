def func(s,  change_num, dic): 
    result = ''
    if s == "": return result

    ss = s.split('\n')
    for i in range(len(ss)): 
        sss = ss[i].split(' ')
        sss = [x.strip() for x in sss if x.strip()!='']

        length = len(sss)
        res = []
        for j in range(length): 
            if sss[j].startswith('.'): 
                res.append(int(sss[j].split('.')[-1])-7+change_num)
            elif sss[j].endswith('.'): 
                res.append(int(sss[j].split('.')[0])+7+change_num)
            else: 
                res.append(int(sss[j])+change_num)
        # print(res)
        # for j in range(8): 
        #     pass

        for j in range(8): 
            for k in range(len(res)): 
                result += dic[res[k]][j] + ' '
            result += '\n'
    return result

def func_td(s,  change_num, dic_td): 
    result = ''
    if s == "": return result

    ss = s.split('\n')
    for i in range(len(ss)): 
        sss = ss[i].split(' ')
        sss = [x.strip() for x in sss if x.strip()!='']

        length = len(sss)
        res = []
        for j in range(length): 
            if sss[j].startswith('.'): 
                res.append(int(sss[j].split('.')[-1])-7+change_num)
            elif sss[j].endswith('.'): 
                res.append(int(sss[j].split('.')[0])+7+change_num)
            else: 
                res.append(int(sss[j])+change_num)
        # print(res)
        # for j in range(8): 
        #     pass
        print(res)
        for j in range(4): 
                   
            for k in range(len(res)): 
                result += dic_td[res[k]][j*2] + dic_td[res[k]][j*2+1] + ' '
            result += '\n'
        # result += '\n'
    return result


def update(dic): 
    for i in range(9, 16): 
        dic[i] = dic[i-8] + " #"
    for i in range(1, 9): 
        dic[i] = dic[i] + "  "
    return dic

# s = '1 1 1 .7 1\n' + \
#     '1 1 2 1 .7 .5 .6\n' + \
#     "1 1 .7 1 1 2\n" + \
#     ".5 .5 2 1 .7 .5 .6"

# s = '1 1 1 .7 1'
dic = {
    1: "oooooo", 
    2: "ooooox", 
    3: "ooooxx", 
    4: "oooxxx", 
    5: "ooxxxx", 
    6: "oxxxxx", 
    7: "xxxxxx", 
    8: "xooooo",  # "oooooo #", 
}
    # 9: "ooooox #", 
dic = update(dic)


dic_td = {
    1: "oooooo q", 
    2: "oxoooo  ", 
    3: "oooxoo  ", 
    4: "oxoxoo  ", 
    5: "xxoooo  ", 
    6: "xxoxoo  ", 
    7: "xxxooo  ", 
    8: "xxxxoo  ", 
    9: "xxxxox  ", 
    10: "xxxxxx  ", 
    11: "xxxxxx z"
}

# change_num = 3
# print(dic)
# result = func(s, change_num, dic)

# change_num_td = 3
# result_td = func_td(s, change_num_td, dic_td)
# # print(str(result))
# print(result_td)