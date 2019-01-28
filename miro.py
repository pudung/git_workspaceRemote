# make matrix
import numpy as np
n=8
miro = np.matrix([[0,0,0,0,0,0,0,1],
           [0,1,1,0,1,1,0,1],
           [0,0,0,1,0,0,0,1],
           [0,1,0,0,1,1,0,0],
           [0,1,1,1,0,0,1,1],
           [0,1,0,0,0,1,0,1],
           [0,0,0,1,0,0,0,1],
           [0,1,1,1,0,1,0,0]])
# 변수 지정

pathway_color = 0; # 통로
wall_color = 1; # 벽
blocked_color = 2; # 방문해봤지만, 출구로 가는 통로가 없는, 이미 방문한 셀
path_color = 3; # 방문해봤는데, 아직 출구로 가는 경로가 있는지 모르는지 모르는 셀

def findMazePath(x, y):
    if x<0 or y<0 or x>=n or y >= n:
        return False

    elif miro[x][y] is not pathway_color: # != 말고 is not으로 고치기.
        return False

    elif x is n-1 and y is n-1:
        # 출구에 온 경우
        miro[x][y] == path_color
        return True
    else:
        miro[x][y] is path_color # 위의 3가지 경우가 아닌 경우 초록색으로,
        # 동서남북 확인 - 여기서 recursion 일어남.
        if (findMazePath(x+1,y) or findMazePath(x-1,y) or findMazePath(x,y+1) or findMazePath(x,y-1)):
            return True # 하나라도 출구가 있는 경우니까 true리턴 후, 빠져나온다.
        else:
            miro[x][y] is blocked_color
            return False

def main():
    findMazePath(0,0) # (0,0 부터 시작)
    # x가 n-1 m-1일때 까지 반복
    for i in range(0,n): # 행에서 열 +1 증가
        for j in range(0,n):
            print(miro[i][j])

# 함수를 실행해봅시다.
print(main())
















