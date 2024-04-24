

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

fake = Faker()

my_word_list = [
'pie','bar','Ice','oat' ]

print(fake.sentence())
# 'Expedita at beatae voluptatibus nulla omnis.'

print(fake.sentence(ext_word_list=my_word_list))
# 'Oat beans oat Lollipop bar cheesecake.'



# def main():
#     for i in range(1,2):
#         print(fake.name())


# if __name__ == "__main__":
#     main()
    









