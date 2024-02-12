rooms = {
    "Start Room":"",
    "Blank Room":"",
    "Monster Room":"",
    "Treasure Room":""
}

current_location = "Start Room"

player_points = 0
attack_points = 0

while player_points == 0:
    print(rooms[current_location])
    next_move = input('Left or Right? (L/R?)')