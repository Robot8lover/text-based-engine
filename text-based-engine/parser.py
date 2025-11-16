def parseFile(file):
    """
    Splits a file into room text arrays.
    """
    rooms = []
    current_room = []
    for line in file:
        if line == "---":
            rooms.append(current_room)
            current_room = []
        else:
            current_room.append(line)
    if current_room:
        rooms.append(current_room)
    return rooms

def parseText(file):
    """
    Splits a string into room text arrays.
    """
    rooms = []
    current_room = []
    for line in file.split("\n"):
        if line == "---":
            rooms.append(current_room)
            current_room = []
        else:
            current_room.append(line)
    if current_room:
        rooms.append(current_room)
    return rooms

