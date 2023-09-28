"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import unittest
import datetime

class TestTaskClasses(unittest.TestCase):
    def test_homework_creation(self):
        homework=Homework('Learn functions',5)
        self.assertEqual(homework.text,'Learn functions')
        self.assertEqual(homework.days_to_complete,5)

    def test_homework_is_active(self):
        homework=Homework('Learn functions',5)
        self.assertTrue(homework.is_active())

        expired_homework=Homework('Expired Homework',0)
        self.assertFalse(expired_homework.is_active())


    def test_teacher_creation(self):
        teacher=Teacher('Dmitry','Orlyakov')
        self.assertEqual(teacher.first_name,'Dmitry')
        self.assertEqual(teacher.lastname,'Orlyakov')

    def test_student_creation(self):
        student=Student('Vladislav','Popov')

        oop_homework=Homework('Create 2 simple classes',5)
        expired_homework=Homework('Expired Homework',0)

        result1=student.do_homework(oop_homework)
        result2=student.do_homeork(expired_homework)

        self.assertEqual(result1,oop_homework)
        self.assertIsNone(result2)

if __name__=="__main__":
    unittest.main()

