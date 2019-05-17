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

#dataout=open("quartafeira.csv","a")
dataout=open("C:\Users\Exposolar20180\Desktop\probandolinkedin\miercoles.txt","w")

time.sleep(2)
num_pag = 40
contador = 0
name=[]
job=[]
url="https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&keywords=codensa&origin=FACETED_SEARCH"
while num_pag <=40:
    driver.get(url+'&page='+str(num_pag))


    cont=1
    while cont <=10:
        time.sleep(1)
       
        try:
            person_follow = driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none ']/li["+str(cont)+"]/div/div/div[3]/div/div/button")
            print(person_follow.text)
            name_person = driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none ']/li["+str(cont)+"]/div/div/div[2]/a/h3/span/span/span[1]").text    
            print(name_person)                                                                                                   
            link_person=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none ']/li["+str(cont)+"]/div/div/div[2]/a").get_attribute('href')
            print(link_person)
            if person_follow.text == "Enviar mensaje":
                driver.get(link_person)
                time.sleep(1)
                try:                                    
                    info= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[1]/h2").text
                    print(info)
                except:
                    info='    '
                try:                                   
                    job= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[2]/button[1]/span/span[1]").text
                    print(job)
                except:
                    job='    '
                try:                                    
                    city= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[1]/h3").text
                    print(city)
                except:
                    city='    '
                        
                driver.get(link_person+"detail/contact-info/")
                time.sleep(1)
                try:
                    email = driver.find_element_by_class_name('ci-email').text[19:]
                    print(email)
                except:
                    email = "    "
                try:
                    phone = driver.find_element_by_class_name('ci-phone').text[19:]
                    print(phone)
                except:
                    phone = "    "
                try:    
                    dataout.write(name_person+","+email+","+phone+","+job+","+info+","+city)
                    dataout.write("\n")
                except:
                    print ("No escribio!")
                time.sleep(1)
                driver.get(url+'&page='+str(num_pag))
                time.sleep(1)
                

            
        except:
            print("     ")
        driver.execute_script("window.scrollTo(0,"+str(cont*70)+")")

        cont=cont+1  
    time.sleep(1)
    num_pag = num_pag + 1

fin=time.clock()
tiempo_ejecucion=math.fabs(inicio-fin)
dataout.write("\n")
#dataout.write("tiempo de ejecucion: "+str(tiempo_ejecucion))

dataout.close()
driver.quit()
