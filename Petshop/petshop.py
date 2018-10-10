import random


# Data containing all the pets, first index in each list is stock, second index is the price
pets = { 'dog': {'chihuahua':[0,1000], 'labrador': [1,2000], 'bulldog': [2,3000]}, 'cat' : {'persian': [1,800], 'siamese': [2,1200], 'russian':[4,2000] }, 'misc': {}}


class PetShop:

    def buy(self, animal):
        if animal == 'dog':
            breed = input("What breed would you like to buy?\n")
            if breed not in pets['dog']:
                "Breed is unavailable.\n"
            else:
                amount = int(input("How much would you like to buy?"))
                if pets['dog'][breed][0] == 0 or pets['dog'][breed][0] < amount:
                    print("Insufficient stock.\n")
                else:
                    paid = int(input("How much money do you have on you?"))
                    if paid < pets['dog'][breed][1]:
                        print("Insufficient funds.\n")
                    else:
                        print("You have successfully purchased a {} {}".format(breed,animal))
                        pets['dog'][breed][0] = pets['dog'][breed][0] - amount
                        if paid > pets['dog'][breed][1]:
                            print("Your change is ${}.".format(paid - pets['dog'][breed][1]))
                        print("We have {} {} {} remaining.".format(pets['dog'][breed][0], breed, animal))
        elif animal == 'cat':
            breed = input("What breed would you like to buy?\n")
            if breed not in pets['cat']:
                "Breed is unavailable.\n"
            else:
                amount = int(input("How much would you like to buy?"))
                if pets['cat'][breed][0] == 0 or pets['cat'][breed][0] < amount:
                    print("Insufficient stock.\n")
                else:
                    paid = int(input("How much money do you have on you?"))
                    if paid < pets['cat'][breed][1]:
                        print("Insufficient funds.\n")
                    else:
                        print("You have successfully purchased a {} {}".format(breed,animal))
                        pets['cat'][breed][0] = pets['cat'][breed][0] - amount
                        if paid > pets['cat'][breed][1]:
                            print("Your change is ${}.".format(paid - pets['cat'][breed][1]))
                        print("We have {} {} {} remaining.".format(pets['cat'][breed][0], breed, animal))
        else:
            print("We do not have that animal.")

    def sell(self, animal):
        status = False
        price = ''
        for i in pets:
            if animal in pets[i]:
                status = True
                price = pets[i][animal][1]
                pets[i][animal][0] = pets[i][animal][0] + 1



        if status:
            print("You have successfully sold your {} for {}.".format(animal,price))

        else:
            randomPrice = random.randint(100,6000)
            print("We have no idea what that is, but we're guessing it's worth about {}".format(randomPrice))
            decision = input("Do you agree on the price? (y/n)\n")
            if decision == 'y':
                print("You have sold {} for {}.".format(animal, randomPrice))
                pets['misc'][animal] = [1, randomPrice]
            else:
                print("Cool, take care.")

    def view(self):
        for i in pets:
            for j in pets[i]:
                print(j)

    def purge(self):
        pets = {}
        print("Congratulations you monster.")
    def actions(self):
        print("Welcome to the SfQf Cats and Dogs Pet Store. What would you like to do today?(input the number)")
        action = input("1.Buy\n2.Sell\n3.View\n4.Exit\n5.Purge")
        if action == '1':
            animal = input("What animal would you like to buy?\n")
            if animal not in pets:
                print("We don't have that animal here.")
                self.actions()
            else:
                self.buy(animal)
                self.actions()
        elif action == '2':
            animal = input("What animal would you like to sell?\n")
            self.sell(animal)
            self.actions()
        elif action == '3':
            print("Here are all the animals we have here:")
            self.view()
            self.actions()
        elif action == '4':
            print("Come back soon!")
        elif action == '5':
            decision = input ("This will kill all the animals. Are you sure?(y/n)\n")
            if decision == 'y':
                self.purge()
                self.action(self)
            else:
                print("Good call.")
                self.action(self)
        else:
            print("Invalid action, try again.")
            self.actions()



def main():
    petshop = PetShop()
    petshop.actions()

main()
