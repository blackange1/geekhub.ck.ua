from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC


path_main = Path(__file__).parent.parent


class SubmitForm(object):
    path_driver = str(path_main.joinpath('driver').joinpath('chromedriver'))
    path_screenshots = path_main.joinpath('screenshots')
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link'
    delay = 1

    def __init__(self, id_user, username):
        self.id_user = id_user
        self.username = username

    def submit(self):
        driver = Chrome(SubmitForm.path_driver)
        driver.get(SubmitForm.url)
        sleep(SubmitForm.delay)
        try:
            input_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "quantumWizTextinputPaperinputInput"))
            )
            input_name.send_keys(self.username)
            driver.save_screenshot(str(SubmitForm.path_screenshots.joinpath(f'{self.id_user}_completed_form.png')))

            submit = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "appsMaterialWizButtonPaperbuttonContent"))
            )
            submit.click()
            driver.save_screenshot(str(SubmitForm.path_screenshots.joinpath(f'{self.id_user}_submitted_form.png')))
        finally:
            sleep(SubmitForm.delay)
            driver.quit()

    def __str__(self):
        return 'class SubmitForm'
