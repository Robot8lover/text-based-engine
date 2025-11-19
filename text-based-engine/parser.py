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
    if not all("" == line or line.isspace() for line in current_room):
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
    if not all("" == line or line.isspace() for line in current_room):
        rooms.append(current_room)
    return rooms

def parse_choice(choice):
    # Test if it is [text](#id) or (#id)
    # If the latter, text is the title of the room
    # Except that requires later knowledge hmmm.
    # So maybe we should make a later pass
    text_pattern = r"\[([\w ()[\]-]*)\](\(#([\w-]*)\))"
    id_pattern = r"(\(#([\w-]*)\))"
    choice = choice.strip()
    id_match = re.match(id_pattern, choice)
    if id_match:
        return None, id_match.group(1)
    else:
        return re.match(text_pattern, choice).group(1, 2) # or .groups()

def parse_choices_list(choices_list):
    choices = []
    pattern = r"\d+\.\s+"
    for line in choices_list:
        split = re.split(pattern, line)
        if len(split) == 1:
            # Reached extra line after choices
            # For now, we assume that this line must be unimportant (empty)
            break
        # We do not check for proper numbering
        choices.append(parse_choice(split[1]))
    return choices

def parse_room_body_list(room_body_list):
    body = {}
    pattern = r"\d+\.\s+"
    for i, line in enumerate(room_body_list):
        if re.match(pattern, line):
            body["text"] = "\n".join(room_body_list[:i])
            body["choices"] = parse_choices_list(room_body_list[i:])
            break
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

