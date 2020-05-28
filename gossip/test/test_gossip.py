from ..gossip import gossip


def test_gossips_never_spread_when_there_is_only_one_route():
    bus_routes = [[1, 2, 3, 4]]
    assert gossip(bus_routes) is None


def test_gossips_never_spread_with_multiple_routes_that_never_share_a_stop():
    bus_routes = [[1, 2, 3], [4, 5, 6]]
    assert gossip(bus_routes) is None


def test_all_gossip_is_spread_in_n_minutes_if_all_routes_share_the_n_plus_one_stop():
    bus_routes = [[1, 2, 3], [1, 4, 5]]
    assert gossip(bus_routes) == 0

    bus_routes = [[1, 2, 3], [4, 2, 5]]
    assert gossip(bus_routes) == 1

    bus_routes = [[1, 2, 3], [4, 5, 3]]
    assert gossip(bus_routes) == 2


def test_drivers_repeat_the_route_once_they_finish():
    bus_routes = [[1, 2], [3, 4, 5, 6, 7, 8, 1]]
    assert gossip(bus_routes) == 6


def test_drivers_drive_a_maximum_of_480_stops():
    bus_routes = [[1000, 480], list(range(1, 481))]
    assert gossip(bus_routes) == 479

    bus_routes = [[481, 1000], list(range(1, 482))]
    assert gossip(bus_routes) is None
