# deloitte

# Jamdani Telemetry Data Format Converter

This Python project demonstrates how to convert telemetry data from **two different JSON formats** into a **single unified JSON format** using Python.

It includes:
- `data-1.json` — Format 1 (uses epoch timestamp and combined location string)
- `data-2.json` — Format 2 (uses ISO timestamp and separate location fields)
- `data-result.json` — Target unified format (the desired output)

## 📂 Project Structure

├── main.py
├── data-1.json
├── data-2.json
├── data-result.json
## ⚙️ How it works

- **convertFromFormat1()**  
  Converts Format 1:
  - Uses existing epoch timestamp.
  - Splits the `location` string into structured parts.
  - Maps `operationStatus` to `data.status` and `temp` to `data.temperature`.

- **convertFromFormat2()**  
  Converts Format 2:
  - Converts ISO timestamp to epoch milliseconds.
  - Combines separate `country`, `city`, `area`, `factory`, `section` into a single `location` dictionary.
  - Maps nested `device` fields.

- **main()**  
  Detects which format to convert based on keys and routes to the correct converter.

- **Unit tests**  
  Automatically verify that both conversions produce exactly the expected result in `data-result.json`.

## 🚀 Running the project

1. Install Python 3 (if not already installed).
2. Clone this repository.
3. Make sure `main.py` and all `data-*.json` files are in the same directory.
4. Run the tests:

```bash
python main.py
If all goes well, you’ll see:

python-repl
Copy
Edit
...
OK
