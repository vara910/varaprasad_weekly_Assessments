//**Using Virtual Methods in Inheritance**

//Create a `Person` base class with a `GetDetails()` method. Derive `Student` and `Teacher` classes that override `GetDetails()` to display their respective properties. Call `GetDetails()` using a base class reference

public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public virtual string GetDetails()
    {
        return $"Name: {Name}, Age: {Age}";
    }
}

public class Student : Person
{
    public string School { get; set; }

    public override string GetDetails()
    {
        return $"Name: {Name}, Age: {Age}, School: {School}";
    }
}

public class Teacher : Person
{
    public string Subject { get; set; }

    public override string GetDetails()
    {
        return $"Name: {Name}, Age: {Age}, Subject: {Subject}";
    }
}

public class Program
{
    public static void Main()
    {
        Person person1 = new Student { Name = "John", Age = 20, School = "XYZ University" };
        Person person2 = new Teacher { Name = "Jane", Age = 35, Subject = "Mathematics" };

        Console.WriteLine(person1.GetDetails());
        Console.WriteLine(person2.GetDetails());
    }
}
