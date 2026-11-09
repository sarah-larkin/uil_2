import json
import sys
from pathlib import Path
from datetime import datetime

from extract import extract_data


def main():

    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "python src/main.py action [function]"
        )
        return

    action = sys.argv[1]

    function = None

    if len(sys.argv) > 2:
        function = sys.argv[2]

    with open("config/settings.json") as f:
        config = json.load(f)

    data = extract_data(
        base_url=config["base_url"],
        token=config["token"],
        action=action,
        function=function
    )

    row_limit = config.get("row_limit", 20) #temp 

    output_dir = Path(config["extract_folder"])
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    name_parts = [action]

    if function:
        name_parts.append(function)

    filename = "_".join(name_parts)

    output_file = output_dir / f"{filename}_{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved to {output_file}")


if __name__ == "__main__":
    main()



