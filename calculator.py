from datetime import datetime
class Calculator:
    def __init__(self):
        pass
    def menu(self):
        while True:
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus")
            print("6. History")
            print("7. Time")
            print("8. Date")
            print("9. Exit")

            try:
                choice = int(input("Enter a choice :"))
            except ValueError:
                print("Enter valid option")
                continue

            if choice == 1:
                try:
                    a = float(input("Enter first number :"))
                    b = float(input("Enter second number :"))
                except:
                    print("Please enter valid number :")
                    continue
                answer =self.add(a,b)
                print(answer)

            elif choice == 2:
                try:
                    a = float(input("Enter first number :"))
                    b = float(input("Enter second number :"))
                except:
                    print("Please enter valid number :")
                    continue

                answer = self.subtraction(a,b)
                print(answer)
            
            elif choice == 3:
                try:
                    a = float(input("Enter first number :"))
                    b = float(input("Enter second number :"))
                except:
                    print("Please enter valid number :")
                    continue
                answer = self.multiplication(a,b)
                print(answer)
            
            elif choice == 4:
                try:
                    a = float(input("Enter first number :"))
                    b = float(input("Enter second number :"))
                except:
                    print("Please enter valid number :")
                    continue
                answer = self.division(a,b)
                print(answer)
            
            elif choice == 5: 
                try: 
                    a = float(input("Enter first number :"))
                    b = float(input("Enter second number :"))
                except:
                    print("Please enter valid number :")
                    continue
                answer = self.modulus(a, b)
                print(answer)
            
            elif choice == 6:
                try:
                    with open("history.txt", "r") as f:
                        print(f.read())
                except FileNotFoundError:
                     print("No history found.")

            elif choice == 7:
                print("Current Time:", datetime.now().strftime("%H:%M:%S"))

            elif choice == 8:
                print("Current Date:", datetime.now().strftime("%d-%m-%Y"))

            elif choice == 9:
                print("Calculator closed.")
                break
            else:
                print("Invalid choice! Please enter 1 to 9.")   
        
    def add(self,a,b):
            result = a + b
            if result.is_integer():
                  result = int(result)

            with open("history.txt", "a") as f:
                f.write(f"Result : {a} + {b} = {result}\n")
                f.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n")
                f.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}\n\n")
            return result
       
    def subtraction(self,a,b):
            result = a - b
            if result.is_integer():
                result = int(result)
        
            with open("history.txt", "a") as f:
                f.write(f"Result : {a} - {b} = {result}\n")
                f.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n")
                f.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}\n\n")
            return result
    

    def multiplication(self,a,b):
            result = a * b
            if result.is_integer():
                result = int(result)

            with open("history.txt", "a") as f:
                f.write(f"Result : {a} * {b} = {result}\n")
                f.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n")
                f.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}\n\n")
            return result
    
    
    def division(self,a,b):
            if b != 0:
                result = a / b  
            else:
                return "Cannot divide by zero"
            
            if  result.is_integer():
                result = int(result) 

            with open("history.txt", "a") as f:
                f.write(f"Result : {a} / {b} = {result}\n")
                f.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n")
                f.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}\n\n")
            return result
            
    def modulus(self,a,b):
        if b != 0:
            result = a % b  
        else:
            return "Cannot divide by zero"
            
        if  result.is_integer():
            result = int(result) 
            
        with open("history.txt", "a") as f:
            f.write(f"Result : {a} % {b} = {result}\n\n")
            f.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n")
            f.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}\n\n") 
        return result
    

c = Calculator()
c.menu()
         
        


