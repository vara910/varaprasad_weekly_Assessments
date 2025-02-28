using System;

public sealed class ConfigurationManager
{
    private static readonly Lazy<ConfigurationManager> instance = new Lazy<ConfigurationManager>(() => new ConfigurationManager());

    // Private constructor to prevent instantiation from outside
    private ConfigurationManager()
    {
    }

    public static ConfigurationManager Instance
    {
        get
        {
            return instance.Value;
        }
    }

    // Example method to demonstrate functionality
    public void DisplayConfiguration()
    {
        Console.WriteLine("Configuration settings displayed.");
    }
}

class Program445
{
    static void Main(string[] args)
    {
        // Access the singleton instance and call a method
        ConfigurationManager configManager = ConfigurationManager.Instance;
        configManager.DisplayConfiguration();
    }
}
