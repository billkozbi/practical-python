# bounce.py
#
# Exercise 1.5

bounce = 100
scale = 0.6

for i in range(10):
    bounce *= scale
    s = '{} {}'.format(i + 1, round(bounce, ndigits=4))
    print(s)