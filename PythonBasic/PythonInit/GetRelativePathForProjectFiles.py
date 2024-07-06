from pathlib import Path


def get_data_path(filename, resources_folder="resources"):
    """
  Gets the relative path to a data file within the project, given a resources folder name.

  Args:
      filename (str): The name of the data file (e.g., "test-data.xlsx").
      resources_folder (str, optional): The name of the folder containing data files. Defaults to "resources".

  Returns:
      pathlib.Path: The path to the data file.

  Raises:
      ValueError: If the filename is empty or not a string.
  """

    if not filename or not isinstance(filename, str):
        raise ValueError("Filename must be a non-empty string.")

    # Get the path to the current Python file
    script_path = Path(__file__)

    # Create a Path object for the data file with relative path
    data_path = script_path.parent / resources_folder / filename

    return data_path


# data_file_to_access = "test-data.xlsx"
# relative_path_from_current_file = "resources"
# other_data_path = get_data_path(data_file_to_access, relative_path_from_current_file)
# print(other_data_path)
