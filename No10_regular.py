#!/usr/bin/env python
# -*- coding:utf-8 -*- 
 
# TODO 用回溯的思想，通过递归来解决，递归最底层应该是p只包含'.*' '.' '*'的一种或者0种
 
def process(s, p):
    if not s:
        return True if p == '' or p == '.*' else False
    flag = True
    tuple_1 = []
    # 将str按照. 或者.* 或者*分割
    for item in p.split('.*'):
        for sub_item in item.split('.'):
            for ssub_item in sub_item.split('*'):
                tuple_1.append(ssub_item)
                tuple_1.append('*')
            tuple_1.pop()  # 将最后一个'*'去掉
            tuple_1.append('.')
        tuple_1.pop()  # 将最后一个'.'去掉
        tuple_1.append('.*')
    print(tuple_1)
    # 进行匹配对比
    s_copy = s
    # 注意这里tuple_1 会在最后加一个'.*'pattern，所以len(tuple_1)-1 刚好取到倒数第二个pattern
    pre_item = None  # 主要服务于* 模式
    for i in range(0, len(tuple_1)-1):
        cur_item = tuple_1[i]
        next_item = tuple_1[i+1]
        if cur_item == '.':
            s_copy = s_copy[1:]
        # 重点1：因为需要判定.* 后的下一个字符串出现在s_copy的哪个位置（最远的位置）
        elif cur_item == '.*':
            s_tmp = s_copy
            idx = s_tmp.find(next_item)
            cur_idx = idx
            next_len = len(next_item)
            # 查找最远的next_item
            while cur_idx != -1:
                idx += next_len
                s_tmp = s_tmp[cur_idx+next_len:]  # 更新str
                cur_idx = s_tmp.find(next_item)  # 新的str是否还有next_item
            if idx == -1:
                flag = False
                break
            else:
                s_copy = next_item+s_tmp
        # 重点2：模式*和之前的模式相关
        elif cur_item == '*':
            pointed_alp = cur_item[-1]  # *前边的一个字母
            s_copy.find()
        # 重点3：对于正常的文本，需要考虑后边有没有*
        else:
            # *前的字母需要判断对应到s_copy的哪个位置
            if next_item == '*':
                # 首先查看pattern的前n-1个是否匹配
                length = len(cur_item)-1
                if s_copy[:length] == cur_item[:-1]:
                    s_copy = s_copy[length:]
                else:
                    flag = False
                    break
            else:
                length = len(cur_item)
                if s_copy[:length] == cur_item:
                    s_copy = s_copy[length:]
                else:
                    flag = False
                    break
        pre_item = cur_item
    # 判断s_copy是否匹配完毕
    if s_copy:
        flag = False
    return flag


if __name__ == '__main__':
    s='aa'
    p='a*a'
    ret = process(s, p)
    print(ret)
