using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _005
{
    class Program
    {
        static void Main(string[] args)
        {
            int notu;
            notu = Convert.ToInt32(Console.ReadLine());
            if (notu >= 90 && (notu <= 100))
            {
                Console.WriteLine("pekiyi");
            }

            else if (notu >= 75 && (notu < 90))
            {
                Console.WriteLine("iyi");
            }

            else if (notu >= 65 && (notu < 75))
            {
                Console.WriteLine("ORTA");
            }


            else if (notu >= 45 && (notu < 60))
            {
                Console.WriteLine("kötü");
            }

            else if (notu < 45)
            {
                Console.WriteLine("kaldı");
            }

            else
            {
                Console.WriteLine("NOT GİRİN!");
            }

            Console.ReadKey();

        }

       
    }
}
