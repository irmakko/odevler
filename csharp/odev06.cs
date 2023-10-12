using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _06
{
    class Program
    {
        static void Main(string[] args)
        {
            ucgen(5);
            ucgen(5,'-');
            
        }
        public static void ucgen(int a)
        {
            for (int i = 1; i <= a; i++)
            {
                for (int c = 0; c < i; c++)
                {
                    Console.Write("*");
                }

                Console.WriteLine();
            }
            


        }
        public static void ucgen(int a, char b)
        {
            for (int i = 1; i <= a; i++)
            {
                for (int c = 0; c < i; c++)
                {
                    Console.Write(b);
                }

                Console.WriteLine();
            }
            Console.Read();
        }
    }
}
