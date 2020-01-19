N, X = list(map(int,input().split()))

k_list = [int(input()) for i in range(N)]

bin_x = format(X, 'b')

str_bin_x = str(bin_x)

for k in k_list:
    print(str_bin_x[-k])