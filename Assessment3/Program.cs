//using System;

//namespace StudentApp
//{
//    class Student
//    {
//        private string? name;
//        private int rollNo;

//        public string Name
//        {
//            get { return name; }
//            set
//            {
//                if (!string.IsNullOrEmpty(value))
//                {
//                    name = value;
//                }
//                else
//                {
//                    throw new ArgumentException("Name cannot be empty");
//                }
//            }
//        }

//        public int RollNo
//        {
//            get { return rollNo; }
//            set
//            {
//                if (value >= 0)
//                {
//                    rollNo = value;
//                }
//                else
//                {
//                    throw new ArgumentException("RollNo cannot be negative");
//                }
//            }
//        }
//    }

//    class Program
//    {
//        static void Main(string[] args)
//        {

//            Console.Write("Enter student name: ");
//            string? name = Console.ReadLine();

//            if (string.IsNullOrEmpty(name))
//            {
//                Console.WriteLine("Name cannot be empty");
//                return;
//            }

//            Console.Write("Enter student roll number: ");
//            if (!int.TryParse(Console.ReadLine(), out int rollNo))
//            {
//                Console.WriteLine("Invalid input format for roll number.");
//                return;
//            }

//            if (rollNo < 0)
//            {
//                Console.WriteLine("RollNo cannot be negative");
//                return;
//            }

//            Student student = new Student
//            {
//                Name = name,
//                RollNo = rollNo
//            };

//            Console.WriteLine($"Student Name: {student.Name}");
//            Console.WriteLine($"Student RollNo: {student.RollNo}");
//        }
//    }
//}