"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os
directory='/Users/pamarthaluru/PYTHON-BASIC/practice/2_python_part_2/files'
values=[]
for filename in os.listdir(directory):
    filepath=os.path.join(directory,filename)
    if os.path.isfile(filepath):
        with open(filepath,'r') as file:
            content =file.read().strip()
            values.append(content)

result_content=', '.join(values)
with open("result.txt", 'w') as result_file:
    result_file.write(result_content)
