import re
import csv


def parse_phone_data(line):
    # Extract brand
    brand = None
    if "Google" in line:
        brand = "Google"
    elif "Apple" in line or "iPhone" in line or "iPad" in line or "Mac" in line:
        brand = "Apple"
    elif "Samsung" in line or "Galaxy" in line:
        brand = "Samsung"
    elif "Xiaomi" in line or "Redmi" in line or "Poco" in line:
        brand = "Xiaomi"
    elif "Amazon" in line:
        brand = "Amazon"

    # Skip if it's a header or warranty line
    if not brand or "Warranty" in line or "Price" in line or "————" in line:
        return None

    # Extract phone name and storage
    match = re.match(r"([^[]+)\s*\[([^\]]+)\]\s*[-]*\s*BDT\.?\s*([\d,]+)/-", line)
    if not match:
        return None

    phone_name = match.group(1).strip()
    storage = match.group(2).strip()
    price = match.group(3).strip().replace(",", "")

    # Determine if it's official or unofficial
    official = "Official"
    if "CN" in line or "IND" in line or "INT" in line:
        official = "Unofficial"

    # Extract variant (if any)
    variant = ""
    if "USA" in line:
        variant = "USA"
    elif "Global" in line:
        variant = "Global"
    elif "Dual" in line:
        variant = "Dual"
    elif "Single" in line:
        variant = "Single"

    # Check if out of stock
    stock_status = ""
    if "OUT" in line:
        stock_status = "Out of Stock"

    return {
        "Brand": brand,
        "Phone Name": phone_name,
        "Official/Unofficial": official,
        "Storage": storage,
        "Variant": variant,
        "Price": price,
        "Stock-Out": stock_status,
    }


def main():
    with open("phone_prices.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    phones = []
    for line in lines:
        phone_data = parse_phone_data(line)
        if phone_data:
            phones.append(phone_data)

    # Write to CSV
    with open("phone_prices.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "Brand",
            "Phone Name",
            "Official/Unofficial",
            "Storage",
            "Variant",
            "Price",
            "Stock-Out",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for phone in phones:
            writer.writerow(phone)


if __name__ == "__main__":
    main()
