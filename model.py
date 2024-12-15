from controller import *

class TaxProfileDatabase:
    def __init__(self):
        self.profiles = {}

    def add_profile(self, tax: TaxController):
        self.profiles[tax._name] = tax

    def get_profile(self, name: str) -> TaxController | None:
        return self.profiles.get(name)

    def get_all_profiles(self) -> list[TaxController]:
        return list(self.profiles.values())
    
    def check_profiles_name(self, name) -> bool:
        return name in self.profiles

    def update_profile_name(self, old_name: str, new_name: str) -> bool:
        if new_name in self.profiles:
            return False
        self.profiles[old_name]._name = new_name
        self.profiles[new_name] = self.profiles.pop(old_name)
        return True
    
    def update_profile_income(self, name: str, new_income: float):
        self.profiles[name]._income = new_income


    def update_profile_deductions(self, name: str, new_deductions: float):
        self.profiles[name]._deductions = new_deductions