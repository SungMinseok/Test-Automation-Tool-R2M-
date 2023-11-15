import os
from datetime import datetime

def extract_required_packages(pkg_file):
    try:
        with open(pkg_file, "r", encoding="utf-8") as file:
            return {line.split('==')[0].strip() for line in file if line.strip()}

    except Exception as e:
        print(f"Error extracting requirements from {pkg_file}: {e}")
        return set()

def create_pkg_required_for_execution(source_path, pkg_file, output_filename="pkg_required_for_execution"):
    try:
        required_packages = set()

        # Load the packages from the given pkg_file
        existing_packages = extract_required_packages(pkg_file)

        # Get the list of Python files in the specified directory
        python_files = [f for f in os.listdir(source_path) if f.endswith(".py")]

        # Extract required packages from import statements
        for python_file in python_files:
            file_path = os.path.join(source_path, python_file)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.strip().startswith("import ") or line.strip().startswith("from "):
                            tokens = line.split()
                            if len(tokens) >= 2:
                                package_name = tokens[1].split(".")[0]
                                if package_name in existing_packages:
                                    required_packages.add(package_name)
            except Exception as e:
                print(f"Error extracting requirements from {python_file}: {e}")

        # Load the versions from the given pkg_file
        versions = {}
        with open(pkg_file, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split('==')
                if len(parts) == 2:
                    package, version = parts
                    versions[package] = version

        # Write the required packages with versions to a new file with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_filename = f"{output_filename}_{timestamp}.txt"
        with open(output_filename, "w") as output_file:
            for req in sorted(required_packages):
                if req in versions:
                    output_file.write(f"{req}=={versions[req]}\n")
                else:
                    output_file.write(f"{req}\n")

        print(f"Required packages for execution with versions saved to {output_filename}")

    except Exception as e:
        print(f"Error creating pkg_required_for_execution file: {e}")

# Example: Extract required packages for execution based on pkg_231115.txt
create_pkg_required_for_execution(os.getcwd(), "pkg_231115.txt")
