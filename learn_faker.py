

'''
This scripts is made by me so that i can keep tracks of 
my faker library learning by making a git 
### pip import faker
Here currently i was using the Faker 24.11.0
For any sugession Msg me in My Telegram Account:
https://t.me/RanaUniverse 🍌🍌🍌

'''


from faker import Faker
fake = Faker()


def main():
    for i in range(1,2):
        # variable = fake.name()
        # print(variable)
        # variable = fake.address()
        # print(variable, "\n")

        # variable = fake.text(5)
        # print(variable)

        # fake = Faker('it_IT')
        # for _ in range(10):
        
        print(fake.name())




if __name__ == "__main__":
    main()
    









