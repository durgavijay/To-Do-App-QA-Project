import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestDeleteTask(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:5000")

    def test_delete_task(self):
        driver = self.driver

        # Add a new task first
        input_field = driver.find_element(By.NAME, "task")
        input_field.send_keys("Test Task")
        input_field.send_keys(Keys.RETURN)

        # Check if the task was added
        task_list = driver.find_elements(By.XPATH, "//ul/li")
        self.assertEqual(len(task_list), 1)
        self.assertIn("Test Task", task_list[0].text)

        # Delete the task
        delete_link = driver.find_element(By.XPATH, "//ul/li/a[text()='Delete']")
        delete_link.click()

        # Check if the task was deleted
        task_list = driver.find_elements(By.XPATH, "//ul/li")
        self.assertEqual(len(task_list), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
