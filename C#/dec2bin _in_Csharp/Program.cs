using System;

namespace dec2bin
{
    class Program
    {
        static void Main()
        {
            Console.Write("Please enter decimal number: ");
              //int.Parse konvertē "string" uz "intrger", console.readline paņem vērtību kuru mēs ievadījām kā "string"
            int dec = int.Parse(Console.ReadLine()); 
            int given_dec = dec;
            
            string result = "";
            while (dec != 0)
            {
                // a mainīgais parāda atlikumu no dalījuma, dec mainīgias ir dalījuma rezultāts
                int a = dec % 2;
                dec = dec / 2;
                result = a.ToString() + result;
            }
            Console.WriteLine("The binary number for " + given_dec + " is : " + result);
        }
    }
}