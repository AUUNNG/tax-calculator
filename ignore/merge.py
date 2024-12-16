class TaxController:
    def __init__(self, name: str, income: float, deductions: float):
        self._name = name
        self._income = income
        self._deductions = deductions

    def calculate_tax(self) -> float:
        taxable_income = self._income
        taxable_income -= min(taxable_income*.5, 100000)
        taxable_income -= 60000
        taxable_income -= self._deductions
        if taxable_income >= 5000001:
            return ((taxable_income-5000000)*.35) + 7500 + 20000 + 37500 + 50000 + 250000 + 900000
        elif taxable_income >= 2000001:
            return ((taxable_income-2000000)*.3) + 7500 + 20000 + 37500 + 50000 + 250000
        elif taxable_income >= 1000001:
            return ((taxable_income-1000000)*.25) + 7500 + 20000 + 37500 + 50000
        elif taxable_income >= 750001:
            return ((taxable_income-750000)*.2) + 7500 + 20000 + 37500
        elif taxable_income >= 500001:
            return ((taxable_income-500000)*.15) + 7500 + 20000
        elif taxable_income >= 300001:
            return ((taxable_income-300000)*.1) + 7500
        elif taxable_income >= 1500001:
            return ((taxable_income-150000)*.05)
        elif taxable_income < 1500001:
            return 0

    def __str__(self):
        return f"Name: {self._name}, Income: {self._income}, Deductions: {self._deductions}, Tax Due: {self.calculate_tax()}"

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

class TaxCalculatorView:
    def __init__(self):
        self.db = TaxProfileDatabase()

    def ui_main_menu(self):
        while True:
            print("\nTax Information System")
            print("  [1] Add a new tax profile.")
            print("  [2] View a tax profile by name.")
            print("  [3] List all tax profiles.")
            print("  [4] Update tax profile name.")
            print("  [5] Update tax profile income.")
            print("  [6] Update tax profile deductions.")
            print("  [7] Exit.")
            result = input("  Choose one [1|2|3|4|5|6|7]: ")
            try:
                match int(result):
                    case 1: self.ui_add_tax()
                    case 2: self.ui_view_tax()
                    case 3: self.ui_list_taxs()
                    case 4: self.ui_update_profile_name()
                    case 5: self.ui_update_profile_income()
                    case 6: self.ui_update_profile_deductions()
                    case 7: break
            except ValueError:
                print("Invalid input. Please choose a valid option.")

    def ui_add_tax(self):
        print("\nAdding a new tax profile:")
        name = input("  Please enter tax name: ")
        if self.db.check_profiles_name(name):
            return print(f"Profile for {name} has been exited.")
        income = float(input("  Please enter income: "))
        deductions = float(input("  Please enter deductions: "))
        tax = TaxController(name, income, deductions)
        self.db.add_profile(tax)
        print(f"Profile for {name} has been added.")

    def ui_view_tax(self):
        print("\nViewing tax profile:")
        name = input("  Please enter the name of the tax: ")
        tax = self.db.get_profile(name)
        if tax:
            print(tax)
        else:
            print("  Profile not found.")

    def ui_list_taxs(self):
        print("\nListing all taxs:")
        taxs = self.db.get_all_profiles()
        if taxs:
            for tax in taxs:
                print(tax)
        else:
            print("  No profiles found.")

    def ui_update_profile_name(self):
        print("\nUpdating tax profile name:")
        old_name = input("  Please enter the current name of the tax: ")
        if self.db.check_profiles_name(old_name) is False:
            return print("Profile not found.")
        new_name = input("  Please enter the new name: ")
        if self.db.update_profile_name(old_name, new_name):
            print(f"Profile name updated from {old_name} to {new_name}.")
        else:
            print(f"  Profile for {new_name} has been exited.")

    def ui_update_profile_income(self):
        print("\nUpdating tax profile income:")
        name = input("  Please enter the profile name: ")
        if self.db.check_profiles_name(name):
            new_income = int(input("  Please enter the new income: "))
            self.db.update_profile_income(name, new_income)
            return print(f"Profile {name} updated income to {new_income}.")
        return print("Profile not found.")

    def ui_update_profile_deductions(self):
        print("\nUpdating tax profile income:")
        name = input("  Please enter the profile name: ")
        if self.db.check_profiles_name(name):
            new_deductions = int(input("  Please enter the new deductions: "))
            self.db.update_profile_deductions(name, new_deductions)
            return print(f"Profile {name} updated deductions to {new_deductions}.")
        return print("Profile not found.")

def main():
    system = TaxCalculatorView()
    system.ui_main_menu()

if __name__ == "__main__":
    main()
