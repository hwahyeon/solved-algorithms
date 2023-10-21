def convert_to_seconds(t):
    return t[0] * 3600 + t[1] * 60 + t[2]

n = list(map(int, input().split(':')))
s = list(map(int, input().split(':')))

n_sec = convert_to_seconds(n)
s_sec = convert_to_seconds(s)

if n_sec >= s_sec:
    s_sec += 24 * 3600

elapsed = s_sec - n_sec

print(f"{elapsed // 3600:02}:{(elapsed % 3600) // 60:02}:{elapsed % 60:02}")
