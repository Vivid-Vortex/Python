import re
from openpyxl import load_workbook


def get_sheet_data(file_path, sheet_name):
    workbook = load_workbook(filename=file_path, data_only=True)

    if sheet_name not in workbook.sheetnames:
        print(f"Sheet {sheet_name} not found in workbook.")
        return None

    sheet = workbook[sheet_name]
    sheet_data = []

    # Identify headers and index columns
    headers = [cell.value for cell in next(sheet.iter_rows(min_row=1, max_row=1))]
    index_columns = {i: headers[i] for i in range(len(headers)) if headers[i] and len(headers[i]) == 1 and headers[i].islower()}

    print(f"Headers: {headers}")
    print(f"Index columns: {index_columns}")

    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {headers[i]: row[i] for i in range(len(headers)) if headers[i]}

        # Replace placeholders in headers with actual values
        processed_row_data = {}
        for header, value in row_data.items():
            if header not in index_columns.values():
                new_header = header
                for col_idx, col_name in index_columns.items():
                    if col_name in row_data and row_data[col_name] is not None:
                        new_header = re.sub(rf'\[{col_name}\]', f'[{row_data[col_name]}]', new_header)
                processed_row_data[new_header] = value

        if processed_row_data:  # Ensure we only add non-empty dictionaries
            sheet_data.append(processed_row_data)

    return sheet_data

from PythonInit.GetRelativePathForProjectFiles import get_data_path
if __name__ == "__main__":
    file_path = get_data_path("test-data-v2.xlsx", "resources")
    sheet_name = 'req-payload2'
    data = get_sheet_data(file_path, sheet_name)
    print(data)
