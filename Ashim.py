import string
import re
from datetime import datetime
import Saving

add_price = 0
charges = 0
order = []
order_value = ''


class menu:
    def __init__(self):
        self.saved_data = []
        self.foods = [{1: ("Noodles", 2)}, {2: ("Sandwich", 4)}, {3: ("Dumpling", 6)}, {4: ("Muffins", 8)},
                 {5: ("Pasta", 10)},
                 {6: ("Pizza", 20)}]
        self.Drinks = [{1: ("Coffee", 2)}, {2: ("Colddrink", 4)}, {3: ("Shake", 6)}]

    def main(self):
        print("\n\n**********************************************")
        print("Welcome to Online Ordering application of Oho")
        print("If your new to this press 1 to signup")
        print("For registered users press 2 to signin")
        print("Press 3 to quit the application")
        choice = input("Please choose an option from 1-3:")
        if choice == "1":
            self.signup()
        elif choice == "2":
            self.signin()
        elif choice == "3":
            pass
        else:
            print("Invalid! Please select number from 1-3 only")
            self.main()

    def signup(self):
        success = False
        while not success:
            print("\nPlease enter the details for signup")
            fullname = input("Enter Your Fullname:")
            Date_of_birth = input("Enter Your Date Of Birth DD/MM/YY:")
            Contact = input("Enter Your Contact Number:")
            Password = input("Create a new password:")
            Confirm_passw = input("Confirm the password:")

            check_one = check.check_dob(self,Date_of_birth)
            check_two = check.check_contact(self,Contact)
            check_three = check.check_psw(self,Password, Confirm_passw)
            check_error = check_one + check_two + check_three
            if check_error != 0:
                success = False

            else:
                success = True
                print("you are registered")
                # save user data in list in the dictionary form
                user = {"fullname": fullname, "DOB": Date_of_birth, "Contact": Contact, "Password": Password}
                self.saved_data.append(user)
                menu.signin(self)

        return success

    def signin(self):
        attempt = 0
        print("\nWelcome to the login page")
        print("\nYou can only try 3 time to sign in!")
        while attempt <= 2:
            username = input("Please enter your user id/ mobile number:")
            password = input("Please enter your password:")
            for user_data in self.saved_data:
                if len(username) == 0 and len(password) == 0:
                    print("You must enter the value in input box.")

                elif user_data["Contact"] != username or user_data["Password"] != password:
                    print("Your username or password doesn't match.PLease Try again")
                    attempt += 1
                    if attempt == 3:
                        print("Print make sure you have signed up or not")
                        self.main()
                        break
                else:
                    print("You have successfully logged in.")
                    attempt += 4
                    self.after_signin()

    def after_signin(self):
        while True:
            print('Please Enter 2.1 to start ordering')
            print('Please Enter 2.2 to Print Statistics')
            print('Please Enter 2.3 to logout')
            after_input = input("Please enter the choice form option to proceed:")
            if len(after_input) == 0:
                print("Please enter either 2.1,2.2,2.3 to proceed.")
            elif after_input == '2.1':
                self.mainmenu()
                break
            elif after_input == '2.2':
                stats.statistics(self)
                break
            elif after_input == '2.3':
                logout = input("Would you like to logout (Y/N):")
                if logout == "N":
                    continue
                elif logout == "Y":
                    self.main()
                    break
                else:
                    print("\nPlease choose the option")
            else:
                print("\nPlease choice from the above mentioned table.")

    def mainmenu(self):
        while True:
            print("\nPress 1 to dine in")
            print("Press 2 to order online")
            print("Press 3 to go to login page")

            option = (input("Please choose an option from 1-3:"))
            if option == '1':
                print('Dine in')
                global order_value
                order_value = 'Dine in'
                self.menus()
                break
            elif option == '2':
                self.online_options()
                break
            elif option == '3':
                self.signin()
                break
            else:
                print("\nPlease enter the option between 1-3")

    def online_options(self):
        while True:
            print("\nEnter 1 for self pick")
            print("Enter 2 for home delivery")
            print("Enter 3 to go to previous menu")
            selected = input("Please enter the option from 1-3:")
            if selected == '1':
                global order_value
                order_value = 'Selfpick'
                self.menus()
                # menus()
                break
            elif selected == '2':
                order_value = "Home Delivery"
                self.menus()
            elif selected == '3':
                self.mainmenu()
            else:
                print('\nInvalid choice. please choose from 1-3')

    def menus(self):
        print("\n\nEnter 1  for Noodles   Price AUD 2 ")
        print("Enter 2  for Sandwich  Price AUD 4")
        print("Enter 3  for Dumpling  Price AUD 6")
        print("Enter 4  for Muffins   Price AUD 8 ")
        print("Enter 5  for Pasta     Price AUD 10")
        print("Enter 6  for Pizza     Price AUD 20")
        if order_value == "Dine in":
            print("Enter 7  for Drink Menu")
            while True:
                menus_choice = input("Enter the choice from 1-7:")
                if len(menus_choice) == 0:
                    print('\nInvalid choice! Choose from 1-7.')
                elif int(menus_choice) > 7:
                    print("\nPlease choose option from 1-7 only!")
                elif menus_choice == '7':
                    self.drink_menu()
                    break
                else:
                    choice_int = int(menus_choice)
                    extract = self.foods[choice_int - 1]
                    for i in extract:
                        extracted = extract[i]
                        order.append(extracted)
        else:
            print("Enter 7 to checkout ")
            while True:
                menus_choice = input("Enter the choice from 1-7:")
                if len(menus_choice) == 0:
                    print('\nInvalid choice! Choose from 1-7.')
                elif int(menus_choice) > 7:
                    print("\nPlease choose option from 1-7 only!")
                elif menus_choice == '7':
                    if len(order) > 0:
                        cal=calculate(self)
                        cal.calculationn()
                        break
                    else:
                        print("\nPlease order something before checkout")
                else:
                    choice_int = int(menus_choice)
                    extract = self.foods[choice_int - 1]
                    for i in extract:
                        extracted = extract[i]
                        order.append(extracted)

    def drink_menu(self):
        print('\n\nEnter 1  for Coffee      Price AUD 2 ')
        print('Enter 2  for Colddrink   Price AUD 4 ')
        print('Enter 3  for Shake      Price AUD 6 ')
        print('Enter 4 to checkout ')
        while True:
            drink_input = input("Enter the choice from 1-4:")
            if len(drink_input) == 0:
                print("\nInvalid choice. Please choose from 1-4")
            elif int(drink_input) > 4:
                print("\nEnter the choice from 1-4 only")
            elif drink_input == '4':
                cal=calculate(self)
                cal.calculationn()
            else:
                int_input = int(drink_input)
                drink_extract = self.Drinks[int_input - 1]
                for i in drink_extract:
                    print(i)
                    drink_extracted = drink_extract[i]
                    order.append(drink_extracted)




# Function for checking the age of the user
class check:
    def check_dob(self,DoB):
        if len(DoB) == 8:
            DoB = datetime.strptime(DoB, '%d/%m/%y')
        elif len(DoB) == 10:
            DoB = datetime.strptime(DoB, '%d/%m/%Y')

        currentday = datetime.today()

        age = currentday.year - DoB.year - ((currentday.month, currentday.day) < (DoB.month, DoB.day))
        # Checking for the age of the user***
        if age < 21:
            print("You must be atleast 21 to register. Please try again.")
            return +1
        else:
            return 0

    def check_contact(self,Contact):
        if len(Contact) != 10 or not Contact.startswith('0') or not Contact.isdigit():
            print("checkloss")
            print("Please enter the number starting with 0 and must have 10 digits.")
            return +1
        else:
            return +0

    def check_psw(self,p1, p2):
        special_symbols = list(string.punctuation)
        if not any(i in p1 for i in special_symbols) or not p1[-1].isdigit():
            print(
                "Your password is invalid. The Password must initiate with alphabets followed by either one of @, & and ending with numeric.  Please try again.")
            return +1
        elif p1 != p2:
            print("Your password doesn't match. Confirmation password must be same as initially entered password.")
            return +1
        else:
            return +0

    def check_datetime(self,date, time):
        pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
        pattern_1 = re.compile(r'\d{2}/\d{2}/\d{2}')
        a = 0
        if pattern.match(date) or pattern_1.match(date):
            a += 1
        else:
            print("The date format doesn't matched")
        time_format = re.compile(r'\d{2}:\d{2}')
        if time_format.match(time):
            a += 1
        else:
            print("Please enter the correct format of time.")
        return a
class calculate:
    def __init__(self,menu):
        self.col_width = 10
        self.col_widthsec = 15
        self.menu_ob=menu
    def calculationn(self):
        global charges
        global order_value
        if order_value == 'Dine in':
            success = False
            while not success:
                Num_person = input("Enter the number you will be there to dine with:")
                Date_visit = input('Enter the date of your visit(DD/MM/YYYY):')
                time_visit = input('Enter the time of your visit (HH:MM):')
                if len(Num_person) == 0:
                    print("Please enter the no. of person to dine")
                    continue
                datetime_func = check.check_datetime(self,Date_visit, time_visit)
                if datetime_func != 2:
                    continue
                success = True
            self.billing()
            charge = add_price * 15 / 100
            charges = charge + add_price
            print('Additional Charges')
            print("\tDescription\t\t\tCharge\tAmount(AUD)")
            print("\tService Charge\t\t15%", "\t\t", charge)
            print("\n\t\t\t\t\t\t\t\tTotal(AUD)")
            print("\t\t\t\t\t\t\t\t\t", add_price + charge)
            self.checkout()


        elif order_value == 'Selfpick':
            charge = 0
            while True:
                date_pick = input("Enter the date of pickup:")
                time_pick = input("Enter the time of pickup:")
                person_name = input("Enter the name of person picking up:")
                time_date = check.check_datetime(self,date_pick, time_pick)
                if time_date != 2:
                    continue
                if len(person_name) == 0:
                    print("Please enter the name of person picking up")
                    continue
                break
            print('Selfpick')
            calculate.billing(self)
            charges = 0 + add_price
            print('Additional Charges')
            print("\tDescription\t\t\tCharge\tAmount(AUD)")
            print("\tService Charge\t\t15%", "\t\t", charge)
            print("\n\t\t\t\t\t\t\t\tTotal(AUD)")
            print("\t\t\t\t\t\t\t\t\t", add_price)
            calculate.checkout(self)
        elif order_value == 'Home Delivery':
            while True:
                date_delivery = input("Please enter the date of delivery:")
                time_delivery = input("Please enter the time of delivery:")
                distance_input = input("Please enter the distance from restaurant in kms:")
                date_time = check.check_datetime(self,date_delivery, time_delivery)
                if date_time != 2:
                    continue

                if len(distance_input) > 0:
                    int_distance = int(distance_input)
                    if int_distance > 15:
                        print(
                            "Sorry home delivery is not available for more than 15.\nHowever You can select for the self pick instead.")
                        print("Enter 1 to self pick instead")
                        print("Enter 2 to go to mainmenu")
                        second_option = input("Please enter your choice:")
                        if second_option == '1':
                            order_value = 'Selfpick'
                            calculate.calculationn(self)
                            break
                    elif int_distance > 10 or int_distance == 15:
                        charge = 18
                        calculate.billing(self)
                        charges = charge + add_price
                        print('Additional Charges')
                        print("\tDescription\t\t\tCharge\tAmount(AUD)")
                        print("\tService Charge\t\t", "\t\t", 18, charge)
                        print("\n\t\t\t\t\t\t\t\tTotal(AUD)")
                        print("\t\t\t\t\t\t\t\t\t", add_price + charge)
                        calculate.checkout(self)
                        break
                    elif int_distance > 5 or int_distance == 10:
                        charge = 10
                        print("Home delivery")
                        calculate.billing(self)
                        charges = charge + add_price
                        print('Additional Charges')
                        print("\tDescription\t\t\tCharge\tAmount(AUD)")
                        print("\tService Charge\t\t", 10, "\t\t", charge)
                        print("\n\t\t\t\t\t\t\t\tTotal(AUD)")
                        print("\t\t\t\t\t\t\t\t\t", add_price + charge)
                        calculate.checkout(self)
                        break
                    elif int_distance > 0 or int_distance == 5:
                        charge = 5
                        calculate.billing(self)
                        charges = add_price + charge
                        print('Additional Charges')
                        print("\tDescription\t\t\tCharge\tAmount(AUD)")
                        print("\tService Charge\t\t", 5, "\t\t", charge)
                        print("\n\t\t\t\t\t\t\t\tTotal(AUD)")
                        print("\t\t\t\t\t\t\t\t\t", add_price + charge)
                        calculate.checkout(self)
                        break
                else:
                    print("You need to provide distance before proceeding to payment")

    def billing(self):
        loop = 0
        global add_price
        print("\n********************************************")
        print('\n', 'No.'.ljust(self.col_width), 'Item'.ljust(self.col_width), 'Price'.ljust(self.col_width),
              'Amount(AUD)'.ljust(self.col_width))
        for Item, Price in order:
            print(str(loop).ljust(self.col_width), str(Item).ljust(self.col_width), str(Price).ljust(self.col_widthsec),
                  str(Price).ljust(self.col_width))
            add_price += Price
            loop += 1

    def checkout(self):
        print("Enter Y/Yes to proceed with payment")
        print("Enter N/NO to cancel the order")
        while True:
            checkout_input = input("Enter yes or no to proceed:")
            print(checkout_input)
            if checkout_input == 'Y' or checkout_input == 'yes':
                if order_value == 'Selfpicking' or order_value == 'Dine in':
                    print("\nThank You for entering the details, Your booking is confirmed.")
                else:
                    print("\nThank You for your order, Your order has been confirmed.")
                self.ifyes()
                break
            elif checkout_input == 'N' or checkout_input == 'no':
                print("\nOops Your have cancelled the order")
                self.ifno()
                break
            else:
                print('\nPlease enter a valid option')

    def ifyes(self):
        print(charges)
        print(order_value)
        Saving.insert(order, order_value, charges)
        order.clear()
        self.menu_ob.after_signin()

    def ifno(self):
        print('\nTo reorder the food 1')
        print('To quit the application press 2')
        no_input = input("Enter 1 or 2 to proceed:")
        if no_input == '1':
            self.menu_ob.menus()
        elif no_input == '2':
            self.menu_ob.mainmenu()
        else:
            print('Invalid option please enter 1 or 2 to proceed.')

class stats:
    def statistics(self):
        print("Enter the Option to Print the statistics.")
        print("1\t-\tAll Dine in Orders.")
        print("2\t-\tAll Pick up Orders.")
        print("3\t-\tAll Deliveries")
        print("4\t-\tAll Orders (Ascending Order).")
        print("5\t-\tTota1"
              "l Amount Spend on all orders.")
        print("6\t-\tTo go to previous menu")
        while True:
            stats_inp = input("Please enter your options:")
            if len(stats_inp) == 0:
                print("Please enter the options from 1-6")
            elif stats_inp == '1':
                Saving.load('Dine in')
            elif stats_inp == '2':
                Saving.load('Selfpick')
            elif stats_inp == '3':
                Saving.load('Home Delivery')
            elif stats_inp == '4':
                Saving.kalls('all')
            elif stats_inp == '5':
                Saving.whole('whole')
            elif stats_inp == '6':
                menu.after_signin(self)
            else:
                print('Please enter option from 1-6')



if __name__ == "__main__":
    menue=menu()
    menue.main()
