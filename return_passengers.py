def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

#beberapa ada yang naik/turun di Bukittinggi dan jambi
bus_stops = [(25, 0), (4, 5), (3, 2)]
print(number(bus_stops)) #jadi total jumlah penumpang tujuan jakarta: 25
