using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace alancevrehesaplama
{
    class Program
    {
        static void Main(string[] args)
        {
            int kisakenar, uzunkenar, alan, cevre;
            Console.WriteLine("kısa kenarı girin: ");
            kisakenar = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("uzun kenarı girin: ");
            uzunkenar = Convert.ToInt32(Console.ReadLine());
            alan = kisakenar * uzunkenar;
            cevre = (kisakenar + uzunkenar) * 2;
            Console.WriteLine("alan: "+alan);
            Console.WriteLine("cevre"+cevre);
            Console.ReadKey();
        }
    }
}
