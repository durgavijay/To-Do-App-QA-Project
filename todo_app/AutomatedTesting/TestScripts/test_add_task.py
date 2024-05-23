import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ToDoAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def test_add_task(self):
        driver = self.driver
        input_field = driver.find_element(By.NAME, "task")
        input_field.send_keys("Test Task")
        input_field.send_keys(Keys.RETURN)
        time.sleep(10)
        tasks = driver.find_elements(By.TAG_NAME, "li")
        task_texts = [task.text for task in tasks]
        print("Tasks:", task_texts)
        self.assertIn("Test Task", task_texts)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
