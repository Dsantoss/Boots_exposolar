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

dataout=open("Ingenieros_civiles_bogota4.csv","a")

time.sleep(2)
num_pag = 4
contador =0
name=[]
job=[]
url="https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22co%3A9549%22%5D&facetNetwork=%5B%22F%22%5D&keywords=civil&origin=FACETED_SEARCH"
while num_pag <=4:
    driver.get(url+'&page='+str(num_pag))


    cont=1
    while cont <=10:
        time.sleep(1)

        try:
            person_follow = driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']/li["+str(cont)+"]/div/div/div[3]/div/div/button")
            print(person_follow.text)
            name_person = driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']/li["+str(cont)+"]/div/div/div[2]/a/h3/span/span/span[1]").text    
            print(name_person)                                                                                                   
            link_person=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']/li["+str(cont)+"]/div/div/div[2]/a").get_attribute('href')
            print(link_person)
            if person_follow.text == "Enviar mensaje":
                                              
                try:
                    person_follow.click()
                    time.sleep(1)
                    message_box = driver.find_element_by_xpath("//div[@class='msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1'][@role='textbox']")
                    message_box.send_keys("¿Es usted ingeniero o técnico Electricista, Electrónico, mecánico, mecatrónico, civil, industrial, ¿entre otros? \n ¡Este Curso de 40 Horas denominado “Prácticas eficientes y seguras para el diseño e instalación de sistemas fotovoltaicos” te interesa! \n Este es el primer curso diseñado y concertado con el sector empresarial, teniendo en cuenta sus necesidades y expectativas, donde se desarrollan competencias para un desempeño efectivo en los participantes. \n Curso con metodología 100% practica, para diseñar, dimensionar e implementar 3 tipos de sistemas On-Grid, Off Grid e Hibrido. \n Bogota del 6 al 10 de mayo \n Mayor información: \n 3007908554 \n https://feriaexposolar.com/curso-practicas-eficientes-y-seguras/")
                    time.sleep(1)
                    driver.find_element_by_xpath("//button[@class='msg-form__send-button artdeco-button artdeco-button--1'][@type='submit']").click()
                    time.sleep(1)
                    cerrar = driver.find_element_by_xpath("//button[@class='msg-overlay-bubble-header__control js-msg-close']").click()
                    time.sleep(1)
                    
                    driver.get(link_person)
                    time.sleep(1)
                    try:
                                              
                        info= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[1]/h2").text
                        print(info)
                    except:
                       
                        info= driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[1]/h2").text
                        print(info)
                    try:
                        print("entro2")                    
                        job= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[2]/button[1]/span/span[1]").text
                        print(job)
                    except:
                        print("entro3")
                        job=driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[2]/button[1]/span/span[1]").text
                        print(job)
                    try:                                    
                        city= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[1]/h3").text
                        print(city)
                    except:
                        city= driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div/div/div/div/div/div[1]/div[2]/section/div[3]/div[1]/h3").text
                        print(city)
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
                    
                    dataout.write(name_person+","+link_person+","+email+","+phone+","+job+","+info+","+city)
                    dataout.write("\n")
                    time.sleep(1)
                    driver.get(url+'&page='+str(num_pag))
                    time.sleep(1)
                except:
                    print("noooooooooo entro")
                    ll=0

            
        except:
            print("  ")
        driver.execute_script("window.scrollTo(0,"+str(cont*70)+")")
     #   driver.delete_all_cookies()
        cont=cont+1  
    time.sleep(1)
    num_pag = num_pag + 1

fin=time.clock()
tiempo_ejecucion=math.fabs(inicio-fin)
dataout.write("\n")
dataout.write("tiempo de ejecucion: "+str(tiempo_ejecucion))
dataout.write("\n")
dataout.close()
driver.quit()
