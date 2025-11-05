using System;

namespace HelloWorld
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var filepath = @"C:\\StudentTesting\\Khuong\\c#\\HelloWorld\\HelloFromC#.txt";
            string Hello = "Hello World";
            Console.WriteLine(Hello);
            File.WriteAllText(filepath, Hello);
        }
    }
}
