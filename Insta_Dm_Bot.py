# importing module
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import chromedriver_binary

driver = webdriver.Chrome()

# enter receiver user name
with open('usernames.txt', 'r') as f:
    user = [line.strip() for line in f]
print(user)

# with open('messages.txt', 'r', encoding="utf-8") as f:
# 	message_ = (f.readlines())
# print(message_)
message_ = ('Hii,\n I sell followers, likes, and more  \n • Instagram \n£10 for 1k followers \n£80 for 10k followers \n£5 for 1k likes \n\n• TikTok\n£15 for 1k followers \n£130 for 10k followers \n£10 1k likes \n\n•Facebook page\n£15 for 1k followers \n£130 for 10k followers \n£10 for 1k likes \n\nJust need your username and I’ll send a free sample Before any sort or payment!\n\nI also make websites and mobile apps for any business \n\nMy page is: @boradigital.co.uk')

username = ""
password = ""


class bot:
	def __init__(self, username, password, user, message):
		self.username = 'Paige.bora'
		self.password = 'Alibora7861'
		self.user = user
		self.message = message
		self.base_url = 'https://www.instagram.com/'
		self.bot = driver
		self.login()

	def login(self):
		self.bot.get(self.base_url)
		time.sleep(10)

		enter_username = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.XPATH,'//*[@name="username"]')))
		enter_username.send_keys(self.username)
		enter_password = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.XPATH, '//*[@name="password"]'))) #'//*[@type="submit"]'
		enter_password.send_keys(self.password)
		enter_password.send_keys(Keys.RETURN)
		time.sleep(15)

		# first pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
		time.sleep(15)

		# 2nd pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		time.sleep(15)

		# direct button
		self.bot.find_element(By.XPATH,
							'//*[@aria-label="Direct"]').click()
		time.sleep(15)

		for i in user:

			# clicks on pencil icon
			self.bot.find_element(By.XPATH,
							'//*[@aria-label="New message"]').click()
			time.sleep(8)

			# enter the username
			self.bot.find_element(By.XPATH,
								'//*[@type="text"]').send_keys(i)
			time.sleep(10)

			# click on the username
			self.bot.find_element(By.CSS_SELECTOR,
								'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j.xh8yej3 > div > div.xjp7ctv > div > div > div:nth-child(1)').click()
			time.sleep(8)

			# next button
			self.bot.find_element(By.CSS_SELECTOR,
								'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j.xh8yej3 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xw7yly9.xktsk01.x1yztbdb.x1d52u69.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div').click()
			time.sleep(8)

			# click on message area
			send = self.bot.find_element(By.XPATH,
										'//*[@aria-label="Message"]')

			# types message
			send.send_keys(self.message)
			time.sleep(10)

			# send message
			send.send_keys(Keys.RETURN)
			time.sleep(8)
			print(f'Massage sent to {i}.')

		self.bot.quit()


def init():
	bot('username', 'password', user, message_)

	# when our program ends it will show "done".
	print('Massages sent to all list.')
	input("DONE")


# calling the function
init()

