from selenium import webdriver
import time
import random

#Make sure you choromium installed with geckodriver
#This program will purchase ANY item on a page it is navigated to. So if you for example navigate to a bottle of soap and your local target has them item the script will purchase that item. 
#Please keep that in mind I am not responsible for your own mistakes.

browser = webdriver.Chrome()

browser.get('https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab')

i = 0
instock = False
#time gap in place so you can sign into your account
time.sleep(30)
while(instock == False):
	time.sleep(random.randint(10,15))
	if(len(browser.find_elements_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/button')) > 0):
		instock = True
		browser.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/button').click()
		time.sleep(3)

		if(len(browser.find_elements_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div/div[2]/div[2]/button')) > 0):
			browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div/div[2]/div[2]/button').click()
			time.sleep(3)
			browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div[2]/div[3]/button').click()
			time.sleep(3)
			browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/button').click()
			time.sleep(4)
			if(len(browser.find_elements_by_xpath('//*[@id="creditCardInput-cvv"]')) > 0):			
				browser.find_element_by_xpath('//*[@id="creditCardInput-cvv"]').send_keys('555')
				browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
			else:			
				browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
		else:
			time.sleep(3)
			browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div[2]/div[3]/button').click()
			time.sleep(3)
			browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/button').click()
			time.sleep(4)
			if(len(browser.find_elements_by_xpath('//*[@id="creditCardInput-cvv"]')) > 0):			
				#replace all of the below lines of code with your own CCV					
				browser.find_element_by_xpath('//*[@id="creditCardInput-cvv"]').send_keys('555')
				browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
			else:			
				browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
	else:
				
		if(len(browser.find_elements_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button')) > 0):
			browser.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button').click()			
			time.sleep(3)			
			print('Now you can go where people are one')			
			if(len(browser.find_elements_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div/div[2]/div[2]/button')) > 0):
				print('Now you can go where they get things done')				
				browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div/div[2]/div[2]/button').click()
				time.sleep(4)
				browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div[3]/div[3]/button').click()
				time.sleep(3)
				browser.find_element_by_xpath('//*[@id="viewport"]/div[5]/div[2]/div[1]/div[2]/div[9]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/fieldset/div/div[1]/label/div').click()
				time.sleep(2)			
				browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/button').click()		
				time.sleep(3)				
				if(len(browser.find_elements_by_xpath('//*[@id="creditCardInput-cvv"]')) > 0):			
					browser.find_element_by_xpath('//*[@id="creditCardInput-cvv"]').send_keys('555')
					browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
					print('Über Alles Califorina')	
				else:			
					browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
					print('California Über Alles')							
		else:		
						
			if(len(browser.find_elements_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div/div[2]/div[2]/button')) > 0):
				print('Lets ride, ride how we ride')				
				browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div/div[2]/div[2]/button').click()
				time.sleep(4)
				browser.find_element_by_xpath('/html/body/div[17]/div/div/div/div/div/div/div[3]/div[3]/button').click()
				time.sleep(3)
				browser.find_element_by_xpath('//*[@id="viewport"]/div[5]/div[2]/div[1]/div[2]/div[9]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/fieldset/div/div[1]/label/div').click()
				time.sleep(2)			
				browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/button').click()		
				time.sleep(3)				
				if(len(browser.find_elements_by_xpath('//*[@id="creditCardInput-cvv"]')) > 0):			
					browser.find_element_by_xpath('//*[@id="creditCardInput-cvv"]').send_keys('555')
					browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
					print('Dispatch calls are you doin something wicked')	
				else:			
					browser.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/div/button').click()
					print('No siree, Jack, we re just givin tickets!')			
		i = i + 1
		print('\n' + str(i))
		browser.refresh()


		



