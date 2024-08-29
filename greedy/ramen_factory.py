def min_ramen_cost(N, A):
    cost = 0
    
    # 세 공장에서 동시에 구매하는 경우를 먼저 처리
    for i in range(N - 2):
        if A[i+1] > A[i+2]:
            min_buy = min(A[i], A[i+1] - A[i+2])
            cost += 5 * min_buy
            A[i] -= min_buy
            A[i+1] -= min_buy

        min_buy = min(A[i], A[i+1], A[i+2])
        cost += 7 * min_buy
        A[i] -= min_buy
        A[i+1] -= min_buy
        A[i+2] -= min_buy

    # 두 공장에서 동시에 구매하는 경우 처리
    for i in range(N - 1):
        min_buy = min(A[i], A[i+1])
        cost += 5 * min_buy
        A[i] -= min_buy
        A[i+1] -= min_buy

    # 남은 라면은 각각의 공장에서 구매
    for i in range(N):
        cost += 3 * A[i]

    return cost

# 입력 및 출력 부분
N = int(input())  # 공장의 수
A = list(map(int, input().split()))  # 각 공장에서 구매해야 하는 라면의 수
print(min_ramen_cost(N, A))

