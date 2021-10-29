import sys

lat = sys.stdin.readline().split('-')
lat[-1] = lat[-1][:-1]

for i in range(len(lat)):
    lat[i] = list(map(int, lat[i].split('+')))

for i in range(len(lat)):
    lat[i] = sum(lat[i])

print(-sum(lat)+2*lat[0])