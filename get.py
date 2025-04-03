def get_string(prompt: str) -> str:
    while True:
        try:
            response = input(prompt).strip()
            return response
        except:
            continue

def get_int(prompt: str, index: int) -> int:
    while True:
        try:
            response = int(input(prompt))
            if index == 0:
                return (response - 1)
            
            elif index == 1:
                return response
            
            else:
                continue

        except TypeError:
            print("Invalid input. Only one-indexed integers are allowed.")