import re
import glob
import os
from collections import Counter

folder_path = ''
files = glob.glob(os.path.join(folder_path, '**/*.vue'), recursive=True)


def count_vue_components(vue_code):
    # pattern = r'(<[a-z]+-[a-z]+-[a-z]+>) | (<[a-z]+-[a-z]+>) | (<[a-z]+-[a-z]+-[a-z]+) | (<[a-z]+-[a-z]+)'
    pattern = r'<([a-z]-\w+(-\w+)*)>'
    component_names = re.findall(pattern, vue_code)

    return Counter(component_names)


for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as file:
        vue_code = file.read()
    for tag, count in count_vue_components(vue_code).items():
        print(f"{tag}: {count}次")
