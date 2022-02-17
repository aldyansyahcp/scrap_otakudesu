import requests
from bs4 import BeautifulSoup as bs
import csv
import os

header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
      'Cache-Control':'max-age=0'
}
green= "\033[0;32m"
blue= "\033[0;36m"
red= "\033[31;1m"
def pencarian():
    cari = input("\n\tMau cari anime apa: ")
    try: 
        url = "https://otakudesu.pro/?s={}&post_type=anime".format(cari)
        req = requests.get(url, headers=header)
        bes = bs(req.text, "html.parser")
    except IndexError:
        print("Ditulis ya ajg")
        os.system("clear")
        os.system("exit")
    return bes

def milih():
    bs = pencarian()
    name = bs.find_all("li", attrs={"style":"list-style:none;"})
    print("="*60)
    print("\n\t\t     ________________ \n\t\t    | Dipilih ya ajg |\n\t\t     ````````````````")
    result_judul = []
    result_link = []
    n = 1
    for i in name:
        nam = i.find("a", attrs={"data-wpel-link":"internal"}).string
        lin = i.find("a")
        link = lin["href"]
        result_link.append(link)
        result_judul.append(nam)
    for i in result_judul:
        print(n,i)
        n+=1
    """for r in result_link:
        print(count,r)
        count+=1"""
    return result_link

def execute():
    link = milih()
    res = []
    try:
        pilih = int(input("Pilih Nomor brp: "))-1
        os.system("clear")
        print("="*60)
        print("\n\t\t     ________________ \n\t\t    | Dipilih ya ajg |\n\t\t     ````````````````")
        """pil = link[int(pilih)-1]
        st = " "
        dipilih = st.join(pil)"""
        rek = requests.get(link[pilih], headers=header)
        soup = bs(rek.text, "html.parser")
        n=1
        for u in soup.find_all("a", attrs={"target":"_blank"}):
            lin = u["href"]
            judl = u.string
            #print(u.prettify())
            if "-episode-" in lin or "-sp-" in lin or "-batch-" in lin:
                #print(n,lin)
                print(n,judl)
                n+=1
                res.append(lin)
    except ValueError:
        print("Pilih nomor angka ya ajg\n")
        os.system("clear")
        os.system("exit")
    return res

def main():
    eps = execute()
    try:
        pi = int(input("Piiilih Nomor brp: "))-1
        os.system("clear")
        print("="*50)
        rek = requests.get(eps[pi], headers=header)
        soup = bs(rek.text, "html.parser")
        n=1
        print(" Bila anda tadi memilih batch bisa input 100\nDownload dari\n 1. Zippyshare\n 2. Files.io\n 3. Racaty\n 4. Acefile\n 5. DesuDrive")
        print(" Urutan download dari atas 0-2 360p-780p dan 3-6 resolusi Mkv")
        pili = int(input("Pilih download dari: "))
        os.system("clear")
        print("="*50)
        if pili == 1:
            for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                #print(n,l.prettify())
                name = l["href"]
                lin = []
                if "zippyshare" in name:
                    lin.append(name)
                    for i in lin:
                        print(n,i)
                        n+=1
                else:
                    pass
        elif pili == 100:
                    print("Download dari\n 1. Racaty\n 2. OtakuDrive\n 3. DesuDrive\n 4. Mega\n 5. Acefile\n 6. Uptobox\n Urutan download dari atas 360p-720p")
                    pir = int(input("Pilih download dari: "))
                    if pir == 1:
                        for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                            name = l["href"]
                            lin = []
                            if "racaty" in name:
                                lin.append(name)
                                for i in lin:
                                    print(n,i)
                                    n+=1
                            else:
                                pass
                    elif pir == 2:
                        for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                            name = l["href"]
                            lin = []
                            if "otakudrive" in name:
                                lin.append(name)
                                for i in lin:
                                    print(n,i)
                                    n+=1
                            else:
                                pass
                    elif pir == 3:
                        for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                            name = l["href"]
                            lin = []
                            if "desudrive" in name:
                                lin.append(name)
                                for i in lin:
                                    print(n,i)
                                    n+=1
                            else:
                                pass
                    elif pir == 4:
                        for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                            name = l["href"]
                            lin = []
                            if "mega" in name:
                                lin.append(name)
                                for i in lin:
                                    print(n,i)
                                    n+=1
                            else:
                                pass
                    elif pir == 5:
                        for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                            name = l["href"]
                            lin = []
                            if "acefile" in name:
                                lin.append(name)
                                for i in lin:
                                    print(n,i)
                                    n+=1
                            else:
                                pass
                    elif pir == 6:
                        for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):
                            name = l["href"]
                            lin = []
                            if "uptobox" in name:
                                lin.append(name)
                                for i in lin:
                                    print(n,i)
                                    n+=1
                            else:
                                pass
                    else:
                        print("Pilihanya same 5 ya ajg")
                        os.system("clear")
                        os.system("exit")
        elif pili == 2:
                for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}): 
                    name = l["href"]
                    lin = []
                    if "files.im" in name:                       
                        lin.append(name)                                                             
                        for i in lin:                                                                                                
                            print(n,i)
                            n+=1
                    else:
                        pass
        elif pili == 3:
                for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):                  
                    name = l["href"]                                                                       
                    lin = []
                    if "racaty.net" in name:                                                                                      
                        lin.append(name)
                        for i in lin:                                                                                                 
                            print(n,i)
                            n+=1
                    else:
                        pass
        elif pili == 4:
                for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):                       
                    name = l["href"]                                 
                    lin = []
                    if "acefile.co" in name:                                                                                      
                        lin.append(name)
                        for i in lin:                                                                                                 
                            print(n,i)
                            n+=1
                    else:
                        pass
        elif pili == 5:
                for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):                           
                    name = l["href"]                               
                    lin = []
                    if "mega.nz" in name:                                                                                        
                        lin.append(name)
                        for i in lin:                                                                                                 
                            print(n,i)
                            n+=1
                    else:
                        pass
        elif pili == 6:
                for l in soup.find_all("a", attrs={"rel":"nofollow external noopener noreferrer"}):                           
                    name = l["href"]                          
                    lin = []
                    if "megaup.net" in name:                                                                                      
                        lin.append(name)
                        for i in lin:                                                                                                 
                            print(n,i)
                            n+=1
                    else:
                        pass
        else:
            print("Pilihan hanya sampai 6 ya su!")
    except ValueError:
        print("Pilihanya sampe 6 ya ajg")
        os.system("clear")
        os.system("exit")
    except TypeError:
        print("Jan dikosongin ajg")
        os.system("clear")
        os.system("exit")
        
if __name__ == "__main__":
    os.system("clear")
    print(blue+"   ____  __        __             __               \n  / __ \/ /_____ _/ /____  ______/ /__  _______  __\n / / / / __/ __ `/ //_/ / / / __  / _ \/ ___/ / / /\n/ /_/ / /_/ /_/ / ,< / /_/ / /_/ /  __(__  ) /_/ / \n\____/\__/\__,_/_/|_|\__,_/\__,_/\___/____/\__,_/  ")
    print(green+"   ____\n  / ___/______________ _____  ____  ___  _____\n  \__ \/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/\n ___/ / /__/ /  / /_/ / /_/ / /_/ /  __/ /    \n/____/\___/_/   \__,_/ .___/ .___/\___/_/     \n                    /_/   /_/                 ")
    main()
