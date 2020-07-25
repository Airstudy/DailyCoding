#include <math.h>

class Solution {
public:
    // 主要是防止溢出
    int reverse(int x) {
        int cur_num = 0;
        // 判断是不是-2^31, 否则会出现溢出
        if(abs(x) == pow(2, 31)){
            return 0;
        }else{
            cur_num = abs(x);
        }
        // 使用long型，避免dst_num溢出
        long dst_num = 0;
        int single = 0;
        while(cur_num > 0){
            single = cur_num % 10;
            dst_num = dst_num * 10 + single;
            cur_num = cur_num / 10;
        }
        if(x<0){
            dst_num = -dst_num;
        }
        long threshold = pow(2, 31);
        if(dst_num < -threshold || dst_num >= threshold){
            dst_num = 0;
        }
        return dst_num;
    }
};
