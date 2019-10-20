
from selenium import webdriver
import time
from IATAcodes import codes

def getIATA(name, valores):    
    res = list(filter(lambda el: el['name'] == name, valores))
    return res[0]['IATA']



print("Cidade de saída:")
cityexit = input()

print("Cidade de destino:")
citygo = input()

print("Data de ida:")
dataexit = input()

print("Data de volta:")
datago = input()

lista_opcoes = []
bestop = lista_opcoes
bestprice = 100000

while(True):   
    
    driver = webdriver.Firefox(executable_path=r'C:\Users\binks\Programas\rafaelbrito_webscraping-master\geckodriver.exe')
    
    url = 'https://www.decolar.com/shop/flights/search/roundtrip/{}/{}/{}/{}/1/0/0/NA/NA/NA/NA/NA/?from=SB&di=1-0'.format(getIATA(cityexit, codes),getIATA(citygo, codes),dataexit,datago)
    
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
    print("A melhor opcao atual é:" + str(bestop))
    time.sleep(15)
