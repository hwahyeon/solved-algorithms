# 첫 번째 풀이 : 왜 틀렸는지 잘 모르겠다.
h, m, s = map(int, input().split())
add_ = int(input())
tot = (h*3600)+(m*60)+s+add_

h_r, m_2 = divmod(tot, 3600)
m_r, s_r = divmod(m_2, 60)
if h_r > 23:
    h_r -= 24
print(f'{h_r} {m_r} {s_r}')


# 두 번째 풀이
h,m,s = map(int,input().split())
add_ = int(input())

s1 = (s+add_)%60
m1 = (s+add_)//60

m2 = (m+m1)%60
h1 = (m+m1)//60

h2 = (h+h1)%24

print(h2,m2,s1)
