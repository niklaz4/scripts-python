import rarfile

def extrair_arquivo_rar(arquivo_rar, senha):
    try:
        with rarfile.RarFile(arquivo_rar, 'r') as rfile:
            rfile.extractall(pwd=senha.encode('utf-8'))
        return senha
    except rarfile.BadRarFile as e:
        print(f"Erro ao extrair o arquivo RAR: {e}")
        return None
    except rarfile.RarCRCError:
        print("Senha incorreta.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def main():
    arquivo_rar = 'teste.rar'
    senha_file = open('lista.txt', 'r')
    
    for line in senha_file.readlines():
        senha = line.strip('\n')
        guess = extrair_arquivo_rar(arquivo_rar, senha)
        
        if guess:
            print(f"Senha encontrada: {senha}")
            break

    senha_file.close()

if __name__ == '__main__':
    main()