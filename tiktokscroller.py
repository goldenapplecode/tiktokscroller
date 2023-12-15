from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

#Makes the browser think you are using an actual computer instead of an automated bot
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get("https://www.tiktok.com/")

#User has to log in manually to avoid captcha detection
print("You have 30 seconds to log in, and return to the for-you page.")
time.sleep(30)

radical_hashtags =["#liberaltears", "#liberalsoftiktok", "#antiwoke", "#wokism", "#indentifyas", "#gender", "#triggeredliberal", "#wakkerworden", "#left", "#wokestupidity", "#antileft", "#indoctrination"]

videos_to_watch = 100
count = 0
radical_videos = 0
while count <= videos_to_watch:
    
    #Finds the text box for the video
    text_box = driver.find_element(By.XPATH, f'//*[@id="main-content-homepage_hot"]/div[1]/div[{count+1}]/div/div[1]/div[2]/div/div[2]').text
    
    #Determines if the text box contains chosen substrings
    if radical_hashtags[0] in text_box or radical_hashtags[1] in text_box or radical_hashtags[2] in text_box or radical_hashtags[3] in text_box or radical_hashtags[4] in text_box or radical_hashtags[5] in text_box or radical_hashtags[6] in text_box or radical_hashtags[7] in text_box or radical_hashtags[8] in text_box or radical_hashtags[9] in text_box or radical_hashtags[10] in text_box or radical_hashtags[11] in text_box:
        time.sleep(1)
        print("Radical hashtags found")

        like_btn = driver.find_element(By.XPATH, f'//*[@id="main-content-homepage_hot"]/div[1]/div[{count+1}]/div/div[2]/div[2]/button[1]')
        like_btn.click()

        time.sleep(9)
        radical_videos += 1
        print(f"Radical Videos: {radical_videos}")
    else:
        print("No radical hashtags found")
        time.sleep(5)
    
    #Scrolls down 1 video
    video_down = ActionChains(driver).send_keys(Keys.DOWN)
    video_down.perform()
    count += 1

time.sleep(1)
driver.quit()