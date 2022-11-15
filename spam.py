from telethon import TelegramClient
from telethon.errors import rpcerrorlist, FloodWaitError, ChatWriteForbiddenError
import time
import os
try:
    import progressbar
except ModuleNotFoundError:
    print("bu kütüphaneyi indir > pip install progressbar2") 


if os.path.isfile('spam.txt'):
    with open('spam.txt', 'r') as r:
        data = r.readlines()
    api_id = int(data[0])
    api_hash = data[1]

else:
    api_id = input('API ID gir: ')
    api_hash = input('API HASH gir: ')
    with open('spam.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('spamer', api_id, api_hash)


async def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    global target
    print('''
        .___             __                                            
  __| _/____ _______|  | __           ____   ____ _____________    
 / __ |\__  \\_  __ \  |/ /  ______ _/ __ \ /    \\___   /\__  \   
/ /_/ | / __ \|  | \/    <  /_____/ \  ___/|   |  \/    /  / __ \_ 
\____ |(____  /__|  |__|_ \          \___  >___|  /_____ \(____  / 
     \/     \/           \/              \/     \/      \/     \/  ''')
    print('\n\nReis burdan bir hedef belirle..')
    i = 0
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(i, ':', dialog.name, 'has ID', dialog.id)
        i = i + 1

    confirm = False
    max = len(dialogs) - 1

    while confirm == False:
        target_index = -1

        # Get target chat
        while target_index < 0 or target_index > max:
            print('Please insert target between 0 and', max)
            target_index = int(input())
            if target_index < 0 | target_index > max:
                print('target out of range')

        target = dialogs[target_index]
        print('target is', target.name, 'with ID', target.id)

        # Wait for confirm
        print('Onaylıyormusun? Y/N')
        reply = input()[0]
        if reply == 'Y' or reply == 'y':
            confirm = True

    msg = int(message.message_id("mesaj id gir : "))
    Several = int(input("kaç tane Göndermek istersin?\n"))

    print("Hedef Yanlış ise Ctrl-Z kullanabilirsin.")
    print('3 saniye icinde basliyor...')
    time.sleep(3)
    print("[+] Spam atmaya başladık yaslan geriye :)")
    bar = progressbar.ProgressBar(
        widgets=[progressbar.SimpleProgress()],
        max_value=Several,
    ).start()
    try:
        for i in range(int(Several)):
            await client.send_message(target.id, msg)
            bar.update(i + 1)
        bar.finish()
        print("[+] Spam tamamlandı..")
    except rpcerrorlist.ChatAdminRequiredError:
        print("[!] Sohbete mesaj gönderimin kısıtlanmış !")
    except ChatWriteForbiddenError:
        print("[!] Sohbete Mesaj Gönderimin Kısıtlı!")
    except FloodWaitError:
        print("[!] Tamam Yorma kendini Sonra denersin :)")


with client:
    client.loop.run_until_complete(main())
