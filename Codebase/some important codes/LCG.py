import matplotlib.pyplot as plt
def getNextLCG(X, m, a, c):
    return (X*a + c)%m

Xi = 5453254554
N_num = 100
Rand_arr = [Xi]
for i in range(N_num):
    m = 4464667
    a = 1544543
    c = 57513
    Rand_arr.append(getNextLCG(Rand_arr[i], m, a, c))
# print(Rand_arr)

plt.scatter(Rand_arr[1:-1], Rand_arr[2:])
plt.show()

