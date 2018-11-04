from telegram.error import NetworkError, Unauthorized
import telegram
import datetime
import requests
import PyPDF2
import subprocess
import os

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

# os.chdir('/home/raghav/Desktop')
final_file = today.strftime('%d%m%Y')+'_Indore.pdf'
merger.write(final_file)


# Telegram Code
print('Uploading in Telegram')
token = 'i_wouldnt_reveal'
cid = 0 # its another private number
bot = telegram.Bot(token)
update_id = bot.get_updates()[0].update_id
bot.send_document(chat_id=cid, document=open(final_file, 'rb'), timeout=2000)
subprocess.Popen(['rm', '-rf', f'{dirr}/temp'])
subprocess.Popen(['rm', '-rf', final_file])

print('Done... Join t.me/NaiDunia')
