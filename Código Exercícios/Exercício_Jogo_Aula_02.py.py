from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Chrome()

navegador.get(url)

sleep(1)

p = navegador.find_element_by_id('ancora')

msg = ''
while 'Você ganhou'not in msg:
    p.click()
    sleep (0.3)
    msg = navegador.find_elements_by_tag_name ('p')[-1].text

navegador.quit()
