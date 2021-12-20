"""
module docstring
"""


class Customer:
    """
    class docstring
    """
    def __init__(self, name, firstname):
        self.name = name
        self.firstname = firstname
        self.total_amount = 0
        self.historique_achat = []
        self.last_buy = None

    def achat(self, date, model):
        """
        method docstring
        """
        self.total_amount += model.price
        self.last_buy_function(model, date)
        self.historique_achat.append(model)

    def last_buy_function(self, model, date):
        """
        method docstring
        """
        self.last_buy = (model, date)
