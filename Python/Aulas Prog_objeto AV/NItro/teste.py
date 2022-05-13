import random, string, requests, threading
from discord_webhook import DiscordWebhook

f = open("Valid Nitro.txt", "w", encoding='utf-8')

x = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{x}?with_application=false&with_subscription_plan=true"
web = "https://discordapp.com/api/webhooks/970319508818501692/UfnUpNp-TQqqgSulRVKteDLFygLyLUkegAWKE74F-C0mogqmDpH9Aw3yWcSYMcDBtLAm"

request = requests.get(url = url)
a = request.json()

def nitro():
    while True:
        x = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        webhook = DiscordWebhook(url=web, content=f"@everyone discord.gift/{x}")
        if a['code'] == int(200):
            print(f"Valid Nitro Code > discord.gift/{x}")
            f.write(f"discord.gift/{x}\n")
            webhook.execute()
        else:
            print(f"Invalid Nitro Code > discord.gift/{x}")
nitrin = threading.Thread(target=nitro)
nitrin.start()