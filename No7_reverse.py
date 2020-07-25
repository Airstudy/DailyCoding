#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# 重点在于判断是否溢出， 32位的范围 [-2^31, 2^31)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 判断是否为负
        is_neg = True if x < 0 else False
        num_str = str(-x) if is_neg else str(x)
        # 赋值给新的字符串
        new_num_str = ''
        for i in range(len(num_str)-1, -1, -1):
            new_num_str += num_str[i]
        print(new_num_str)
        # 判断是否会溢出
        threshold = pow(2,31)  # 2147483648
        if is_neg and int(new_num_str) <= threshold:
            new_num = -int(new_num_str)
        elif not is_neg and int(new_num_str) < threshold:
            new_num = int(new_num_str)
        else:
            new_num = 0
        return new_num
