# input
import re
M, D, x, Y, T = re.split('[ ,]', input())
cur_y = int(Y)
cur_m = M
cur_d = int(D)
cur_hh, cur_mm = map(int, T.split(':'))

# days, months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if cur_y % 400 == 0 or (cur_y % 4 == 0 and cur_y % 100 != 0):
    days[1] += 1

# minutes
tot_d = sum(days[:months.index(cur_m)]) + cur_d - 1
tot_mm = (tot_d * 24 * 60) + (cur_hh * 60) + (cur_mm)

print((tot_mm / (sum(days) * 24 * 60) * 100))
