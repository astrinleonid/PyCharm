
import sys

a = []
result = True
for i in range(2):
    try:
        a.append(float(sys.argv[i+1]))
    except:
        result = False

if result:
    print(a)
    print(a[0]+a[1])
    print(abs(a[0] - a[1]))
    print(a[0] * a[1])
else:
    print("Invalid argument")
