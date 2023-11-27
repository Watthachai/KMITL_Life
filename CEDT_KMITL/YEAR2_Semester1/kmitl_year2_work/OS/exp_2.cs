using System;
using System.Threading;

namespace Lab_OS_Concurrency01
{
    class Program
    {
        static int resource = 10000;
        static void TestThread1()
        {
            Console.WriteLine("Thread# 1 i={0}", resource);
        }
        static void TestThread2()
        {
            Console.WriteLine("Thread# 2 i={0}", resource);
        }

        static void Main(string[] args)
        {
            Thread t1 = new Thread(TestThread1);
            Thread t2 = new Thread(TestThread2);
            t1.Start();
            t2.Start();
            Console.ReadKey();
        }
    }
}