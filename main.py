from LeetcodeSolver import LeetcodeSolver
from LeetcodeScraper import LeetcodeScraper
from colorama import init, Fore

init(autoreset=True)

def main():
    ascii_art = r""" __                              __       ______                                __                           
/  |                            /  |     /      \                              /  |                          
$$ |        ______    ______   _$$ |_   /$$$$$$  |  ______   ______    _______ $$ |   __   ______    ______  
$$ |       /      \  /      \ / $$   |  $$ |  $$/  /      \ /      \  /       |$$ |  /  | /      \  /      \ 
$$ |      /$$$$$$  |/$$$$$$  |$$$$$$/   $$ |      /$$$$$$  |$$$$$$  |/$$$$$$$/ $$ |_/$$/ /$$$$$$  |/$$$$$$  |
$$ |      $$    $$ |$$    $$ |  $$ | __ $$ |   __ $$ |  $$/ /    $$ |$$ |      $$   $$<  $$    $$ |$$ |  $$/ 
$$ |_____ $$$$$$$$/ $$$$$$$$/   $$ |/  |$$ \__/  |$$ |     /$$$$$$$ |$$ \_____ $$$$$$  \ $$$$$$$$/ $$ |      
$$       |$$       |$$       |  $$  $$/ $$    $$/ $$ |     $$    $$ |$$       |$$ | $$  |$$       |$$ |      
$$$$$$$$/  $$$$$$$/  $$$$$$$/    $$$$/   $$$$$$/  $$/       $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       
                                                                                                             
                                                                                                             
                                                                                                             """
    print(Fore.RED + ascii_art)
    print(Fore.GREEN + "Choose an option:")
    print("1. Run LeetcodeSolver")
    print("2. Run LeetcodeScraper")
    choice = input(Fore.GREEN + "Enter your choice (1 or 2): ")

    if choice == "1":
        solver = LeetcodeSolver()
        solver.solve()
    elif choice == "2":
        scraper = LeetcodeScraper()
        scraper.scrape_accepted_solutions()
    else:
        print(Fore.RED + "Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
