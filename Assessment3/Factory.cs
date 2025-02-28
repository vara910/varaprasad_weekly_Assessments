//Factory Pattern for Object Creation**

//Implement a `VehicleFactory` class that returns different vehicle objects (`Car`, `Bike`) based on an input parameter.

public interface IVehicle
{
    void Drive();
}

public class Car1 : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Driving a car.");
    }
}

public class Bike1 : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Riding a bike.");
    }
}

public static class VehicleFactory
{
    public static IVehicle GetVehicle(string vehicleType)
    {
        return vehicleType.ToLower() switch
        {
            "car" => new Car1(),
            "bike" => new Bike1(),
            _ => throw new ArgumentException("Invalid vehicle type")
        };
    }
}

public class Program34
{
    public static void Main(string[] args)
    {
        IVehicle vehicle1 = VehicleFactory.GetVehicle("car");
        vehicle1.Drive();

        IVehicle vehicle2 = VehicleFactory.GetVehicle("bike");
        vehicle2.Drive();
    }
}
