start = int(input("Enter a number to start countdown: "))

while start >= 0:
    print(start)
    start -= 1

# print("Time's up!")



n = int(input("Enter the number of Fibonacci terms you want: "))
a, b = 0, 1
count = 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1




while True:
    user_input = input("Enter a word to check if it's a palindrome (or type 'exit' to quit): ").lower()
    
    if user_input == 'exit':
        break
    
    # Check if the string is equal to its reverse
    if user_input == user_input[::-1]:
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")



pin = 1234
pin_attempt = 3
balance = 2000
while pin_attempt > 0 :
  n = int(input("Enter a pin number :"))
  if n == pin:
    print("pin is corrected ")
    while True:
      print("\Atm Menu :")
      print("1. Check Balance")
      print("2. Exit")
      choice = int(input("Enter the choice :"))
      if choice == 1:
        print(f"Balance ${balance}")
      elif choice == 2 :
        print("goodbye")
    break
  else:
    print("invalid  choice")
    break

else:
  pin_attempt -=1
  print(f"invalid choice. you have{pin_attempt} left. ")
  if pin_attempt == 0 :
    print("your account is locked")















