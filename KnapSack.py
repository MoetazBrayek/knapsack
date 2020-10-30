import colorama
colorama.init()

CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'
RESET = '\033[0m'
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[m"
REVERSE = "\033[m"
def sacproblem(W, wt, val, n):
    # return to break all lops -_-
    a = ''' 


  ______                _ _   
 |  ____|              (_) |  
 | |__   ___ _ __  _ __ _| |_ 
 |  __| / __| '_ \| '__| | __|
 | |____\__ \ |_) | |  | | |_ 
 |______|___/ .__/|_|  |_|\__|
            | |               
            |_|   2020   
                Moetaz Brayek
                Cyrine chebby
                Sadek sellmi
                         

    i'm not a programmer , i'm a coder . !
    '''
    print RED+a+RESET
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print "======================================"
print GREEN+"I Think Max Is , ... ==>  "+str((sacproblem(W, wt, val, n)))+RESET
print "======================================"
