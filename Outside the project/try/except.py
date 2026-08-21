try:                                    # এই ব্লক 'চেষ্টা' করা হবে
    number = int(input("Enter a number: "))   # যদি এখানে ValueError হয়...
    print(f"You entered: {number}")     # ...তাহলে এই লাইন আর চলবে না
except ValueError:                      # ValueError হলে, এখানে চলে আসবে
    print("এটা কোনো বৈধ সংখ্যা না! আবার চেষ্টা করো।")   # প্রোগ্রাম crash হবে না!