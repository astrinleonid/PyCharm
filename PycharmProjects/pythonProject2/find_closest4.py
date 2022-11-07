# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#
import random
import time


class Axis:
    def __init__(self, arr, L_F = True):
        self.n = len(arr)
        self.pos = 0 # keeps the position (one-dimensional index) of the point, which is the starting point of
        # the current pair in the iteration
        self.A_ind = [] # array of the one dimension coordinates, sorted and with the track of the original indexes
        for i in range(self.n):
            self.A_ind.append([arr[i], i])
        self.A_ind.sort()
        self.A_dist = [] # array of the distances between one dimension coordinates, sorted and with
        # the track of the indexes in the A_ind array. Each element of the A_dist array contains:
        # A_dist[i][0] - one-dimensional distance between the points in the pair
        # A_dist[i][1] - position (index in the A_ind array) of the starting point in the pair
        # A_dist[i][2] - shift in the index to the second point in such a way that the index in A_ind
        # of the second point in the pair equals A_dist[i][1] + A_dist[i][2]
        self.LA_dist = self.n - 1 # the length of the A_dist array
        self.Log = L_F # Debug feature
        self.iter = 0 # Debug feature
        for i in range(self.LA_dist):
            self.A_dist.append([self.A_ind[i + 1][0] - self.A_ind[i][0], i, 1])
        self.A_dist.sort()

    def Dist(self, pair):
        return self.A_ind[pair[1]][0] - self.A_ind[pair[0]][0]

    # returns the index of the point in the initial array
    def Get_point(self, a):
        return self.A_ind[a][1]

    def Get_pair(self, pos):
        a = self.A_dist[pos][1]
        b = a + self.A_dist[pos][2]
        return [a, b]

    # given the pair of indexes in the A_ind array, returns the pair of indexes in the original array
    def Get_pair_XY(self, pair):
        return [self.Get_point(pair[0]), self.Get_point(pair[1])]

    # given the position in the A_dist array, returns the pair of indexes in the initial array
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

    def FindPlace(self,ps,pf,d):
        for i in range(ps+1, pf):
            self.iter += 1
            ni = self.Get_pair(i)
            curr_dist = self.Dist(ni)
            if curr_dist >= d:
                return i
                break
        return pf

    def FindPlaceLog(self,ps,pf,d):
        self.iter += 1
        if pf - ps > 0:
            midpoint = ps + ((pf - ps) // 2)
#            print("ps ", ps, " pf ", pf, " midpoint ", midpoint)
            curr_dist = self.Dist(self.Get_pair(midpoint))
            if curr_dist > d:
                return self.FindPlaceLog(ps,midpoint,d)
            elif pf-ps == 1:
                return pf
            else:
                return self.FindPlaceLog(midpoint,pf,d)
        else:
            return pf

    # This function finds the next pair of points to be checked, returns one-dimension distance between the points
    # in the pair
    def Find_next_pos(self):

        new_pos = -1
        # for the current position increase the distance to the next point by 1. If the pair gets out of range,
        # it means that we run out of points for the current position, and we pop it
        self.A_dist[self.pos][2] += 1
        pair = self.Get_pair(self.pos)
        while self.Out_of_range(pair):
            if self.Pop_pos(self.pos) <= 0:
                return -1 # no more elements in A-dist, means we checked all possible pairs
            pair = self.Get_pair(self.pos)

        # find new place for the first element of the A_dist array

        cp_dist = self.Dist(pair)
        if self.Log:
            new_pos = self.FindPlaceLog(0, self.LA_dist, cp_dist)
        else:
            new_pos = self.FindPlace(0, self.LA_dist, cp_dist)

        if new_pos == self.LA_dist:
            element = self.A_dist[self.pos]
            self.A_dist.append(element)
            del self.A_dist[0]
            self.pos = 0
        elif new_pos > 1:
            element = self.A_dist[self.pos]
            self.A_dist.insert(new_pos, element)
            del self.A_dist[0]
            self.pos = 0

        # return the one-dimension distance between current pair of points
        return self.Dist(self.Get_pair(self.pos))


# returns the actual vector from the pair of indexes
def XY_pair(arr, pair):
    return [arr[pair[0]], arr[pair[1]]]

# returns the X dimension of the vector
def X_distance(pair):
    return abs(pair[1][0] - pair[0][0])

# returns the Y dimension of the vector
def Y_distance(pair):
    return abs(pair[1][1] - pair[0][1])

# calculates the length of the vector
def VectorLength(pair):
    x = X_distance(pair)
    y = Y_distance(pair)
    x2 = x * x
    y2 = y * y
    return x2 + y2


def closestSquaredDistance(x1, y1, Log_flag = True):

    # this is a debug feature
 #    max_n = 6000
    n = len(x1)
 #    n = min(len(x1),max_n)
    print(n)
 #   x = x1[:n]
 #   y = y1[:n]

    x = x1
    y = y1
    # main array to store all points
    arr = []
    for i in range(n):
        arr.append([x[i], y[i]])

    # we will check the vectors by the following algorythm: 1) Check the vector with shortest x-dimension.
    # 2) Check the vector with shortest y-dimension. 3) Check the vector with second-short x-dimension
    # 4) Check the vector with the second-short y-dimension 5) Progress in such a way iterating
    # intermittently over x and over y. Keep the track of the shortest vector found iterating over x and
    # of the shortest vector found iterating over y. While iterating over x, if we find that the x-dimension of
    # the vector we are currently checking is bigger than the x-dimension of the shortest vector found iterating over y,
    # we stop iterating over x. Similarly, while iterating over y, if we find that the y-dimension of
    # the vector we are currently checking is bigger than the y-dimension of the shortest vector found iterating over x,
    # we stop iterating over y. If both iterations stopped, then we already have the shortest vector.

    # in order to iterate by the dimensions of the vectors, for each dimension, we sort the array of the coordinates,
    # keeping the track of the original indexes. Then we make an array of the distances between neighbouring elements,
    # and sort it too, again keeping the track of the indexes. In order to handle this structure, we define the class Axis.
    # The iteration process is handled inside the class structure. At any given moment the Axis class variable returns
    # the pair of points to be checked at the current step in iteration (Get_pair and Get_current_pair methods)

    # Lof_flag is a debug feature, used to compare the running time with different methods
    A_X = Axis(x, Log_flag)
    A_Y = Axis(y, Log_flag)


    # get the indexes of the pair of points closest in y dimension
    close_pair = A_Y.Get_current_pair()
    # derive the actual vector from the pair of poins found
    close_pair_XY = XY_pair(arr, close_pair)
    # store the x-dimension of the vector found. The variable x_min_dist will keep the track of the x-dimention of
    # the shortest vector found iterating over x
    x_min_dist = X_distance(close_pair_XY)

    # get the indexes of the pair of points closest in x dimension
    close_pair = A_X.Get_current_pair()
    # derive the actual vector from the pair of poins found
    close_pair_XY = XY_pair(arr, close_pair)
    # store the x-dimension of the vector found. The variable y_min_dist will keep the track of the x-dimention of
    # the shortest vector found iterating over x
    y_min_dist = Y_distance(close_pair_XY)

    X_continue = True # x-iteration trigger
    Y_continue = True # y-iteration trigger
    # the length of the shortest vector found up to the moment
    min_dist = VectorLength(close_pair_XY)

    # this is a debug feature
    y_iter = 0
    x_iter = 0
    t = time.time()

    while X_continue or Y_continue:
        # one iteration over y dimension
        if Y_continue:
            y_iter += 1
            y_dist = A_Y.Find_next_pos()
            if y_dist < 0:
                # we didn't find a next vector over y dimension, means we run out of vectors.
                break

            if y_dist > y_min_dist:
                Y_continue = False

            current_pair = A_Y.Get_current_pair()
            current_pair_XY = XY_pair(arr, current_pair)
            current_dist = VectorLength(current_pair_XY)
            if current_dist <= min_dist: # new shortest vector found
                min_dist = current_dist # save the length of the shortest vector
                # saving the shortest vector itself (debug feature)
                close_pair[0] = current_pair[0]
                close_pair[1] = current_pair[1]
                x_min_dist = X_distance(current_pair_XY) # save the x-dimension of the shortest vector

        # one iteration over x dimension
        if X_continue:
            x_iter += 1
            x_dist = A_X.Find_next_pos()
            if x_dist < 0:
                break

            if x_dist > x_min_dist:
                X_continue = False

            current_pair = A_X.Get_current_pair()
            current_pair_XY = XY_pair(arr, current_pair)
            current_dist = VectorLength(current_pair_XY)
            if current_dist <= min_dist: # new shortest vector found
                min_dist = current_dist # save the length of the shortest vector
                # saving the shortest vector itself (debug feature)
                close_pair[0] = current_pair[0]
                close_pair[1] = current_pair[1]
                y_min_dist = Y_distance(current_pair_XY) # save the y-dimension of the shortest vector

    print("iterations on x ", x_iter)
    print("iterations on y ", y_iter)
    print("Total iterations ",A_X.iter+A_Y.iter)

    close_pair_XY = XY_pair(arr, close_pair)
    print("close_pair_XY ", close_pair_XY)
    t = time.time() - t
    print("Running time", t)
    return min_dist

