using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi.Models;


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
            EscortTFSController c = new EscortTFSController();
            Dictionary<string, EscortItemModel> re = c.Extract();
            foreach (string key in re.Keys)
            {
                bool temp = re[key].Equals(re[key]);
            }
        }
    }
}
