from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Zoom link - force browser join
zoom_url = "https://us05web.zoom.us/wc/join/87021818655?pwd=MnABnZ7hiHHkIEa0mEC8IBRshD6Iwx.1&prefer=1"

options = Options()
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(zoom_url)

try:
    # Wait for the input box to appear
    name_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "input-for-name"))
    )
    name_input.clear()
    name_input.send_keys("ZoomBot")

    # Wait a tiny bit to let Zoom enable the button
    time.sleep(1)

    # Try to find and click the join button
    join_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.preview-join-button"))
    )
    join_button.click()

    print("Joined the meeting!")

except Exception as e:
    print("Error occurred:", e)

# Stay in the meeting for a bit
time.sleep(60)

driver.quit()

