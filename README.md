# Crop Yield Monitoring System
**Course:** PROG211 – Object-Oriented Programming 1  
**Project domain:** Agriculture

## Overview
A Python command-line program for adding, listing, and summarising crop yield records. It demonstrates classes, objects, attributes, instance methods, a class method, and a list data structure.

## Requirements
- Python 3.8 or later
- No external libraries are required

## How to run
1. Install Python 3 if it is not already installed.
2. Save `crop_yield_monitoring.py` to a folder.
3. Open a terminal or command prompt in that folder.
4. Run:
   ```bash
   python crop_yield_monitoring.py
   ```
   On some systems use `python3 crop_yield_monitoring.py`.

## Menu
1. Add crop record
2. View all crop records
3. View summary
4. Exit

## Example data
- Crop name: Rice
- Farm/community location: Makeni
- Area planted: 2
- Total yield: 5

Expected yield per hectare: 2.50 tonnes.

## OOP and data structure features
- `CropRecord`: models one crop record.
- `CropYieldSystem`: manages multiple records.
- `records`: a list of `CropRecord` objects.
- Instance methods: `calculate_yield_per_hectare`, `display_record`, and system methods.
- Class method: `CropRecord.get_records_created`.
- Input validation rejects blank crop/location names, non-numeric values, and non-positive area/yield values.

## Digital Public Goods (DPG) alignment
- Open-source: source code can be shared and reviewed on GitHub.
- Inclusive and accessible: simple text menu and clear prompts.
- Privacy-respecting: the program does not ask for names, phone numbers, or other personal data.
- Modular and reusable: crop records and record management are separated into classes.

## Limitations
Data is held in memory and is lost when the program closes. A future version could add a database, export features, user roles, and more detailed reports.
