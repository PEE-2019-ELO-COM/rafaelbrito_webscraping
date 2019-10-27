#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from selenium import webdriver
import time
from IATAcodes import codes

def set_text(text):
    log.delete(0,END)
    log.insert(0,text)
    return



def getIATA(name, valores):    
    res = list(filter(lambda el: el['name'] == name, valores))
    return res[0]['IATA']


def get_info():
    global citysaida, citydestino, datasaida, dataida, useremail
    citysaida = cityexit.get()
    citydestino = citygo.get()
    datasaida = dataexit.get()
    dataida = datago.get()
    useremail = email.get()



def rodando():
    master.update()
    lista_opcoes = []
    bestop = lista_opcoes
    bestop1 = []
    bestprice = 100000
    while(True):   
        try:
            driver = webdriver.Firefox(executable_path=r'C:\Users\binks\Desktop\afins\geckodriver.exe')

            url = 'https://www.decolar.com/shop/flights/search/roundtrip/{}/{}/{}/{}/1/0/0/NA/NA/NA/NA/NA/?from=SB&di=1-0'.format(getIATA(citysaida, codes),getIATA(citydestino, codes),datasaida,dataida)
            driver.get(url)

            time.sleep(8)

            for i in range(1,10):
                op = {}
                try:    
                    op["preco"] = int(driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[2]/fare/span/span/fare-details-items/div/item-fare/p/span/flights-price/span/flights-price-element/span/span/em/span[2]""".format(i)).text.replace('.', ''))
                    op["comapanhia_ida"] = driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[1]/div/span/div/div/span[1]/route-choice/ul/li/route/itinerary/div/div/div[1]/itinerary-element[2]/span/itinerary-element-airline/span/span/span/span[2]/span""".format(i)).text
                    op["saida_ida"] = driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[1]/div/span/div/div/span[1]/route-choice/ul/li[1]/route/itinerary/div/div/div[2]/itinerary-element[1]/span/span/span""".format(i)).text
                    op["chegada_ida"] = driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[1]/div/span/div/div/span[1]/route-choice/ul/li[1]/route/itinerary/div/div/div[3]/itinerary-element[1]/span/span/span/span""".format(i)).text
                    op["companhia_volta"] = driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[1]/div/span/div/div/span[2]/route-choice/ul/li/route/itinerary/div/div/div[1]/itinerary-element[2]/span/itinerary-element-airline/span/span/span/span[2]/span""".format(i)).text
                    op["saida_volta"] = driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[1]/div/span/div/div/span[2]/route-choice/ul/li[1]/route/itinerary/div/div/div[2]/itinerary-element[1]/span/span/span""".format(i)).text
                    op["chegada_volta"] = driver.find_element_by_xpath("""/html/body/div[10]/div/div/div/div[3]/div/div[2]/div/div[5]/app-root/app-common/items/div/span[{}]/span/cluster/div/div/div[1]/div/span/div/div/span[2]/route-choice/ul/li[1]/route/itinerary/div/div/div[3]/itinerary-element[1]/span/span/span/span""".format(i)).text

                    lista_opcoes.append(op)

                except:
                    break

            driver.close()


            #pega melhor opcao do site
            for i in range(0,len(lista_opcoes)):
                if bestprice > lista_opcoes[i]['preco']:
                    bestprice = lista_opcoes[i]['preco']
                    index = i

            #mostra melhor opcao
            bestop = lista_opcoes[index]
            
            print("A melhor opcao atual tem preço " + str(bestop["preco"]) + " reais, na ida pela " + str(bestop["comapanhia_ida"]) + " com horários de chegada e partida respectivamente " + str(bestop["chegada_ida"]) + " e " + str(bestop["saida_ida"]) + ". A volta é pela " + str(bestop["companhia_volta"]) + " com horarios de chegada e saida " + str(bestop["chegada_volta"]) + " e " + str(bestop["saida_volta"]))

            #alertas
            if bestop != bestop1:
                print('\a')
                # create message object instance
                msg = MIMEMultipart()


                message = str("A melhor opcao atual tem preço " + str(bestop["preco"]) + " reais, na ida pela " + str(bestop["comapanhia_ida"]) + " com horários de chegada e partida respectivamente " + str(bestop["chegada_ida"]) + " e " + str(bestop["saida_ida"]) + ". A volta é pela " + str(bestop["companhia_volta"]) + " com horarios de chegada e saida " + str(bestop["chegada_volta"]) + " e " + str(bestop["saida_volta"]) + "./n")

                # setup the parameters of the message
                password = "passagem112358"
                msg['From'] = "passagem.melhor@gmail.com"
                msg['To'] = str(useremail)
                msg['Subject'] = "Hey, tem passagem melhor!"

                # add in the message body
                msg.attach(MIMEText(message, 'plain'))

                #create server
                server = smtplib.SMTP('smtp.gmail.com: 587')

                server.starttls()

                # Login Credentials for sending the mail
                server.login(msg['From'], password)


                # send the message via the server.
                server.sendmail(msg['From'], msg['To'], msg.as_string())

                server.quit()

                print ("E-mail enviado com sucesso para %s" % (msg['To']))

                bestop1 = bestop

            time.sleep(15)
            
        
        except:
            driver.close()
            continue



master = tk.Tk()
tk.Label(master, text="Cidade de saída").grid(row=0)
tk.Label(master, text="Cidade de destino").grid(row=1)
tk.Label(master, text="Data de ida (ex: 2019-12-31)").grid(row=2)
tk.Label(master, text="Data de volta").grid(row=3)
tk.Label(master, text="Email").grid(row=4)



cityexit = tk.Entry(master)
citygo = tk.Entry(master)
dataexit = tk.Entry(master)
datago = tk.Entry(master)
email = tk.Entry(master)


cityexit.grid(row=0, column=1)
citygo.grid(row=1, column=1)
dataexit.grid(row=2, column=1)
datago.grid(row=3, column=1)
email.grid(row=4, column=1)






tk.Button(master, text='Enviar Infos', command=get_info).grid(row=6, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='RUN', command=rodando).grid(row=6, column=1, sticky=tk.W, pady=4)


tk.mainloop()


# In[ ]:





# In[ ]:




