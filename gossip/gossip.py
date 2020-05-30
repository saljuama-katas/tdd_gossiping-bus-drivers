def gossip(routes):
    drivers = [BusDriver(route) for route in routes]
    if len(drivers) > 1:
        for x in range(480):
            if drivers[0].stop_at_minute(x) == drivers[1].stop_at_minute(x):
                return x

    return None


class BusDriver:
    def __init__(self, route):
        self.route = route

    def stop_at_minute(self, minute):
        return self.route[minute % len(self.route)]
