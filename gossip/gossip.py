class GossipCalculator:
    def __init__(self, bus_routes):
        self.drivers = [BusDriver(route) for route in bus_routes]

    def gossip_spread_time(self):
        if len(self.drivers) > 1:
            for x in range(480):
                if self.drivers[0].stop_at_minute(x) == self.drivers[1].stop_at_minute(x):
                    return x
        return None


class BusDriver:
    def __init__(self, route):
        self.route = route

    def stop_at_minute(self, minute):
        return self.route[minute % len(self.route)]
