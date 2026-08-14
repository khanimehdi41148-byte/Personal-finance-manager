class transaction:
    def __init__(
            self,
            transaction_id,
            transaction_type,
            description,
            amount,
            category,
            date
    ):
        self.transaction_id = id
        self.transaction_type = type
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date
    def to_dict(self):
        return(
            "id": self.id,
            "type": self.type,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": str(self.date)
        )

    def __str__(self):
        return(
            f"Id: {self.id} | "
            f"Type: {self.type} | "
            f"Description: {self.description} | "
            f"Amount: {self.amount} | "
            f"Category: {self.category} | "
            f"Date: {self.date} | "
        )