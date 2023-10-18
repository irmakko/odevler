using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _07
{
    class person
    {
        private string ad;
        private string soyad;
        private string cinsiyet;
        public string Ad   // property
        {
            get { return ad; }
            set { ad = value; }
        }
        public string Soyad   // property
        {
            get { return soyad; }
            set { soyad = value; }
        }
        public string Cinsiyet   // property
        {
            get { return cinsiyet; }
            set { cinsiyet = value; }
        }
       
    }
    class kimlik
    {
         

        string ad = "ırmak";
        string soyad = "koc";
        string cinsiyet = "kadın";
        static void Main(string[] args)
        {

            kimlik a = new kimlik();
            person irmak = new person();
            irmak.Ad = "ırmak";
            Console.WriteLine(irmak.Ad);
            
            person koc = new person();
            koc.Ad = "koc";
            Console.WriteLine(koc.Ad);

            person cinsiyet = new person();
            cinsiyet.Ad = "kadın";
            Console.WriteLine(cinsiyet.Ad);
            Console.ReadKey();
          
        }
    }
}



