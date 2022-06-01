import time
try:
    import os
    from os import system
    system("title " + "Webhook Spammer")
except:
    pass

error = False

try:
    import requests, colorama
except:
    error = True

if error == True:
    print("Missing Modules, Press Enter To Start Repair (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama")
        os.system("pip install requests")
        print("Problem May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Failed To Fix")
        input("")
        exit()





def webhook_spammer():
    colorama.init(autoreset=True)
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r_check = requests.get(webhook).json
            r_check = str(r_check)
            if "200" in r_check:
                break
            if "200" not in r_check:
                print(colorama.Fore.RED + "Webhook Invalid, Please Enter A Valid One")
        except Exception:
            print(colorama.Fore.RED + "Webhook Invalid, Please Enter A Valid One")
    content = input("Enter Message: ")
    while True:
        avatar_y_n = input("Want An Avatar (y/n): ")
        if avatar_y_n == "n" or avatar_y_n == "y":
            break
        else:
            print(colorama.Fore.RED + "Enter A Valid Choice")
    if avatar_y_n == "y":
        while True:
            avatar_url = input("Enter Avatar Url: ")
            if "http://" in avatar_url or "https://" in avatar_url:
                break
            else:
                print(colorama.Fore.RED + "Enter A Valid Choice")
    if avatar_y_n == "n":
        avatar_url = ""
    username = input("Enter Bot Username: ")
    while True:
        limit = input("Enter Limit (i for infinity): ")
        if limit == "i" or limit == "I":
            break
        try:
            limit = int(limit)
            break
        except Exception:
            print(colorama.Fore.RED + "Enter A Valid Choice")
    while True:
        try:
            delay = input("Enter Delay (0 For None): ")
            delay = float(delay)
            break
        except:
            print(colorama.Fore.RED + "Enter A Valid Choice")
    if limit == "i" or limit == "I":
        limit = str(limit)
        
    done = 0
    while True:
        limit = str(limit)
        r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
        r = str(r)
        if "i" not in str(limit) and "204" in r:
            done = int(done) + 1
        if "i" in limit or "I" in limit:
            done == ""
        if "204" in r:
            if "i" not in limit and "I" not in limit:
                print(colorama.Fore.GREEN + f"Message Succsesfully Sent ({done})")
            if "i" in limit or "I" in limit:
                print(colorama.Fore.GREEN + "Message Succsesfully Sent")
        if "204" not in r:
            print(colorama.Fore.YELLOW + "Rate Limited, Retrying...")
        try:
            if int(done) == int(limit):
                print("Done")
                input("")
                return
        except Exception:
            pass
        time.sleep(float(delay))

webhook_spammer()