//using Assessment3;
//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace Assessment3
//{
//    class Calculator
//    {
//        public int A { get; set; }
//        public int B { get; set; }
//        public int Add(int A, int B)
//        {
//            int res1 = A + B;
//            return res1;
//        }
//        public int Add(int A, int B, int C)
//        {
//            int res2 = A + B + C;
//            return res2;
//        }
//        public double Add(double A, double B)
//        {
//            double res3 = A + B;
//            return res3;
//        }
//    }
//}
//class Program
//{
//    static void Main(string[] args)
//    {
//        Calculator calc = new Calculator();

//        Console.WriteLine("Enter the values of A and B:");
//        int A = int.Parse(Console.ReadLine());
//        int B = int.Parse(Console.ReadLine());
//        int res1 = calc.Add(A, B);
//        Console.WriteLine(res1);

//        Console.WriteLine("Enter the values of A, B, and C:");
//        A = int.Parse(Console.ReadLine());
//        B = int.Parse(Console.ReadLine());
//        int C = int.Parse(Console.ReadLine());
//        int res2 = calc.Add(A, B, C);
//        Console.WriteLine("Result of Add(A, B, C): " + res2);

//        Console.WriteLine("Enter the values of A and B (double):");
//        double dA = double.Parse(Console.ReadLine());
//        double dB = double.Parse(Console.ReadLine());
//        double res3 = calc.Add(dA, dB);
//        Console.WriteLine("Result of Add(dA, dB): " + res3);
//    }
//}
