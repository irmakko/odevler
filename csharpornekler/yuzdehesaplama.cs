using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace basityüzdehesaplama
{
    class Program
    {
        static void Main(string[] args)
        {
            double sayi, yuzde, sonuc;
            Console.WriteLine("sayıyı giriniz: ");
            sayi = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("yuzdeyi giriniz: ");
            yuzde = Convert.ToDouble(Console.ReadLine());
            sonuc = sayi * yuzde / 100;
            Console.WriteLine("girilen sayının % {0}'i:{1}",yuzde,sonuc);
            Console.ReadKey();
        }
    }
}
