import re


def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub(r"[^a-z0-9-.\_]", "", new_id)
    # 3
    while True:
        if ".." not in new_id:
            break

        new_id = new_id.replace("..", ".")

    print(new_id)
    # 4
    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_id = new_id[:-1]

    print(new_id)
    # 5
    if new_id == "":
        new_id = "a"

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id.endswith("."):
        new_id = new_id[:-1]

    # 7
    while True:
        if len(new_id) >= 3:
            break

        new_id += new_id[-1]

    print(new_id)
    return new_id