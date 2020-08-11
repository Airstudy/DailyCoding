#!/usr/bin/env python
import copy
def solveNQueens(n):
    # 定义递归函数
    def unit_queen(q_list, cur):
        '''
        q_list: 当前的list
        cur: 当前皇后在的列
        '''
        if cur == n:  # 所有行皇后互不冲突， 则将list添加到结果中
            save_list = copy.deepcopy(q_list)  # 注意此处得用深拷贝
            all_queen.append(save_list)
            return
        # 遍历每一列
        for col in range(0, n):
            q_list[cur] = col  # 第cur个（行）皇后在col列
            flag = True
            for row in range(0, cur):
                # 两个（行）皇后在同一列 或者 两个（行）皇后在对角线
                if q_list[row] == col or abs(q_list[row] - col) == cur - row:
                    flag = False
            if flag:
                unit_queen(q_list, cur + 1)
    # 开始递归
    all_queen = []  # 保存满足条件的list
    queen_list = ['0'] * n  # 初始化皇后list， 下标idx皇后对应矩阵中第idx行皇后
    unit_queen(queen_list, 0)  # 所以可能的情况
    return all_queen
