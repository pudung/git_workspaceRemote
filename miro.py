# make matrix
import numpy as np
n = 8
# 매트릭스를 행렬로 만들 때 오류를 발견.
miro = np.array([[0,0,0,0,0,0,0,1],
           [0,1,1,0,1,1,0,1],
           [0,0,0,1,0,0,0,1],
           [0,1,0,0,1,1,0,0],
           [0,1,1,1,0,0,1,1],
           [0,1,0,0,0,1,0,1],
           [0,0,0,1,0,0,0,1],
           [0,1,1,1,0,1,0,0]])

pathway_color = 0; # 통로
wall_color = 1; # 벽
blocked_color = 2; # 방문해봤지만, 출구로 가는 통로가 없는, 이미 방문한 셀
path_color = 3; # 방문해봤는데, 아직 출구로 가는 경로가 있는지 모르는지 모르는 셀
Is_escape = False;

def findMazePath(x, y, Is_escape):

    if x < 0 or y < 0 or x > n or y > n:
        print("if 1")
        return False

    elif x is n-1 and y is n-1:
        # 출구에 온 경우
        miro[x][y] == path_color
        print("if절 2")
        Is_escape == True
        return True

    else:
        miro[x][y] == path_color # 위의 3가지 경우가 아닌 경우 초록색으로,
        # 동서남북 확인 - 여기서 recursion 일어남. 8번 call 됨 .

        if (findMazePath(x+1,y,Is_escape) or findMazePath(x-1,y,Is_escape) or findMazePath(x,y+1,Is_escape) or findMazePath(x,y-1,Is_escape)):
            print("findMazePath?")
            Is_escape = True
            return Is_escape # 하나라도 출구가 있는 경우니까 true리턴 후, 빠져나온다.

        # else인경우?
        else:
            miro[x][y] == blocked_color
            Is_escape = False
            return Is_escape

print(findMazePath(0,0,Is_escape))















