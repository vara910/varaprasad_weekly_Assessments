//Operator Overloading for Complex Numbers**

using System;

public class ComplexNumber
{
    public double Real { get; set; }
    public double Imaginary { get; set; }

    public ComplexNumber(double real, double imaginary)
    {
        Real = real;
        Imaginary = imaginary;
    }

    public static ComplexNumber operator +(ComplexNumber c1, ComplexNumber c2)
    {
        return new ComplexNumber(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
    }

    public override string ToString()
    {
        return $"{Real} + {Imaginary}i";
    }
}

public class Program6
{
    public static void Main(string[] args)
    {
        ComplexNumber c1 = new ComplexNumber(1.2, 3.4);
        ComplexNumber c2 = new ComplexNumber(5.6, 7.8);
        ComplexNumber sum = c1 + c2;

        Console.WriteLine($"The sum of {c1} and {c2} is {sum}");
    }
}
