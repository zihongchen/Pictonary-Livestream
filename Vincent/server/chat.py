

class Chat(object):
    def __init__(self):
        self.data = []
    
    def update_chat(self, msg: str) -> None:
        self.data.append(msg)

    def get_chat(self):
        return self.data

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self) -> str:
        return "".join(self.data)

    def __repr__(self) -> str:
        return str(self)
    

