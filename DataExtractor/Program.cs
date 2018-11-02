using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;


namespace DataExtractor
{
    class Program
    {
        private static Random random = new Random();
        public static string RandomString(int length)
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            return new string(Enumerable.Repeat(chars, length)
              .Select(s => s[random.Next(s.Length)]).ToArray());
        }

        static void Main(string[] args)
        {
            LogHandler log = LogHandler.Instance;
            int i = 10000;

            while (i > 0)
            {
                Random random = new Random();

                String message = RandomString(random.Next(5, 10));

                log.writeLog(message);

                int randomTime = random.Next(10, 20);
                System.Threading.Thread.Sleep(randomTime);
                i = i--;
            }

        }
    }
}
