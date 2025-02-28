using System;

public class Manager
{
    public string Name { get; set; }
}

public class Department
{
    public Manager Manager { get; set; }

    // Shallow Copy
    public Department ShallowCopy()
    {
        return (Department)this.MemberwiseClone();
    }

    // Deep Copy
    public Department DeepCopy()
    {
        Department clone = (Department)this.MemberwiseClone();
        clone.Manager = new Manager { Name = this.Manager.Name };
        return clone;
    }
}

public class Program7
{
    public static void Main()
    {
        // Create original Department
        Department original = new Department { Manager = new Manager { Name = "John" } };

        // Perform Shallow Copy
        Department shallowCopy = original.ShallowCopy();
        // Perform Deep Copy
        Department deepCopy = original.DeepCopy();

        // Display original and copies
        Console.WriteLine("Original Manager: " + original.Manager.Name);
        Console.WriteLine("Shallow Copy Manager: " + shallowCopy.Manager.Name);
        Console.WriteLine("Deep Copy Manager: " + deepCopy.Manager.Name);

        // Modify original Manager's name
        original.Manager.Name = "Jane";

        // Display original and copies after modification
        Console.WriteLine("\nAfter modifying original Manager's name:");
        Console.WriteLine("Original Manager: " + original.Manager.Name);
        Console.WriteLine("Shallow Copy Manager: " + shallowCopy.Manager.Name);
        Console.WriteLine("Deep Copy Manager: " + deepCopy.Manager.Name);
    }
}
