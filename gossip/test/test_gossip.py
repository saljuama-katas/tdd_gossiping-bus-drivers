from ..gossip import GossipCalculator


def test_gossips_never_spread_when_there_is_only_one_route():
    calculator = GossipCalculator([[1, 2, 3, 4]])
    assert calculator.gossip_spread_time() is None


def test_gossips_never_spread_with_multiple_routes_that_never_share_a_stop():
    calculator = GossipCalculator([[1, 2, 3], [4, 5, 6]])
    assert calculator.gossip_spread_time() is None


def test_all_gossip_is_spread_in_n_minutes_if_all_routes_share_the_n_plus_one_stop():
    calculator = GossipCalculator([[1, 2, 3], [1, 4, 5]])
    assert calculator.gossip_spread_time() == 0

    calculator = GossipCalculator([[1, 2, 3], [4, 2, 5]])
    assert calculator.gossip_spread_time() == 1

    calculator = GossipCalculator([[1, 2, 3], [4, 5, 3]])
    assert calculator.gossip_spread_time() == 2


def test_drivers_repeat_the_route_once_they_finish():
    calculator = GossipCalculator([[1, 2], [3, 4, 5, 6, 7, 8, 1]])
    assert calculator.gossip_spread_time() == 6


def test_drivers_drive_a_maximum_of_480_stops():
    calculator = GossipCalculator([[1000, 480], list(range(1, 481))])
    assert calculator.gossip_spread_time() == 479

    calculator = GossipCalculator([[481, 1000], list(range(1, 482))])
    assert calculator.gossip_spread_time() is None


def test_gossip_never_spreads_if_one_driver_does_not_get_all_gossips():
    calculator = GossipCalculator([
        [1, 2, 3],
        [1, 3, 4],
        [7, 8, 9]
    ])
    assert calculator.gossip_spread_time() is None


def test_gossip_can_be_spread_without_direct_contact():
    calculator = GossipCalculator([
        [1, 2, 3],   # learns about 2 in stop 0, learns about 3 in stop 3 (via driver 2)
        [1, 3, 4],   # learns about 1 in stop 0, learns about 3 in stop 1
        [5, 3, 6]    # learns about 1 (via driver 2) and 2 in stop 1
    ])
    assert calculator.gossip_spread_time() == 3
