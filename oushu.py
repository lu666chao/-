def even(x):
    z = 0
    for i in x:
        if i % 2 == 0:  #求偶数
            z += 1
            print('偶数位置：', [i])
    return z

a = even([1, 2, 3, 4, 5, 6])  # 输入序列
print('序列中偶数的个数为：', a)