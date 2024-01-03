class States:
    IDLE = 1
    LOADING =2
    LOADED=3
    DELIVERING=4
    DELIVERED=5
    RETURNING=6

productStates = States()

class DronStatus:
    active = 1
    inactive =2
dronStatus = DronStatus