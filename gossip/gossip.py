def gossip(routes):
    if len(routes) < 2:
        return None

    if routes[0][0] == routes[1][0]:
        return 0
    elif routes[0][1] == routes[1][1]:
        return 1
    else:
        return None
