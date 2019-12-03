def main():
    #partOne()
    partTwo()
    

def partOne():
    P = [int(x) for x in open('input.txt').read().split(',')]
    P[1] = 12
    P[2] = 2
    ip = 0
    while True:
        opcode = P[ip]
        i1,i2,i3 = P[ip+1],P[ip+2],P[ip+3]
        print('')
        print(opcode, "--", i1, i2, i3)
        if opcode == 1:
            P[i3] = P[i1]+P[i2]
            print(P[i1], " + ", P[i2], " = ", P[i3])
        elif opcode == 2:
            P[i3] = P[i1]*P[i2]
            print(P[i1], " * ", P[i2], " = ", P[i3])
        else:
            print(opcode)
            assert (opcode == 99)
            break
        ip += 4
    print(P)

def partTwo():
    OP = [int(x) for x in open('input.txt').read().split(',')]
    
    for x1 in range(100):
        for x2 in range(100):
            P = [x for x in OP]
            P[1] = x1
            P[2] = x2
            ip = 0
            while True:
                opcode = P[ip]
                i1,i2,i3 = P[ip+1],P[ip+2],P[ip+3]
                if opcode == 1:
                    P[i3] = P[i1]+P[i2]
                elif opcode == 2:
                    P[i3] = P[i1]*P[i2]
                else:
                    assert (opcode == 99)
                    break
                ip += 4
            if P[0] == 19690720:
                print(x1,x2)
    

main()