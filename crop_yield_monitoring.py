"""
Crop Yield Monitoring System
PROG211 - Object-Oriented Programming 1

A small command-line application for recording and viewing crop yield data.
It uses OOP, a list data structure, instance methods, and a class method.
No sensitive personal information is collected.
"""

class CropRecord:
    """Represents one crop yield record."""

    records_created = 0  # Class attribute shared by all CropRecord objects

    def __init__(self, crop_name, farm_location, area_hectares, yield_tonnes):
        self.crop_name = crop_name
        self.farm_location = farm_location
        self.area_hectares = area_hectares
        self.yield_tonnes = yield_tonnes
        CropRecord.records_created += 1

    def calculate_yield_per_hectare(self):
        """Instance method: calculate tonnes produced per hectare."""
        if self.area_hectares <= 0:
            return 0
        return self.yield_tonnes / self.area_hectares

    def display_record(self):
        """Instance method: display the record in a readable format."""
        print(f"Crop: {self.crop_name}")
        print(f"Farm location: {self.farm_location}")
        print(f"Area planted: {self.area_hectares:.2f} hectares")
        print(f"Total yield: {self.yield_tonnes:.2f} tonnes")
        print(f"Yield per hectare: {self.calculate_yield_per_hectare():.2f} tonnes")
        print("-" * 40)

    @classmethod
    def get_records_created(cls):
        """Class method: return the number of CropRecord objects created."""
        return cls.records_created


class CropYieldSystem:
    """Stores and manages multiple crop records."""

    def __init__(self):
        self.records = []  # List data structure stores CropRecord objects

    def add_record(self, record):
        """Add a CropRecord object to the list."""
        self.records.append(record)
        print("Crop record added successfully.")

    def display_all_records(self):
        """Display every record stored in the list."""
        if not self.records:
            print("No crop records have been added yet.")
            return

        print("\n===== CROP YIELD RECORDS =====")
        for number, record in enumerate(self.records, start=1):
            print(f"Record {number}")
            record.display_record()

    def show_summary(self):
        """Display simple statistics about the stored records."""
        if not self.records:
            print("No data available for a summary.")
            return

        total_yield = sum(record.yield_tonnes for record in self.records)
        total_area = sum(record.area_hectares for record in self.records)
        print("\n===== SUMMARY =====")
        print(f"Number of crop records: {len(self.records)}")
        print(f"Combined area: {total_area:.2f} hectares")
        print(f"Combined yield: {total_yield:.2f} tonnes")
        print(f"CropRecord objects created: {CropRecord.get_records_created()}")


def get_positive_float(prompt):
    """Read a positive number and keep asking if the input is invalid."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number, for example 2.5.")


def main():
    system = CropYieldSystem()

    while True:
        print("\n=== CROP YIELD MONITORING SYSTEM ===")
        print("1. Add crop record")
        print("2. View all crop records")
        print("3. View summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            crop_name = input("Enter crop name: ").strip()
            farm_location = input("Enter farm/community location: ").strip()

            if not crop_name or not farm_location:
                print("Crop name and location cannot be empty.")
                continue

            area = get_positive_float("Enter area planted in hectares: ")
            yield_tonnes = get_positive_float("Enter total yield in tonnes: ")

            record = CropRecord(crop_name, farm_location, area, yield_tonnes)
            system.add_record(record)

        elif choice == "2":
            system.display_all_records()

        elif choice == "3":
            system.show_summary()

        elif choice == "4":
            print("Thank you for using the Crop Yield Monitoring System.")
            break

        else:
            print("Invalid choice. Select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
