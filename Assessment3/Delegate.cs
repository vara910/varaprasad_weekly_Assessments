using System;

public class Button
{
    // Delegate for the OnClick event
    public delegate void ClickHandler();

    // Event based on the delegate
    public event ClickHandler OnClick;

    // Method to simulate button click
    public void Click()
    {
        // Trigger the event if there are any subscribers
        OnClick?.Invoke();
    }
}

public class Program12
{
    public static void Main(string[] args)
    {
        // Create a new button instance
        Button button = new Button();

        // Subscribe to the OnClick event
        button.OnClick += Button_OnClick;

        // Simulate button click
        button.Click();
    }

    // Event handler method
    private static void Button_OnClick()
    {
        Console.WriteLine("Button was clicked!");
    }
}
