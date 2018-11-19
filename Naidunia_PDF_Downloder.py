from telegram.error import NetworkError, Unauthorized
import telegram
import datetime
import time
import requests
import PyPDF2
import subprocess
import os

def a():
	merger = PyPDF2.PdfFileMerger()
	today = datetime.datetime.now()
	yesterday = today - datetime.timedelta(days = 1)
	page = 0
	dirr = os.getcwd()

	try:
	    os.mkdir(f'{dirr}/temp')
	except:
		print('Cant create temporary dirctory')
		exit()

	while True:
		page += 1
		print(f'Downloading page - {page}')
		ngr = yesterday.strftime('%d')
		dayy = today.strftime('%d%m%Y')
		url = f'https://naiduniaepaper.jagran.com/epaperimages/{dayy}/indore/{ngr}ngr-pg{page}-0.pdf'
		path = f'{dirr}/temp/{page}.pdf'

		try:
			r = requests.get(url, stream=True)
			if r.status_code == 404:
				url = f'https://naiduniaepaper.jagran.com/epaperimages/{dayy}/indore/{ngr}rtm-pg{page}-0.pdf'
				r = requests.get(url, stream=True)
				if r.status_code == 404:
					raise Exception("That's the end")

			with open(path, 'ab') as fd:
				for chunk in r.iter_content(1000):
					fd.write(chunk)
			merger.append(PyPDF2.PdfFileReader(path, 'rb'))
		except BaseException as e:
			print(e)
			print(f'Total {page} pages')
			break

	print('Merging PDF')
	final_file = today.strftime('%d%m%Y')+'_Naidunia.pdf'
	merger.write(final_file)


	# Telegram Code
	print('Uploading in Telegram')
	token = 'private_token_string'
	cid = 0	#channel id
	bot = telegram.Bot(token)
	bot.send_document(chat_id=cid, document=open(final_file, 'rb'), timeout=2000)
	subprocess.Popen(['rm', '-rf', f'{dirr}/temp'])
	subprocess.Popen(['rm', '-rf', final_file])

	print('Done... Join t.me/NaiDunia')

while True:
	noww = [int(x) for x in time.strftime("%H:%M:%S", time.localtime()).split(':')]
	if noww[0]-6==0 and noww[1]-0==0 and noww[2] in range(0, 15):
		a()
