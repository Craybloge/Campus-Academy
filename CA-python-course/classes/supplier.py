"""
module docstring
"""


class Supplier:
    """
    module docstring
    """
    def __init__(self, name, factory_siting, nationality):
        self.name = name
        self.factory_siting = factory_siting
        self.nationality = nationality
        self.historique_achat = []

    def historique_achat_supplier(self, product):
        """
        module docstring
        """
        self.historique_achat.append(product)

    def funcname(self, parameter_list):
        """
        docstring
        """
