n = 5
for i in range(n):
        print(' ' * (n-i-1) + '*' * (2*i + 1) + ' ' * (n-i-1))


# If we want to print the reverse pyramid structure Then we can just reverse the pattern 

for i in range(n):
    print(' ' * (i) + '*' * (2*(n-i)-1) + ' ' * (i)) 