import re

def parse_file(file):
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
    if not all("" = line or line.isspace() for line in current_room):
        rooms.append(current_room)
    return rooms

def parse_text(file):
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
    if not all("" = line or line.isspace() for line in current_room):
        rooms.append(current_room)
    return rooms

def parse_room_body_list(room_body_list):
    body = {}
    in_choices = False
    pattern = r"\d+\.\s+"
    for i, line in enumerate(room_body_list):
        split = re.split(pattern, line)
        if in_choices:
            if len(split) == 1:
                # Reached extra space after choices
                break
            body["choices"].append(split[1])
        elif len(split) > 1:
            body["text"] = "\n".join(room_body_list[:i])
            body["choices"] = [split[1]]
            in_choices = True
    return body

def parse_room_lists(room_lists):
    rooms = {}
    for current_room in room_lists:
        title = current_room[0].strip()
        room_id = current_room[1].strip()
        if room_id[0] == "#":
            # otherwise, we don't have an id maybe
            # depending on our choices
            # and then maybe we should assign it?
            room_id = room_id[1:].strip() # or just lstrip
        room_body = parse_room_body_list(current_room[2:])
        if room_id in rooms:
            raise ValueError(f"Room id {room_id} is not unique")
        else:
            rooms[room_id] = {
                    "title": title,
                    "body": room_body,
            }
    return rooms

