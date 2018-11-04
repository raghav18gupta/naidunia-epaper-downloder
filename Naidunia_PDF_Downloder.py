import os
import datetime
import PyPDF2
import requests
import subprocess

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

os.chdir('/home/raghav/Desktop')
merger.write(today.strftime('%d%m%Y')+'_Indore.pdf')
subprocess.Popen(['rm', '-rf', f'{dirr}/temp'])

print('Done... Join t.me/NaiDunia')
