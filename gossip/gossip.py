import uuid


class GossipCalculator:
    def __init__(self, bus_routes):
        self.drivers = [BusDriver(route) for route in bus_routes]
        self.all_gossips = set([driver.initial_gossip for driver in self.drivers])

    def _update_gossips_for_minute(self, minute):
        for x in self.drivers:
            for y in self.drivers:
                if x.stop_at_minute(minute) == y.stop_at_minute(minute):
                    x.learn_gossip_from(y)

    def _do_all_drivers_know_all_gossips(self):
        for driver in self.drivers:
            if driver.known_gossips != self.all_gossips:
                return False
        return True

    def gossip_spread_time(self):
        if len(self.drivers) > 1:
            for x in range(480):
                self._update_gossips_for_minute(x)
                if self._do_all_drivers_know_all_gossips():
                    return x
        return None


class BusDriver:
    def __init__(self, route):
        self.route = route
        self.initial_gossip = uuid.uuid4()
        self.known_gossips = {self.initial_gossip}

    def stop_at_minute(self, minute):
        return self.route[minute % len(self.route)]

    def learn_gossip_from(self, driver):
        self.known_gossips.update(driver.known_gossips)
