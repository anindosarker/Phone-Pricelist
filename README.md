# Sumash Tech Phone Pricelist Formatter

This project provides a script to parse, sort, and format the Sumash Tech phone price listings from a text file into a structured CSV format. It supports a wide range of brands and handles both official and unofficial price listings as found in the Sumash Tech pricelist.

## Features

- Extracts phone data (brand, model, storage, price, variant, stock status, and official/unofficial status) from the Sumash Tech semi-structured text file.
- Supports many brands, including Google, Apple, Samsung, Xiaomi, Realme, OnePlus, Motorola, Honor, Oppo, Vivo, iQOO, Nothing, ZTE, Infinix, Nokia, Asus, Helio, XTRA, Maximus, DIZO, Tecno, Benco, Lenovo, and Amazon.
- Outputs a tab-separated CSV file for easy analysis and further processing.

## Requirements

- Python 3.7 or higher

## Usage

1. Place your Sumash Tech input file as `phone_prices.txt` in the project directory. The file should contain phone price listings in the expected format.
2. Run the script:
   ```bash
   python format_phone_prices.py
   ```
3. The script will generate `phone_prices.csv` in the same directory.

## Input Format

- The input file should contain lines with phone information, e.g.:
  ```
  iPhone 14 [128GB] ----------------------- BDT. 71,999/- USA | 76,499/- Global
  Galaxy F04 [4/64] -------------------- BDT 10,999/-
  Redmi Note 12 4G [6/64] --------------------- BDT. 18,499/- IND
  ```
- The script expects the storage information to be in square brackets `[ ]` and the price to follow the pattern `BDT. <amount>/-` as used in the Sumash Tech pricelist.

## Output

- The output file `phone_prices.csv` is a tab-separated CSV with the following columns:
  - Brand
  - Phone Name
  - Official/Unofficial
  - Storage
  - Variant
  - Price
  - Stock-Out

## Notes

- The script is designed to handle the most common formats in the Sumash Tech data. If some entries are missing, you may need to adjust the parsing logic in `format_phone_prices.py`.
- For best results, ensure your input file follows the Sumash Tech format as closely as possible.

## License

MIT
