import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init()

def get_key():
    cookies = {
        'cf_clearance': 'JWho8UtsA0rVLO35JXFdScLoZxxyGczbzGScWoPTSpQ-1701792122-0-1-87e6d8a1.ba58baad.df76a9f7-0.2.1701792122',
    }

    headers = {
        'authority': 'galaxyswapperv2.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'cf_clearance=JWho8UtsA0rVLO35JXFdScLoZxxyGczbzGScWoPTSpQ-1701792122-0-1-87e6d8a1.ba58baad.df76a9f7-0.2.1701792122',
        'referer': 'https://lootlinks.co/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    response = requests.get('https://galaxyswapperv2.com/Key/Create.php', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    key_div = soup.find('div')
    key = key_div.text.strip()
    return key


print(Fore.RED + '''
 ██████╗  █████╗ ██╗      █████╗ ██╗  ██╗██╗   ██╗    ███████╗██╗    ██╗ █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝ ██╔══██╗██║     ██╔══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██║    ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ███╗███████║██║     ███████║ ╚███╔╝  ╚████╔╝     ███████╗██║ █╗ ██║███████║██████╔╝██████╔╝█████╗  ██████╔╝
██║   ██║██╔══██║██║     ██╔══██║ ██╔██╗   ╚██╔╝      ╚════██║██║███╗██║██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║███████╗██║  ██║██╔╝ ██╗   ██║       ███████║╚███╔███╔╝██║  ██║██║     ██║     ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                                
██╗  ██╗███████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗       
██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗      
█████╔╝ █████╗   ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝      
██╔═██╗ ██╔══╝    ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗      
██║  ██╗███████╗   ██║       ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║      
╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      
                                                                                                                                                                                                                                        
''')

value = input(f"{Fore.RESET}How much Keys > ")

x = 0

for x in range(int(value)):
    x += 1
    key = get_key()
    print(f"{x} {Fore.RED}> {Fore.RESET}{key}")
    with open("keys.txt","a") as f:
        f.write(f"{key}\n")
