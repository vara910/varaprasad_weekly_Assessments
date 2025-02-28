

public static class CalculateAreas
{
    public static double CalculateCircleArea(double radius)
    {
        return Math.PI * Math.Pow(radius, 2);
    }

    public static double CalculateRectangleArea(double length, double width)
    {
        return length * width;
    }

    public static double CalculateTriangleArea(double baseLength, double height)
    {
        return 0.5 * baseLength * height;
    }

    public static void Main()
    {
        Console.WriteLine("Circle Area (radius 5): " + CalculateCircleArea(5));
        Console.WriteLine("Rectangle Area (length 4, width 6): " + CalculateRectangleArea(4, 6));
        Console.WriteLine("Triangle Area (base 3, height 7): " + CalculateTriangleArea(3, 7));
    }
}
