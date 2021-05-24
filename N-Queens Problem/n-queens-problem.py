"""
Placing N queens on an NxN chessboard using the backtracking method.
"""
import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt

#Number of queens
# N = int(input("Enter the number of queens: "))
# N = 4

# # Creating nxn Chessboard Matrix with 0 as default

QUEEN = 1
N = 0
def main(N):
    # board = np.zeros((N,N), dtype= np.int64)
    board = [[0]*N for _ in range(N)]

    start = timer()

    N_queen(N)

    end = timer()


    # # printing each row
    # for i in board:
    #     print(str(i))
    #     # ♕

    print(f'\n[TIME TAKEN] {end-start}s')




def is_attack(i, j):
    # queen row and col attack check
    for k in range(0,N):
        if board[i][k] == QUEEN or board[k][j] == QUEEN:
            return True

    # queen diagonal attack check
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l] == QUEEN:
                    return True

    # not under attack
    return False


def N_queen(n):
    # no queens base case :/
    if n == 0:
        return True

    # row
    for i in range(0,N):
        # col
        for j in range(0,N):
            '''
            checking if we can place a queen here or not.
            Conditions:
                1. is occupied already?
                2. can be placed without being under attack
            If not, then queen will not be placed and we'll back track
            '''
            if ( not(is_attack(i,j)) ) and ( board[i][j]!=1 ):
                # queen placed
                board[i][j] = QUEEN

                #recursive
                if N_queen(n-1)==True:
                    return True

                # for this timeline, the board will be empty
                board[i][j] = 0

    return False



def plot_complexity(func, stop):
    title = "N-Queens problem"
    data = {
        'length of list':[],
        'time taken': []
    }

    for i in range(1, stop):
        N = i
        start = timer()
        func(i)
        end = timer()

        print(f'Queens problem of {i} for {i}x{i} in {end-start}s')

        data['length of list'].append(i)
        data['time taken'].append(end-start)

    plt.plot(data['length of list'], data['time taken'], label=title)
    plt.title(title)
    plt.xlabel('No. of Queens')
    plt.ylabel('Time taken')
    plt.show()




if __name__ == '__main__':
    plot_complexity(main, 8500)
