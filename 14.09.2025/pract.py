bus = []
arrived = 0
with open("bus.txt", "r", encoding="utf-8") as f:
    all_seats = int(next(f))
    for pas in f:
        bus = [i - 1 for i in bus]
        pas_exit = bus.count(0)
        arrived += pas_exit
        for i in range(pas_exit):
            bus.remove(0)
        pas_list = pas.strip().split()
        
        j = 0
        while len(bus) < all_seats and j < len(pas_list):
                bus.append(int(pas_list[j]))
                j += 1
print(arrived)


















# with open("bus.txt", "r", encoding="utf-8") as f:
#   data = f.read()
# data = data.split(sep="\n")

# mest = int(data[0])
# data = data[1:len(data)]
# print(data)


