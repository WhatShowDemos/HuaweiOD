f = open("in")

for i in range(2):
    flights_raw = f.readline().strip().split(',')
    
    flights = [];
    for flight_raw in flights_raw:
        flights.append([flight_raw[0:2], flight_raw[2:]]);
    # lambda是匿名函数
    flights.sort(key = lambda x: (x[0], x[1]));
    
    flights_str = [];
    for flight in flights:
        flights_str.append(flight[0] + str(flight[1]));
    print(" ".join(flights_str))

f.close();