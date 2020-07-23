class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_len = len(s)
        # 注意特殊情况
        if s_len < 3 or numRows <2:
            return s
        # Step1 计算至少需要多少组（一组为"一竖+一折"）
        c_num = s_len/(2*numRows-2) * (numRows-1)
        # 在Step1 的基础上，查看后边还需几列
        remain_len = s_len - (2*numRows-2) * (c_num/(numRows-1))
        if remain_len == 0:
            c_num += 0
        else:
            c_num += remain_len%numRows + 1
        # new_s = [['0']*c_num]*numRows  # 注意行和列
        new_s = []
        for i in range(0, numRows):
            tmp = []
            for j in range(0, c_num):
                tmp.append('0')
            new_s.append(tmp)
        # 赋值给新的
        s_i = 0
        cur_i = 0
        cur_j = 0
        while s_i<s_len:
            while cur_i<numRows and cur_j<c_num and s_i<s_len:
                # print('cur_i={}, cur_j={}, s_i={}'.format(cur_i, cur_j, s_i))
                new_s[cur_i][cur_j] = s[s_i]
                cur_i += 1
                s_i += 1
            cur_i = cur_i - 2
            cur_j = cur_j + 1
            while s_i<s_len and cur_i>0 and cur_j<c_num:
                # print('cur_i={}, cur_j={}, s_i={}'.format(cur_i, cur_j, s_i))
                new_s[cur_i][cur_j] = s[s_i]
                # print('s[s_i]={}'.format(s[s_i]))
                cur_i -= 1
                cur_j += 1
                s_i += 1
            cur_i = 0
        # print(new_s)
        # 按行读取有效字符，并输出
        out_s= ''
        for i in range(0,numRows):
            for j in range(0,c_num):
                c = new_s[i][j]
                if c != '0':
                    out_s += c
        return out_s

