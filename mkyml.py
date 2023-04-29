import yaml
import os
aproject = {'tg_bot_token': os.get('TG_BOT_TOKEN'),'tg_chat_id': os.get('TG_CHAT_ID')}
with open("/root/.tg_jav_bot/config.yaml", 'w') as f:
  f.write(yaml.dump(aproject))

