def gossip(routes):
    if len(routes) > 1:
        for x in range(480):
            if routes[0][x % len(routes[0])] == routes[1][x % len(routes[1])]:
                return x

    return None
