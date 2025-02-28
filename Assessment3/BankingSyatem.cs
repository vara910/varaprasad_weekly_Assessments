using System;

public class Bank
{
    public static double InterestRate { get; private set; }

    public static void SetInterestRate(double newRate)
    {
        InterestRate = newRate;
    }
}

public class Program10
{
    public static void Main(string[] args)
    {
        // Set the interest rate using the static method
        Bank.SetInterestRate(3.5);

        // Create two bank objects
        Bank bank1 = new Bank();
        Bank bank2 = new Bank();

        // Display the interest rate for both bank objects
        Console.WriteLine($"Bank1 Interest Rate: {Bank.InterestRate}%");
        Console.WriteLine($"Bank2 Interest Rate: {Bank.InterestRate}%");

        // Change the interest rate using the static method
        Bank.SetInterestRate(4.0);

        // Display the updated interest rate for both bank objects
        Console.WriteLine($"Updated Bank1 Interest Rate: {Bank.InterestRate}%");
        Console.WriteLine($"Updated Bank2 Interest Rate: {Bank.InterestRate}%");
    }
}
