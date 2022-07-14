timer = [300, 60, 10]

T = int(input()) # 1 <= T <= 10000
buttons = [0, 0, 0]

if T % timer[-1] != 0:
    print(-1)
    exit()

i = 0
for time in timer:
    count = T // time
    if count > 0:
        buttons[i] += count
        T %= time
    i += 1


for button in buttons:
    print(button, end = " ")