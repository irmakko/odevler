using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace orn
{
    class Program
    {


        static void hello(string fname)
        {

            Console.WriteLine("merhaba "+fname);
        }
        static void hello(string fname,string sname)
        {

            Console.WriteLine("merhaba"+" "+fname+" "+sname);
        }
        static void hello(string a,string fname, string sname, int yas)
        {
            Console.WriteLine(a+fname + sname + yas);

        }
        static void Main(string[] args)
        {
            hello("merhaba \n", "ırmak \n", "koc \n",16);
            hello("ırmak","koc");

            Console.ReadLine();
        }
    }
}
