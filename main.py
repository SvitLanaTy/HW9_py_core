
EXIT_COMMANDS = ("good bye", "close", "exit")

contacts_info = {}


def input_error(func):
    def inner(*args):
        try:            
            return func(*args)
        
        except (ValueError, IndexError, KeyError):
            return f"Unknown command or parametrs. Correct commands: add name phone | change name newphone | phone name | show all | hello | good bye | close | exit. For commands ADD and CHANGE - Name and Phone are required. For command PHONE - Name is required." 
        
        except Exception as err:
            return f"Exception: {err}.\nCorrect commands: add name phone | change name newphone | phone name | show all | hello | good bye | close | exit"
        
    return inner


@input_error
def handle_hello():
    return "How can I help you?"


@input_error
def handle_show_all():
    if contacts_info:
        result = ""
        for name, phone in contacts_info.items():
            result += f"{name} : {phone} \n"
        return result
    else:
        return "Contact book is empty......"


@input_error
def handle_add(*args):
    name, phone = args
    if name in contacts_info:
        return f"Contact << {name} : {phone} >> already exists!!! Maybe you want to change this contact...."
    else:
        contacts_info[name] = phone    
        return f"Contact << {name} : {phone} >> added sucessfully."


@input_error
def handle_phone(args):
    name = args
    phone = contacts_info[name]     
    return f"Contact {name} has phone: << {phone} >> "


@input_error
def handle_change(*args):
    name, new_phone = args
    if name in contacts_info:
        contacts_info[name] = new_phone
        return f"Contact << {name} : {new_phone} >> changed sucessfully."
    else:
        return f"Unknow contact << {name} >> !"
    

COMMANDS = {
    "hello": handle_hello,
    "add": handle_add,
    "change": handle_change,
    "phone": handle_phone,
    "show all": handle_show_all
}


def command_parser(input_str):    
    command, *args = input_str.split()
        
    if command not in COMMANDS:        
        for key in COMMANDS:
            if input_str.startswith(key):
                command = key            
    args = input_str.removeprefix(command).strip().split(" ", 1)
                        
    return command, *args
      

def main():
    print("Hello. Your bot helper is ready.")
    
    while True:        
        input_str = input("Enter your command: ").lower().strip()
        if len(input_str) == 0:
            continue
        else:
            if input_str in EXIT_COMMANDS:
                print("Good bye!")
                break
            elif input_str == '.':
                break
            
            command, *args = command_parser(input_str)            
            if command in COMMANDS:
                result = COMMANDS[command](*args) if args[0] != '' else COMMANDS[command]()
                print(result)
            else:
                print(f"Unknown command: <<< {input_str} >>>, Correct commands: add name phone | change name newphone | phone name | show all | hello | good bye | close | exit")
                
                
if __name__ =="__main__":
    main()

