import sys
import copy
sys.setrecursionlimit(10000)

# define
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
ans_count = sys.maxsize

height, width = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())

arrive = [[0 for i in range(width)] for l in range(height)]
input_map = []

for i in range(height):
    input_map.append(list(input()))

def solve(current_x, current_y, local_arrive, count):
    global width
    global height
    global goal_x
    global goal_y
    global ans_count
    global input_map

    local_arrive[current_y][current_x] = 1
    if goal_x - 1 == current_x and goal_y - 1 == current_y:
        ans_count = min(ans_count, count)

    ## debug
    # for i in range(height):
    #     for l in range(width):
    #         print(arrive[i][l], end='')
    #     print()
    # print()

    for x, y in zip(dx, dy):
        ## 場外に行っているか，もうすでに行ったことのある経路は行かないようにする
        if current_y + y < 0 or current_y + y >= height or current_x + x < 0 or current_x + x >= width:
            continue
        if local_arrive[current_y + y][current_x + x] == 1:
            continue
        if input_map[current_y + y][current_x + x] == '#':
            continue

        solve(current_x + x, current_y + y, copy.deepcopy(local_arrive), 1 + count)
        print('count:{0}, cur_x:{1}, cur_y:{2}'.format(count, current_x + x, current_y + y))
        for i in range(height):
            for l in range(width):
                print(local_arrive[i][l], end='')
            print()
        print()

solve(start_x - 1, start_y - 1, copy.deepcopy(arrive), 0)
print(ans_count)
