"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""


import unittest
import os
import tempfile


class TestReadWriteTask(unittest.TestCase):

    def test_read_write_task(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file1_content="File 1 content"
            file2_content="File 2 content"

            file1_path=os.path.join(temp_dir,"file1.txt")
            file2_path=os.path.join(temp_dir,"file2.txt")

            with open(file1_path,'w') as file1:
                file1.write(file1_content)

            with open(file2_path,'w') as file2:
                file2.write(file2_content)

            result_file_path=os.path.join(temp_dir,"result.txt")
            self.assertTrue(os.path.isfile(result_file_path))

            with open(result_file_path,'r') as result_file:
                result_content=result_file.read().strip()


            expected_result_content=f"{file1_content},{file2_content}"
            self.assertEqual(result_content,expected_result_content)
    

if __name__ == '__main__':
    unittest.main()