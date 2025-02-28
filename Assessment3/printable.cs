using System;
using System.IO;

// Define the IPrintable interface
public interface IPrintable
{
    void PrintDetails();
}

// Define the ISerializable interface
public interface ISerializable
{
    void SaveToFile(string filePath);
}

// Implement both interfaces in the Report class
public class Report : IPrintable, ISerializable
{
    public string Title { get; set; }
    public string Content { get; set; }

    public void PrintDetails()
    {
        Console.WriteLine($"Title: {Title}");
        Console.WriteLine($"Content: {Content}");
    }

    public void SaveToFile(string filePath)
    {
        File.WriteAllText(filePath, $"Title: {Title}\nContent: {Content}");
    }
}

// Demonstrate multiple interface implementation
public class Program2
{
    public static void Main(string[] args)
    {
        Report report = new Report
        {
            Title = "Monthly Report",
            Content = "This is the content of the monthly report."
        };

        // Print details
        report.PrintDetails();

        // Save to file
        string filePath = "report.txt";
        report.SaveToFile(filePath);
        Console.WriteLine($"Report saved to {filePath}");
    }
}
