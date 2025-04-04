S = int(input()); # S
num = 0;
count = 0;
key = 0; 

while True:

    num += 1;
    key += num;
    count += 1;

    if key == S :
        break;
    if key + num > S :
        key -= num;
        if (num-1 == S-key) :
            count -=1;
            break;
        num = S - key;
        key += num;
        break;

print(count);