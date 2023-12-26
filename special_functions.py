from tabulate import tabulate
import os
import time


def centre_table(table,table_type):
    table_str = tabulate(table,tablefmt=table_type)
    # head_out = tabulate(Header, tablefmt='grid',showindex=False)     just for reference yeah
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(table_str.split("\n")[0])) // 2
    
    # Print the table with centered padding ,, don't forget 
    for line in table_str.split("\n"):
        centered_table = " " * padding + line
        print(centered_table)



def centre_txt(text,artifacts):
    if artifacts: # specially use this for notorios strings and arts that just wont print correctly 
        logo_lines = text.split("\n")
 
        max_line_width = max(len(line) for line in logo_lines) # This calculates the maximum width of any line, almost killed me haaaaah

        terminal_width = os.get_terminal_size().columns
        padding = (terminal_width - max_line_width) // 2
        for line in logo_lines:
            centered_line = " " * padding + line
            print(centered_line)
    else:
        terminal_width = os.get_terminal_size().columns
        padding = (terminal_width - len(text)) // 2
        centered_text = " " * padding + text
        print(centered_text)


def fix_list_for_tabulate(unprocessed_list):
    list_len = len(unprocessed_list)
    n = list_len // 5  # this was implemented for print a table with only 5 elements in a row

    if list_len % 5 != 0:
        n += 1  # Increment n if there's a remainder

    processed_lists = []
    for i in range(0, n):
        processed_list = unprocessed_list[i*5 : (i+1)*5]  
        processed_lists.append(processed_list)

    return processed_lists



def refresh_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()

def logo():
    logo = f"""
                                                                                                                                
          ____                      ____                                                                                        
        ,'  , `.    ,---,.        ,'  , `.        ,-.----.       ,---,.  ,----..               ,-.----.                  ,---,. 
     ,-+-,.' _ |  ,'  .' |     ,-+-,.' _ |        \    /  \    ,'  .' | /   /   \         ,--, \    /  \        ,---.  ,'  .' | 
  ,-+-. ;   , ||,---.'   |  ,-+-. ;   , ||        ;   :    \ ,---.'   ||   :     :      ,'_ /| ;   :    \      /__./|,---.'   | 
 ,--.'|'   |  ;||   |   .' ,--.'|'   |  ;|        |   | .\ : |   |   .'.   |  ;. / .--. |  | : |   | .\ : ,---.;  ; ||   |   .' 
|   |  ,', |  '::   :  |-,|   |  ,', |  ':        .   : |: | :   :  |-,.   ; /--`,'_ /| :  . | .   : |: |/___/ \  | |:   :  |-, 
|   | /  | |  ||:   |  ;/||   | /  | |  ||        |   |  \ : :   |  ;/|;   | ;   |  ' | |  . . |   |  \ :\   ;  \ ' |:   |  ;/| 
'   | :  | :  |,|   :   .''   | :  | :  |,        |   : .  / |   :   .'|   : |   |  | ' |  | | |   : .  / \   \  \: ||   :   .' 
;   . |  ; |--' |   |  |-,;   . |  ; |--'         ;   | |  \ |   |  |-,.   | '___:  | | :  ' ; ;   | |  \  ;   \  ' .|   |  |-, 
|   : |  | ,    '   :  ;/||   : |  | ,            |   | ;\  \'   :  ;/|'   ; : .'|  ; ' |  | ' |   | ;\  \  \   \   ''   :  ;/| 
|   : '  |/     |   |    \|   : '  |/             :   ' | \.'|   |    \'   | '/  :  | : ;  ; | :   ' | \.'   \   `  ;|   |    \ 
;   | |`-'      |   :   .';   | |`-'              :   : :-'  |   :   .'|   :    /'  :  `--'   \:   : :-'      :   \ ||   :   .' 
|   ;/          |   | ,'  |   ;/                  |   |.'    |   | ,'   \   \ .' :  ,      .-./|   |.'         '---" |   | ,'   
'---'           `----'    '---'                   `---'      `----'      `---`    `--`----'    `---'                 `----'                                                                                                                                     
"""
    centre_txt(logo,artifacts=True)