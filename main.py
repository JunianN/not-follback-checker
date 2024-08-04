import json


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


followers_data = load_json("followers.json")
following_data = load_json("following.json")
following_data = following_data["relationships_following"]

followers = {entry["string_list_data"][0]["value"] for entry in followers_data}
following = {entry["string_list_data"][0]["value"] for entry in following_data}

not_following_back = following - followers

for account in not_following_back:
    print(account)
