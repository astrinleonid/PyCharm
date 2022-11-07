
import sys
try:
    a1 = float(sys.argv[1])
except:
    print("Invalid argument 1")
try:
    a2 = float(sys.argv[2])
except:
    print("Invalid argument 2")
print(a1,a2)
print(a1 + a2)
print(abs(a1 - a2))
print(a1 * a2)