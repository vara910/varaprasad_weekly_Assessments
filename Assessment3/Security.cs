//Sealed Class in a Security System**

//Create a sealed class `SecuritySystem` that prevents inheritance. Show how sealing a class stops further extension.

using System;

sealed class SecuritySystem
{
    public void Activate()
    {
        Console.WriteLine("Security System Activated.");
    }

    public void Deactivate()
    {
        Console.WriteLine("Security System Deactivated.");
    }
}
    
class Program11
{
    static void Main(string[] args)
    {
        SecuritySystem securitySystem = new SecuritySystem();
        securitySystem.Activate();
        securitySystem.Deactivate();
    }
}

// Uncommenting the following code will result in a compilation error
// because SecuritySystem is a sealed class and cannot be inherited.
// class AdvancedSecuritySystem : SecuritySystem
// {
// }
