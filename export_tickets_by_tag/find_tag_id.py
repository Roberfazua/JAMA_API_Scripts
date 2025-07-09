# find_tag_id.py
import json
from datetime import datetime

# Basic no error handling version
# def find_tag_id(tags, tag_name):
#     matches = [tag for tag in tags if tag['name'] == tag_name]
#     filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - TagID.json"
#     with open(filename, 'w') as f:
#         json.dump(matches, f, indent=2)
#     return matches[0]['id'] if matches else None


# With Error Handling and Debugging
import json
import glob
from datetime import datetime

def get_latest_tags_file():
    files = sorted(glob.glob("*Tags.json"), reverse=True)
    if not files:
        print("No Tags.json file found.")
        return None
    return files[0]

def find_tag_id(tags, tag_name):
    tag_name_clean = tag_name.strip().lower()
    matches = [tag for tag in tags
               if isinstance(tag, dict) and tag.get('name', '').strip().lower() == tag_name_clean]

    if not matches:
        print(f"Tag '{tag_name}' not found.")
        print("Available tags (first 20):", [tag.get('name') for tag in tags[:20]])
        with open("debug_tags.json", "w") as f:
            json.dump(tags, f, indent=2)
        return None

    print(f"Found {len(matches)} match(es) for tag '{tag_name}':")
    for idx, tag in enumerate(matches, 1):
        print(f"{idx}: ID={tag.get('id')}, Name='{tag.get('name')}', Project={tag.get('project_id', 'N/A')}")

    filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - TagID.json"
    with open(filename, 'w') as f:
        json.dump(matches, f, indent=2)

    return matches[0].get('id')

if __name__ == "__main__":
    tags_file = get_latest_tags_file()
    if not tags_file:
        exit(1)
    with open(tags_file, "r", encoding="utf-8") as f:
        tags = json.load(f)
    tag_name = input("Enter tag name to search: ")
    tag_id = find_tag_id(tags, tag_name)
    print("Tag ID found:", tag_id)

