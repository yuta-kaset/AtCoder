from pprint import pprint


N = int(input())
p = [[]]
for i in range(N):
    p.append(list(map(int, input().split())))


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        m[i][i] = 0
    for l in range(2, n + 1):  # 部分行列積の長さは2~n
        for i in range(1, n + 2 - l):  # 始まりの地点は1~n+1-lまで
            j = i + l - 1  # 終わりの地点はi+1~i+l-1まで。i<jとなるように。
            m[i][j] = float("inf")
            # 行列積A(i)..A(j)を部分行列積A(i)..A(k)とA(k+1)..A(j)に分けてそれぞれの最小乗算回数と各部分行列積の結果の行列を乗算する
            # ただし、i<=k<j
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i][0] * p[k][1] * p[j][1]
                if q < m[i][j]:
                    m[i][j] = q
    pprint(m)
    return m[1][n]


print(matrix_chain_order(p))
