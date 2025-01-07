import sys;
import bisect;

T = int(sys.stdin.readline());

for case in range(T):
    N = int(sys.stdin.readline())
    diary1 = list(map(int,sys.stdin.readline().split()))
    diary1.sort();

    M = sys.stdin.readline()
    diary2 = list(map(int,sys.stdin.readline().split()))

    for item in diary2 :
        bisectValue = bisect.bisect_left(diary1,item);
        if (bisectValue <0 or bisectValue >= N or diary1[bisectValue] != item) :
            print(0)
        else :
            print(1)
