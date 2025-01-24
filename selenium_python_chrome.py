# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)
# pip3 install faker (Устанавливаем библиотеку faker)
import glob
import os
# импортируем необходимые библиотеки и элементы
import time
# from datetime import datetime, timedelta
# from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
download_path = 'C:\\Users\\the_r\\PycharmProjects\\Selenium2_15\\Downloaded file\\'
prefs = {'download.default_directory' : download_path}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.maximize_window()

# создаем переменную для кнопки загрузки файла с сайта и взаимодействуем с ней
download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
download_button.click()
time.sleep(3)

# создаем переменные для взаимодействия со скачанным файлом и проводим проверки
file_path = download_path + 'LambdaTest.pdf'
print(file_path)
assert os.access(file_path, os.F_OK) == True, 'Файла нет в папке'
print('Файл в папке')

files = glob.glob(os.path.join(download_path, '*.*'))
for file in files:
    size = os.path.getsize(file)
    if size > 10:
        print('Файл не пуст')
    else:
        print('Файл пуст')
    os.remove(file)

# после задержки в 10 секунд закрываем браузер
time.sleep(10)
driver.quit()