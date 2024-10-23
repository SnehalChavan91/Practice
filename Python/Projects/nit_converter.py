class Converter():
    def __init__(self):
        self.conversions={
            '1':self.length_conversion,
            '2':self.weight_conversion,
            '3':self.temperature_conversion
            }
    def length_conversion(self):
        print("\n Length Conversion")
        print("1.Kilometers to miles")
        print("2.Miles to kilometers")
        choice = input("Choose conversion(1/2): ")

        if choice == "1":
            km = float(input("Enter the value in kilometers: "))
            miles = km*0.621371
            print(f"{km} kilometers ={miles} miles")
        elif choice == "2":
            miles = float(input("Enter the value in miles: "))
            km = miles/0.621371
            print(f"{miles} miles = {km}kilometers")
        else:
            print("Invalid choice !")

    def weight_conversion(self):
        print("\n Weight Conversion")
        print("1. Kilograms to Pound")
        print("2. Pound to Kilograms")
        choice = input("Choose conversion (1/2)")

        if choice =="1":
            kg = float(input("Enter the value in kilogram"))
            pounds = kg*2.20462
            print(f"{kg} kilograms = {pounds} pounds")
        elif choice =="2":
            pounds = float(input("Enter the value in pounds"))
            kg = pounds/2.20462
            print(f"{pounds} pounds = {kg} kilograms")
        else:
            print("Invalid Choice!")

    def temperature_conversion(self):
        print("\n Temperature Conversion")
        print("1.Celcius to Fahrenheit")
        print("2.Fahrenheit to Celcius")
        choice = input("Choose conversion (1/2): ")

        if choice =='1':
            celcius = float(input("Enter value in celcius: "))
            fahrenheit = (celcius * 9/5)+32
            print(f"{celcius}celcius = {fahrenheit} fahrenheit")
        elif choice =="2":
            fahrenheit = float(input("Enter the value in fahrenheit: "))
            celcius = (fahrenheit-32)*5/9
            print(f"{fahrenheit}fahrenheit={celcius}celcius")
        else:
            print("Invalid choice")

    def display_menu(self):
        print("\n Unit Converter")
        print("Select conversion type")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")

    def run(self):
        while True:
            self.display_menu()
            choice=input("Enter choice (1/2/3): ")

            if choice in self.conversions:
                self.conversions[choice]()
            else:
                print("Invalid choice! Please select valid option")

            next_conversion=input("Do you want next conversion?(yes/no): ")
            if next_conversion.lower()!='yes':
                break

if __name__=='__main__':
    convert=Converter()
    convert.run()
            
                               
                           
