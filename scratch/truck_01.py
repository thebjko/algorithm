# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# http://icpckorea.org/2016/ONLINE/problem.pdf
def solution(bridge_length, weight, truck_weights):
    time_lapse = 1
    offset = 0
    n_trucks = len(truck_weights)
    for i in range(n_trucks):
        i += offset
        if i >= n_trucks:
            break
        for j in range(min(bridge_length, n_trucks-i), 0, -1):
            s, l = sum(truck_weights[i:i+j]), len(truck_weights[i:i+j])
            if s <= weight and l <= bridge_length:
                time_lapse += bridge_length + l - 1   # 4가 다 지나가기 전에 3이 올라온다.
                offset += j - 1
                break
    return time_lapse

if __name__ == '__main__':
    import sys
    sys.stdin = open('truck_01.txt')
    input = sys.stdin.readline
    for tc in range(int(input())):
        bridge_length, weight = map(int, input().split())
        truck_weights = list(map(int, input().split()))
        print(solution(bridge_length, weight, truck_weights))