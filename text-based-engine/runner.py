from user_input import get_choice_input

def choices_to_str(choice_list: list) -> str:
    return "\n".join(f"{i+1}. {choice["text"]}" for i, choice in enumerate(choice_list))

def loop(rooms, start_id):
    current_id = start_id
    while True:
        current_room = rooms[current_id]
        room_body = current_room["body"]
        choices = room_body["choices"]
        print(current_room["title"])
        print()
        print(room_body["text"])
        print()
        print(choices_to_str(choices))
        next_index = get_choice_input(len(choices))
        current_id = choices[next_index]["id"]

def run():
    pass
