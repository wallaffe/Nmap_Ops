import subprocess
from colorama import Fore, Style

def execute_option(option):
    if option == 0:
        print(Fore.GREEN + "Saindo do programa." + Style.RESET_ALL)
        exit()

    target = input("Informe o alvo: ")
    if option == 1:
        scan_command = ["nmap", target]
    elif option == 2:
        scan_command = ["nmap", "-v", target]
    elif option == 3:
        port_range = input("Informe o intervalo de portas (ex: 1-100): ")
        scan_command = ["nmap", "-p", port_range, target]
    elif option == 4:
        scan_command = ["nmap", "-sV", target]
    elif option == 5:
        scan_command = ["nmap", "-A", target]
    elif option == 6:
        scan_command = ["nmap", "-sV", "-A", target]
    elif option == 7:
        scan_command = ["nmap", "-sn", target]
    elif option == 8:
        subnet = input("Informe a sub-rede (ex: 192.168.1.0/24): ")
        scan_command = ["nmap", "-sP", subnet]
    elif option == 9:
        custom_options = input("Informe as opções personalizadas do Nmap: ")
        scan_command = ["nmap"] + custom_options.split() + [target]
    elif option == 10:
        targets = input("Informe os alvos separados por espaço: ")
        scan_command = ["nmap"] + targets.split()
    elif option == 11:
        output_file = input("Informe o nome do arquivo para exportar os resultados: ")
        scan_command = ["nmap", "-oN", output_file, target]
    elif option == 12:
        scan_command = ["nmap", "-sU", target]  # Escaneamento UDP
    elif option == 13:
        scan_command = ["nmap", "--script", "default", target]  # Escaneamento de scripts NSE
    elif option == 14:
        scan_command = ["nmap", "-sV", "--version-all", target]  # Escaneamento de banners
    elif option == 15:
        scan_command = ["nmap", "--script", "ssl-enum-ciphers", target]  # Escaneamento de SSL/TLS
    elif option == 16:
        scan_command = ["nmap", "--reason", target]  # Escaneamento de firewall
    elif option == 17:
        scan_command = ["nmap", "-PR", target]  # Escaneamento de tráfego ARP
    elif option == 18:
        scan_command = ["nmap", "--script", "vuln", target]  # Escaneamento de hosts vulneráveis
    elif option == 19:
        scan_command = ["nmap", "-O", target]  # Escaneamento de sistemas operacionais remotos
    elif option == 20:
        scan_command = ["nmap", "-sP", target]  # Escaneamento de hosts ativos

    try:
        subprocess.run(scan_command, check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Erro ao executar o comando: {e}" + Style.RESET_ALL)

def main():
    print(Fore.BLUE + "-------------------------------------------------------")
    print("            NMAP OPS - Interface           ")
    print("-------------------------------------------------------" + Style.RESET_ALL)
    print("\nEscolha uma opção:\n")
    print(Fore.CYAN + "[1] Scan rápido")
    print(Fore.GREEN + "[2] Scan detalhado")
    print(Fore.MAGENTA + "[3] Scan de portas específicas")
    print(Fore.YELLOW + "[4] Scan de serviços")
    print(Fore.RED + "[5] Scan com detecção de sistema operacional")
    print(Fore.CYAN + "[6] Scan de versões de serviços")
    print(Fore.GREEN + "[7] Scan de hosts vivos")
    print(Fore.MAGENTA + "[8] Scan de sub-redes")
    print(Fore.YELLOW + "[9] Personalizado")
    print(Fore.RED + "[10] Escanear múltiplos alvos")
    print(Fore.CYAN + "[11] Exportar resultados para um arquivo")
    print(Fore.GREEN + "[12] Escaneamento UDP")
    print(Fore.MAGENTA + "[13] Escaneamento de scripts NSE")
    print(Fore.YELLOW + "[14] Escaneamento de banners")
    print(Fore.RED + "[15] Escaneamento de SSL/TLS")
    print(Fore.CYAN + "[16] Escaneamento de firewall")
    print(Fore.GREEN + "[17] Escaneamento de tráfego ARP")
    print(Fore.MAGENTA + "[18] Escaneamento de hosts vulneráveis")
    print(Fore.YELLOW + "[19] Escaneamento de sistemas operacionais remotos")
    print(Fore.RED + "[20] Escaneamento de hosts ativos")
    print(Fore.GREEN + "[0] Sair" + Style.RESET_ALL)

    while True:
        try:
            option = int(input("\nOpção: "))
            if option < 0 or option > 20:
                raise ValueError
            else:
                execute_option(option)
        except ValueError:
            print(Fore.YELLOW + "Opção inválida. Por favor, escolha uma opção válida." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
