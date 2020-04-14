N, X, Y = list(map(int,input().split()))

log_list = []

for i in range(N):
  l = [i]
  log_list.append(l)

log_before = []
log_after = []

for i in range(N):
  l = []
  if(i - 1 >= 0):
    l.append(i - 1)
  if(i == X - 1):
    l.append(Y - 1)
  if(i == Y - 1):
    l.append(X - 1)
  if(i + 1 <= N - 1):
    l.append(i + 1)
  log_before.append(l)

print(log_before)

