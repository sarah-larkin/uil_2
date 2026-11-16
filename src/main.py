import json
import os

from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from extract import extract_data

#Can update for other extractions: 
ACTION = "getScan"
FUNCTION = "InventoryManagement"

def main():

    load_dotenv()

    base_url = os.getenv("VISCO_BASE_URL")
    token = os.getenv("VISCO_TOKEN")
    extract_folder = os.getenv("EXTRACT_FOLDER", "extracts")
    row_limit = int(os.getenv("ROW_LIMIT", 20))

    data = extract_data(
        base_url=base_url,
        token=token,
        action=ACTION,
        function=FUNCTION
    )

    print(json.dumps(data, indent=2)[:3000])

    output_dir = Path(extract_folder)
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{ACTION}_{FUNCTION}_{timestamp}.json"

    output_file = output_dir / filename

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()


#save CSV as well as json
