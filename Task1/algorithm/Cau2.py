def n_steps(x, y):
    steps = ""
    while(x != y):
        if x > y/2:
            if x * 2 == (y + 1):
                x *= 2
                steps += "*"
            else:
                x -= 1
                steps += "-"

        elif x <= y/2:
            x *= 2
            steps += "*"
    
    return len(steps)

print(n_steps(5,11))