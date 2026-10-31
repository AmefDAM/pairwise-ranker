from collections import OrderedDict


# File errors are propagated to the caller for handling.
def load_items(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        items_raw = [line.strip() for line in file if line.strip()]

    items = list(OrderedDict.fromkeys(items_raw))
    return items