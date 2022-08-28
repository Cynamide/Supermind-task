from telethon.sync import TelegramClient
import pandas as pd


api_id = 14393217
api_hash = "ecee2f714c6219e2c5354cef49d69fa7"

chats = ['cryptosignals0rg', 'altsignals',
         'mycryptopedia', 'btcchamp', 'onwardbtc_official']


df = pd.DataFrame()

for chat in chats:
    with TelegramClient('anon', api_id, api_hash) as client:
        total = ""
        count = 0
        for message in client.iter_messages(chat):
            try:
                message.text = message.text.replace('\n', ' ')
                message.text = message.text.replace('\t', ' ')
                message.text = message.text.replace('\r', ' ')
                total += message.text + ' '
                count += 1
            except:
                print("Error")

        print(chat+": "+str(count))

        data = {"group": chat, "text": total}

        temp_df = pd.DataFrame(data, index=[1])
        df = df.append(temp_df)
        df.to_csv("data_scrapped.csv")
