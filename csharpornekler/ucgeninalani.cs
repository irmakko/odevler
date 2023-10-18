using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ucgenalanı
{
    class Program
    {
        static void Main(string[] args)
        {
            int alan, yukseklik, kenar;
            Console.WriteLine("üçgenin kenar uzunluğunu gieriniz: ");
            kenar = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("üçgenin yüksekliğini giriniz: ");
            yukseklik = Convert.ToInt32(Console.ReadLine());
            alan = kenar * yukseklik / 2;
            Console.WriteLine("üçgenin alanı: "+alan);
            Console.ReadLine();

        }
    }
}
