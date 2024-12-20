from model.model import *

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