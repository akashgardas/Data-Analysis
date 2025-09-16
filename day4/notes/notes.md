=========================================================
--------------------------DAY 4--------------------------
=========================================================
# Object Oriented Programming
    - Abstract class

---------------------------------------------------------
### Practice Problems
1. Create an abstract class Shape that defines:
    An abstract method area() (no implementation).
    Create two child classes that inherit from Shape:
    Rectangle → has attributes length, breadth, and implements area().
    Circle → has attribute radius, and implements area().

2. Create a Bank Account class 

3. Create a student class to demonstrate classes and objects

4. Demonstrate exception handling

5. Inheritance: Create an Employee and Manager classes

6. Polymorphism:
    You are asked to design a simple Payment System that can handle different payment methods.
        Requirements:
            Create a base class Payment with a method pay(amount).
            Create three child classes that override the pay(amount) method:
            CashPayment → print "Paid ₹<amount> in cash"
            CardPayment → print "Paid ₹<amount> using credit/debit card"
            UPIPayment → print "Paid ₹<amount> using UPI"
        Task:
            Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
            Loop through them and call pay(1000).
            Each object should print a different message.
