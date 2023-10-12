using System;
using System.Collections.Generic;

namespace _04
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> tek = new List<int>();
            List<int> cift = new List<int>();
            for (int i=0;  i<=10; i++)
            {
                if(i %2==0)
                {
                    cift.Add(i);
                }
                else
                {
                    tek.Add(i);
                }
            }
            foreach(int sayilar in tek)
            {
                Console.WriteLine(sayilar);
            }
            foreach (int sayilar in cift)
            {
                Console.WriteLine(sayilar);
            }

            Console.ReadLine();

        }
    }
}
