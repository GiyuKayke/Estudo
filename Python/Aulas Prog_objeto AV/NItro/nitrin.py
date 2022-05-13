import random, string, z, threading

f = open("Valid Nitro.txt", "w", encoding='utf-8')

x = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{x}?with_application=false&with_subscription_plan=true"

request = requests.get(url = url)
a = request.json()

def nitro():
    while True:
        x = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        if a['code'] == int(200):
            print(f"Valid Nitro Code > discord.gift/{x}")
            f.write(f"discord.gift/{x}\n")
        else:
            print(f"Invalid Nitro Code > discord.gift/{x}")

nitrin = threading.Thread(target=nitro)
nitrin.start()