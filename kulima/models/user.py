from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id: str, name: str, phone: str, language: str, location: str):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.language = language
        self.location = location

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def update_profile(self, **kwargs):
        pass

class Farmer(User):
    def __init__(self, farmer_id: str, name: str, phone: str, language: str, location: str):
        super().__init__(farmer_id, name, phone, language, location)
        self.farmer_id = farmer_id

    def register(self):
        pass

    def update_profile(self, **kwargs):
        pass

class LoanOfficer(User):
    def __init__(self, officer_id: str, name: str, phone: str, language: str, location: str, bank_affiliation: str):
        super().__init__(officer_id, name, phone, language, location)
        self.officer_id = officer_id
        self.bank_affiliation = bank_affiliation

    def approve_loan(self, application_id: str):
        pass

    def contact_farmer(self, farmer_id: str):
        pass

    def register(self):
        pass

    def update_profile(self, **kwargs):
        pass

class Admin(User):
    def __init__(self, admin_id: str, name: str, phone: str, language: str, location: str, access_level: str):
        super().__init__(admin_id, name, phone, language, location)
        self.admin_id = admin_id
        self.access_level = access_level

    def manage_users(self):
        pass

    def generate_reports(self):
        pass

    def register(self):
        pass

    def update_profile(self, **kwargs):
        pass 