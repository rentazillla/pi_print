# calculate nth digit of pi
# store 16 digits at a time then print them to the user
# but print them as binary representations

import numpy as np
from PIL import Image

# pi digit function based on
# https://math.hmc.edu/funfacts/finding-the-n-th-digit-of-pi/
# published by David Bailey, Peter Borwein, and Simon Plouffe in 1995
def pi_n(position):
  position = 16**-(position) * (
  (4/(8*position + 1)) - (2/(8*position+4))
  - (1/(8*position + 5)) - (1/(8*position + 6)))

  return(position)

# example
# n = 16
# pieces = []
# for i in range (0, n):
#   pieces.append(pi_n(i))
#
# pisum = np.sum(np.array(pieces))
# print(f'This is pi to {n:d} digits: {pisum:.{n:d}f}')

# better implementation
def S(j, n):
    # left sum
    s = 0.0
    k = 0
    while k <= n:
        r = 8*(k+j)
        s = (s + float(pow(16, n - k, r)) / r) % 1.0
        k += 1
    # right sum
    t = 0.0
    k = n +1
    while 1:
        newt = t + pow(16, n - k) / (8 * (k + j))
        # iterate until t no longer changes
        if t == newt:
            break
        else:
            t = newt
        k += 1
    return s + t

def pi(n):
    n -= 1
    x = (4 * S(1, n) - 2 * S(4, n) - 5 * S(5, n) - S(6, n)) % 1.0
    return x

def to_rgb(v):
    return np.array([int(v[1:3],16), int(v[3:5],16) , int(v[5:7],16)])

def main():
    final = [pi(0)]
    for i in range(1, 1080*720):
        pixeli = pi(i)
        final.append(pixeli)

    final_array = np.array(final)
    final_array *= (255.0/final_array.max())
    im = Image.fromarray(final_array.reshape((1080, 720)), mode = 'P')
    im.save('pies.png', optimize = True)

if __name__ == "__main__":
    main()
