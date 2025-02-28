//**Method Overriding for a Vehicle System**

//Create a base class `Vehicle` with a method `Start()`. Override it in `Car` and `Bike` classes to provide specific implementations. Use the `override` keyword and demonstrate polymorphism.

public class Vehicle
{
    public virtual void Start()
    {
        Console.WriteLine("Vehicle is starting.");
    }
}

public class Car : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Car is starting with a roar.");
    }
}

public class Bike : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Bike is starting with a vroom.");
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Vehicle myCar = new Car();
        Vehicle myBike = new Bike();

        myCar.Start(); // Output: Car is starting with a roar.
        myBike.Start(); // Output: Bike is starting with a vroom.
    }
}
