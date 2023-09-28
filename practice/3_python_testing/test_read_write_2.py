"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import unittest
import os

class TestReadWriteTask(unittest.Testcase):
    def test_file_writing_and_reading(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            words=generate_words()

            utf8_content='\n'.join(words)
            cp1252_content=', '.join(reversed(words))

            write_file(os.path.join(temp_dir,'file1.txt'),utf8_content,'utf_content')
            write_file(os.path.join(temp_dir,'file2.txt'),cp1252_content,'cp1252_content')


            with open(os.path.join(temp_dir,'file1.txt'),'r',encoding='utf-8') as file1:
                file1_content=file1.read()

            with open(os.path.join(temp_dir,'file2.txt'),'r',encoding='cp1252') as file2:
                file2_content=file2.read()

            self.assertEqual(file1_content,utf8_content)
            self.assertEqual(file2_content,cp1252_content)

if __name__ == "__main__":
    unittest.main()
    
            
