bus = []
arrived = 0
with open("bus.txt", "r") as file:
    all_seats = int(next(file))
    for pas in file:
        bus = [i - 1 for i in bus]
        print(1, bus)
        pas_exit = bus.count(0)
        arrived += pas_exit

        for i in range(pas_exit):
            bus.remove(0)

        print(2, bus)
        pas_list = pas.strip().split()
        pas = map(int, pas_list)
        free_seats = all_seats - len(bus)
        free_seats = min(free_seats, len(pas_list))
        for i in range(free_seats):
            bus.append(next(pas))
        print(3, bus)
        print()

print(arrived)
