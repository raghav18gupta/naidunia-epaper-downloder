import telegram
import datetime
import time
import requests
import PyPDF2
import subprocess
import os


def worker():
    merger = PyPDF2.PdfFileMerger()
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
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
        rtm_var = ['ngr', 'rtm', 'mnd']  # add more link part here
        path = f'{dirr}/temp/{page}.pdf'

        try:
            for i, rtm in enumerate(rtm_var):
                url = f'https://naiduniaepaper.jagran.com/epaperimages/{dayy}/indore/{ngr}{rtm}-pg{page}-0.pdf'
                print('\t', url)
                r = requests.get(url, stream=True)
                if r.status_code == 404:
                    if i == len(rtm_var) - 1:
                        raise Exception("That's the end")
                    continue
                break

            with open(path, 'ab') as fd:
                for chunk in r.iter_content(1000):
                    fd.write(chunk)
            merger.append(PyPDF2.PdfFileReader(path, 'rb'))

        except BaseException as e:
            print(e)
            print(f'Total {page-1} pages')
            break

    print('Merging PDF')
    final_file = today.strftime('%d-%m-%Y') + '_Naidunia.pdf'
    merger.write(final_file)

    # Telegram Code
    print('Uploading in Telegram')
    token = 'token-string'
    chatid = -0000  # channel-id
    bot = telegram.Bot(token)
    bot.send_document(chat_id=chatid,
                      document=open(final_file, 'rb'), timeout=2000)
    subprocess.Popen(['rm', '-rf', f'{dirr}/temp'])
    subprocess.Popen(['rm', '-rf', final_file])

    print('Done... Join t.me/NaiDunia')

worker()
