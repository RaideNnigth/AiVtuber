import pandas as pd
from datetime import datetime
import re


def get_chat_dataframe(file):
    data = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n\n\n')

        for line in lines:
            try:
                time_logged = line.split('—')[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                username_message = line.split('—')[1:]
                username_message = '—'.join(username_message).strip()
                username, channel, message = re.search(
                        ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message).groups()
                d = {
                    'Hora': time_logged,
                    'channel': channel,
                    'username': username,
                    'message': message
                }

                data.append(d)
            except Exception:
                pass
    return pd.DataFrame().from_records(data)
df = get_chat_dataframe('chat.log')
df.set_index('Hora', inplace=True)
df.head()
print(df)