using System;

public interface IDiscountStrategy
{
    decimal ApplyDiscount(decimal totalAmount);
}

public class NoDiscount : IDiscountStrategy
{
    public decimal ApplyDiscount(decimal totalAmount)
    {
        return totalAmount;
    }
}

public class PercentageDiscount : IDiscountStrategy
{
    private readonly decimal _percentage;

    public PercentageDiscount(decimal percentage)
    {
        _percentage = percentage;
    }

    public decimal ApplyDiscount(decimal totalAmount)
    {
        return totalAmount - (totalAmount * _percentage / 100);
    }
}

public class FixedAmountDiscount : IDiscountStrategy
{
    private readonly decimal _fixedAmount;

    public FixedAmountDiscount(decimal fixedAmount)
    {
        _fixedAmount = fixedAmount;
    }

    public decimal ApplyDiscount(decimal totalAmount)
    {
        return totalAmount - _fixedAmount;
    }
}

public class ShoppingCart
{
    private IDiscountStrategy _discountStrategy;

    public void SetDiscountStrategy(IDiscountStrategy discountStrategy)
    {
        _discountStrategy = discountStrategy;
    }

    public decimal CalculateTotal(decimal totalAmount)
    {
        return _discountStrategy.ApplyDiscount(totalAmount);
    }
}

public class Program65
{
    public static void Main(string[] args)
    {
        ShoppingCart cart = new ShoppingCart();

        Console.WriteLine("Enter total amount:");
        decimal totalAmount = Convert.ToDecimal(Console.ReadLine());

        Console.WriteLine("Choose discount type: 1. No Discount 2. Percentage Discount 3. Fixed Amount Discount");
        int choice = Convert.ToInt32(Console.ReadLine());

        switch (choice)
        {
            case 1:
                cart.SetDiscountStrategy(new NoDiscount());
                break;
            case 2:
                Console.WriteLine("Enter percentage discount:");
                decimal percentage = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new PercentageDiscount(percentage));
                break;
            case 3:
                Console.WriteLine("Enter fixed amount discount:");
                decimal fixedAmount = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new FixedAmountDiscount(fixedAmount));
                break;
            default:
                Console.WriteLine("Invalid choice. No discount applied.");
                cart.SetDiscountStrategy(new NoDiscount());
                break;
        }

        decimal finalAmount = cart.CalculateTotal(totalAmount);
        Console.WriteLine($"Final amount after discount: {finalAmount}");
    }
}
