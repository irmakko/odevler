using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace odev08
{
    class Person
    {
        private string ad;
        private string soyad;
        private int yas;

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
        public int Yas   // property
        {
            get { return yas; }
            set { yas = value; }
        }
        class Program
        {
            static void Main(string[] args)
            {

                Person[] Person = new Person[5];
                string[] bilgi = new string[5];

                bilgi[0] = "ırmak,koç,16";
                bilgi[1] = "gizem,koç,17";
                bilgi[2] = "gülsüm,sayım,19";
                bilgi[3] = "zehra,sayım,16";
                bilgi[4] = "elizan,koç,1";
                void Splitter (int index)
                {
                    var myValues = bilgi[index].Split(',');
                    Person[index]= new Person 
                    { 
                    Ad=myValues[0],
                    Soyad=myValues[1],
                    Yas= int.Parse(myValues[2])
                    };
                }
                for(int i=0; i<bilgi.Length; i++)
                {
                    Splitter(i);
                }



                foreach (var i in Person)
                {
                    Console.WriteLine($"Ad: {i.Ad} , Soyad: {i.Soyad}, Yas: {i.Yas}");
                }

                Console.ReadKey();
            }



        }

    }
}
