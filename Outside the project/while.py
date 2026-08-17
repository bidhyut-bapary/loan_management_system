running = True          # একটা flag/সংকেত variable, শুরুতে True

while running:           # যতক্ষণ running == True, ততক্ষণ loop চলবে
    print("Menu running...")
    answer = input("Stop? (yes/no): ")
    if answer == "yes":
        running = False   # এই লাইন চললে পরের বার loop condition false হয়ে যাবে, loop থেমে যাবে

print("Program ended.")   # loop শেষ হওয়ার পর এটা চলবে