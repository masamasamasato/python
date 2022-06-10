from tkinter import N


def solution(X,Y,D):

    if (Y - X)%D >= 1:
        return (Y - X)//D +1
    else:
        return (Y - X)//D
    

if __name__ == '__main__':
    print(solution(10,85,30))
    print(solution(20,40,10))
    
