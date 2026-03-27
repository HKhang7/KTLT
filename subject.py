class Subject:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"{self.id} {self.name} {self.credit}"