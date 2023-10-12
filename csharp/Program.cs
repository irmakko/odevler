using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace odevv03
{
    class Program
    {
        static void changer(int index, string value)
        {
            string[] dizi = { "artık", "kod", "yazmaya", "başlamak", "istiyorum" };
            

            foreach (string i in dizi)
            {
                Console.WriteLine(i);
                if(i ==value)
                    Console.WriteLine("bu değer mevcuttur.");
            }

            dizi[index] = value;

            Console.WriteLine("Dizinin yeni hali:");
            foreach (string i in dizi)
            {
                Console.WriteLine(i);
            }

            int uzunluk = dizi.Length * 2;
            Console.WriteLine(uzunluk);

            Console.WriteLine(dizi[dizi.Length-2]);

        }


        static void Main(string[] args)
        {

            changer(3, "4");
            changer(4, "kod");
            Console.ReadLine();
        } 
    }
}



