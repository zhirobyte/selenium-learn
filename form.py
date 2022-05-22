#this is the line for import the dependency

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as execute


#mulai aja dari sini masukin form nya

namaStr = 'muchsin'
alamatStr = 'anjay@gmail.com'
subjekStr = 'subjekanda ada disini'
pesan = 'selamat driver bot anda berhasil'

#ini untuk drivernya biar bisa execute
browser = webdriver.Edge()
browser.get(('https://printing.sublimaxdigital.com/hubungi-kami/'))



#ini untuk isi otomatis formnya 
# fill in username and hit the next button


#nama
nama = browser.find_element_by_id('forminator-field-name-1')
nama.send_keys(namaStr)

#alamat
alamat = browser.find_element_by_id('forminator-field-email-1')
alamat.send_keys(alamatStr)

#subjek
subjek = browser.find_element_by_id('forminator-field-text-1')
subjek.send_keys(subjekStr)

#pesan
pesan = browser.find_element_by_id('forminator-field-textarea-1')
pesan.send_keys(pesanStr)

nextButton = browser.find_element_by_id('forminator-button forminator-button-submit')
nextButton.click()