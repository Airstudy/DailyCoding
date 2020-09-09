#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 旋转数组（无重复）中找到指定值

def find_n(l_list, num):
    right_pos = len(l_list) - 1
    left_pos = 0
    left_num = l_list[0]
    right_num = l_list[right_pos]
    pos_flag = None
    # 确定num在旋转数组的前半段还是后半段
    if num < left_num and num < right_num:
        pos_flag = 'RIGHT'
    elif num > left_num and num > right_num:
        pos_flag = 'LEFT'
    elif num == left_num:
        return 0
    elif num == right_num:
        return right_pos
    else:
        return -1  # 没有答案
    # 二分法查找
    while(left_pos <= right_pos):
        middle_pos = (left_pos+right_pos)/2
        if num == l_list[middle_pos]:
            return middle_pos
        if pos_flag == 'LEFT':
            if num < l_list[middle_pos]:
                right_pos = middle_pos
            elif num > l_list[middle_pos] and l_list[middle_pos] > right_num:
                left_pos = middle_pos
            elif num > l_list[middle_pos] and l_list[middle_pos] < right_num:
                right_pos = middle_pos
        else:
            if num > l_list[middle_pos]:
                left_pos = middle_pos
            elif num < l_list[middle_pos] and l_list[middle_pos] < right_num:
                right_pos = middle_pos
            elif num < l_list[middle_pos] and l_list[middle_pos] > right_num:
                left_pos = middle_pos
    return -1

if __name__ == '__main__':
    l_list = [6, 8, 9, 10, 12, 20, 45, 58, 1, 3, 4, 5]
    ret = find_n(l_list, 4)
    print(ret)
