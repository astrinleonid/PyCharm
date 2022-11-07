# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Axis:
    def __init__(self, arr):
        self.n = len(arr)
        self.pos = 0
        self.max_pos = 0
        self.A_ind = []
        for i in range(self.n):
            self.A_ind.append([arr[i], i])
        self.A_ind.sort()
        self.A_dist = []
        self.LA_dist = self.n - 1
        for i in range(self.LA_dist):
            self.A_dist.append([self.A_ind[i + 1][0] - self.A_ind[i][0], i, 1])
        self.A_dist.sort()

    def Dist(self, pair):
        return self.A_ind[pair[1]][0] - self.A_ind[pair[0]][0]

    def Get_point(self, a):
        return self.A_ind[a][1]

    def Get_pair(self, pos):
        a = self.A_dist[pos][1]
        b = a + self.A_dist[pos][2]
        return [a, b]

    def Get_pair_XY(self, pair):
        return [self.Get_point(pair[0]), self.Get_point(pair[1])]

    def Get_current_pair(self):
        return self.Get_pair_XY(self.Get_pair(self.pos))

    def Out_of_range(self, pair):
        if pair[0] < 0 or pair[0] > pair[1] or pair[1] >= self.n:
            return True
        else:
            return False

    def Pop_pos(self, pos):
        self.A_dist.pop(pos)
        self.LA_dist -= 1
        return self.LA_dist

    def Find_next_pos(self):

        new_pos = -1
        self.A_dist[self.pos][2] += 1

        pair = self.Get_pair(self.pos)

        while self.Out_of_range(pair):
            if self.Pop_pos(self.pos) <= 0:
                return -1
            pair = self.Get_pair(self.pos)

        # find new place for the first element of the A_dist array
        cp_dist = self.Dist(pair)
        print("cp_dist ", cp_dist)

        for i in range(1, self.LA_dist):
            ni = self.Get_pair(i)
            curr_dist = self.Dist(ni)
            print("curr_dist",curr_dist)
            #        print("Current distance = ", curr_dist, "pair ", ni)
            if curr_dist >= cp_dist:
                new_pos = i
                print("new_pos ", new_pos)
                break
        if new_pos < 0:
            return -1
        elif new_pos > 1:
            print("before moving ", self.A_dist)
            element = self.A_dist[self.pos]
            self.A_dist.insert(new_pos, element)
            del self.A_dist[0]
            print("after moving ", self.A_dist)
            self.pos = 0

            return self.Dist(self.Get_pair(self.pos))

        return self.Dist(self.Get_pair(self.pos))


def XY_pair(arr, pair):
    return [arr[pair[0]], arr[pair[1]]]


def X_distance(pair):
    return abs(pair[1][0] - pair[0][0])


def Y_distance(pair):
    return abs(pair[1][1] - pair[0][1])


def dist(pair):
    x = X_distance(pair)
    y = Y_distance(pair)
    x2 = x * x
    y2 = y * y
    return x2 + y2


def closestSquaredDistance(x, y):
    n = len(x)
    print("number of points ", n)
    arr = []

    for i in range(n):
        arr.append([x[i], y[i]])

    A_X = Axis(x)
    A_Y = Axis(y)

    close_pair = A_Y.Get_current_pair()
    close_pair_XY = XY_pair(arr, close_pair)
    x_min_dist = X_distance(close_pair_XY)

    close_pair = A_X.Get_current_pair()
    close_pair_XY = XY_pair(arr, close_pair)
    y_min_dist = Y_distance(close_pair_XY)

    X_continue = True
    Y_continue = True
    min_dist = dist(close_pair_XY)

    y_min_dist = Y_distance(close_pair_XY)
    y_iter = 0
    x_iter = 0
    y_distances = []
    x_distances = []
    while X_continue or Y_continue:
        if Y_continue:
            y_iter += 1

            y_dist = A_Y.Find_next_pos()
            if y_dist < 0:
                break
            y_distances.append(y_dist)
            if y_dist > y_min_dist:
                Y_continue = False
            current_pair = A_Y.Get_current_pair()
            current_pair_XY = XY_pair(arr, current_pair)
            current_dist = dist(current_pair_XY)
            if current_dist <= min_dist:
                min_dist = current_dist
                close_pair[0] = current_pair[0]
                close_pair[1] = current_pair[1]
                x_min_dist = X_distance(current_pair_XY)
        if X_continue:
            x_iter += 1
            x_dist = A_X.Find_next_pos()
            if x_dist < 0:
                break
            x_distances.append(x_dist)
            if x_dist > x_min_dist:
                X_continue = False
            current_pair = A_X.Get_current_pair()
            current_pair_XY = XY_pair(arr, current_pair)
            current_dist = dist(current_pair_XY)
            if current_dist <= min_dist:
                min_dist = current_dist
                close_pair[0] = current_pair[0]
                close_pair[1] = current_pair[1]
                y_min_dist = Y_distance(current_pair_XY)
    print("iterations on x ", x_iter)
    print("iterations on y ", y_iter)
    print("x distances ", x_distances)
    print("y distances ", y_distances)
    close_pair_XY = XY_pair(arr, close_pair)
    print("close_pair_XY ", close_pair_XY)
    return min_dist


def print_hi(str):
    x = [445152567, 767344406, 262763386, 702193038, 632784809, 283493647, 195698264, 799788254, 277474314, 365415143]
    y = [910984701, 219404802, 131039861, 425318360, 890312171, 927993176, 85421044, 537577753, 499341569, 429523681]
    min_dist = closestSquaredDistance(x, y)

    print(str, min_dist)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
