from selenium import webdriver
import time
import csv
import math
inicio=time.clock()

driver = webdriver.Firefox(executable_path='C:\Selenium\geckodriver.exe')
driver.maximize_window()
driver.get('https://www.linkedin.com/')
user_box = driver.find_element_by_id('login-email')
pass_box = driver.find_element_by_id('login-password')
user_box.send_keys('carlos.yepes@feriaexposolar.com')
pass_box.send_keys('#exposolar19*v3')
login_button = driver.find_element_by_id('login-submit')
login_button.click()

dataout=open("holaaaaaa.csv","a")

time.sleep(2)
num_pag = 1
contador = 0
name=[]
job=[]
url="https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22S%22%2C%22O%22%5D&keywords=epm&origin=FACETED_SEARCH"
while num_pag <=5:
    driver.get(url+'&page='+str(num_pag))


    cont=1
    while cont <=10:
        time.sleep(2)

        try:
            person_follow = driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']/li["+str(cont)+"]/div/div/div[3]/div/button")
            print(person_follow.text)
            name_person = driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']/li["+str(cont)+"]/div/div/div[2]/a/h3/span/span/span[1]").text
            print(name_person)
            link_person=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']/li["+str(cont)+"]/div/div/div[2]/a").get_attribute('href')
            print(link_person)
            if person_follow.text == "Conectar":
                                              
                try:
                    person_follow.click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//button[@class='button-secondary-large mr1']").click()
                    time.sleep(2)
                    message_box = driver.find_element_by_id('custom-message')
                    message_box.click()
                    message_box.send_keys('Únete a ExpoSolar Colombia, la red más importante de energía solar para Latinoamérica y el caribe. Ingresa a: https://feriaexposolar.com/')
                    time.sleep(2)
                    driver.find_element_by_xpath("//div[@class='send-invite__actions']/button[2]").click()
                    time.sleep(2)
    #                dataout.write(name_person+","+link_person)
        #            dataout.write("\n")
                except:
                    driver.find_element_by_xpath("//button[@class='send-invite__cancel-btn']").click()

            
        except:
            print("     ")
        driver.execute_script("window.scrollTo(0,"+str(cont*70)+")") 
        cont=cont+1  
    time.sleep(1)
    num_pag = num_pag + 1

fin=time.clock()
tiempo_ejecucion=math.fabs(inicio-fin)
#dataout.write("\n")
#dataout.write("tiempo de ejecucion: "+str(tiempo_ejecucion))
#dataout.write("\n")
#dataout.close()
driver.quit()
