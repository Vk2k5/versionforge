# report_generator.py

def generate_report(data, output_file="report.txt"):
    """
    Generates a simple text report from the given data and writes it to a file.

    Args:
        data (list of dicts): A list of dictionaries, where each dictionary
                               represents a record to be included in the report.
                               It's assumed each dictionary has the same keys
                               which will be used as column headers.
        output_file (str, optional): The name of the file to write the report to.
                                     Defaults to "report.txt".
    """
    if not data:
        print("No data to generate report.")
        return

    keys = data[0].keys()
    header = "| " + " | ".join(keys) + " |"
    separator = "-" * len(header)

    with open(output_file, "w") as f:
        f.write(header + "\n")
        f.write(separator + "\n")
        for item in data:
            row_values = [str(item.get(key, "")) for key in keys]
            row = "| " + " | ".join(row_values) + " |"
            f.write(row + "\n")

    print(f"Report generated and saved to '{output_file}'")

if __name__ == "__main__":
    # Example usage:
    report_data = [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    ]
    generate_report(report_data, "student_report.txt")

    # Another example with different data:
    feedback_data = [
        {"Student": "StudentA", "Comment": "Very helpful."},
        {"Student": "StudentB", "Comment": "Could be clearer."},
        {"Student": "StudentA", "Comment": "Excellent content."},
    ]
    generate_report(feedback_data, "feedback_report.txt")
