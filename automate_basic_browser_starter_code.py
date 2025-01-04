
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep


url = "https://phptravels.com/demo/"

options = Options()
options.add_experimental_option("detach" , True)

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) , options=options)

# maximize browser window
driver.maximize_window()


# load the webpage 
driver.get(url)

# find the first name field 
first_name = driver.find_element(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/input')
# fill out the first name field
first_name.send_keys("Masab")

# find the last name field 
last_name = driver.find_element(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/input')
# find the last name field 
last_name.send_keys("Jatoi")

country_dropdown = driver.find_element(By.ID, "country_id")
select = Select(country_dropdown)

# Select Pakistan by visible text
select.select_by_visible_text("Pakistan +92")

# find the telephone field
telephone = driver.find_element(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/input')
# fill in the telephone field
telephone.send_keys("03176324765")

# find the email field
business = driver.find_element(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[3]/input')
# fill in the email field
business.send_keys("Kun btaon")

# find the email field 
email = driver.find_element(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[4]/input')
# fill in the email field 
email.send_keys("masabjatoi@gmail.com")



# Wrap the element with the Select class


# # find the password field
# password = driver.find_element(By.XPATH, '//*[@id="password"]')
# # fill in the password field
# password.send_keys("masab")




# # find the password confirm field
# password_confirm = driver.find_element(By.XPATH, 'FILL IN')
# # fill in the password confirm field
# password_confirm.send_keys("FILL IN")

# # find the desired response to the newsletter subscribe field
# newsletter_subscribe = driver.find_element(By.XPATH, 'FILL IN')
# # click on it
# newsletter_subscribe.click()

try:
    # Extract text from the element
    element = driver.find_element(By.XPATH,
                                  '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[5]/div[2]/div/div/h5/small')
    text = element.text.strip()


    # Evaluate the mathematical expression
    if "=" in text:
        expression = text.split("=")[0].strip()  # Extract part before "="
        result = eval(expression)  # Evaluate the mathematical expression
        # print("Calculated result:", result)

        # Locate the input field and enter the result
        next_field = driver.find_element(By.XPATH, '//*[@id="number"]')  # Update this XPath as needed
        next_field.send_keys(str(result))
    else:
        print("Text does not contain a valid expression.")

except Exception as e:
    print("Error processing the element:", e)

# # find the continue button
# submit = driver.find_element(By.XPATH, '')
# # click on the continue button
# submit.click()

submit = driver.find_element(By.XPATH, '//*[@id="demo"]')
driver.execute_script("arguments[0].scrollIntoView(true);", submit)
submit.click()


# # find the checkbox for agreeing to the terms
# agree = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[4]')
# # click on the agree checkbox
# agree.click()

# # Handling reCAPTCHA (adjust as needed, might need different approaches like solving captcha)
# try:
#     # Wait for reCAPTCHA to load, adjust timeout if necessary
#     driver.implicitly_wait(10)
#     recaptcha_checkbox = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div/div[8]')
#     recaptcha_checkbox.click()
#     sleep(5)  # Wait for captcha to complete (manual or automated solving if required)
# except Exception as e:
#     print("reCAPTCHA not found or already solved:", e)
#
# # scroll down by 200 units to view the lower part of the page
# driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()