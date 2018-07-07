# taro 문제
# 타로는 맛있는 키위주스를 준비했습니다. 타로는 0부터 N-1 이라 이름을 붙인 N 개의 병에 키위주스를 넣었습니다. 이때 i번째 병의 용량은 capacites[i]
# 타로가 i번째 병에 넣은 키위주스의양을 bottles[i]라고 한다
# 타로는 병에 키위주스를 재분배하려고하며, 0부터 M-1까지 M회 조작합니다 i번째 조작은 타로가 fromId[i]부터 toId[i]에 키위주스를 넣는것을 의미합니다
# 병 fromId[i]가 비어있거나 toId[i]가 꽉 차잇는 순간 타로는 더이상 주스를 넣지않는다
# N개의 요소륵ㄹ 가진 정수 배열 int[] 를 리턴해주세요 배열 i번째 요소는 모든주스를 쏟는 작업이 완료되고 i번째 병에 남아있는 키위주스양 입니다.

capacites = [20, 20]  # 병의 순수용량
bottles = [5, 8]  # 키위주스의 양
fromId = [0]
toId = [1]

cap1 = [30, 20, 10]
bot1 = [10, 5, 5]
fromId = [0, 1, 2]
toId = [1, 2, 0]

cap1 = [14, 35, 86, 58, 25, 62]
bot1 = [6, 34, 27, 38, 9, 60]
fromId = [1, 2, 4, 5, 3, 3, 1, 0]
toId = [0, 1, 2, 4, 2, 5, 3, 1]

for idx, fromId in enumerate(fromId):
    if cap1[toId[idx]] - (bot1[fromId] + bot1[toId[idx]]) > 0:
        bot1[toId[idx]] += bot1[fromId]
        bot1[fromId] = 0
    else:
        a = cap1[toId[idx]] - bot1[toId[idx]]
        bot1[fromId] -= a
        bot1[toId[idx]] += a

for i in bot1:
    print(i)
