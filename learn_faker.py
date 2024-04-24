

'''
This scripts is made by me so that i can keep tracks of 
my faker library learning by making a git 
### pip import faker
Here currently i was using the Faker 24.11.0
For any sugession Msg me in My Telegram Account:
https://t.me/RanaUniverse 🍌🍌🍌

'''


from faker import Faker
from faker.providers import DynamicProvider


medical_professions_provider = DynamicProvider(
     provider_name="medical_profession",
     elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)
fake = Faker()

fake.add_provider(medical_professions_provider)
print(fake.medical_profession())






# def main():
#     for i in range(1,2):
#         print(fake.name())


# if __name__ == "__main__":
#     main()
    









