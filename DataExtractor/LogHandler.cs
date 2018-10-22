using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;

namespace DataExtractor
{
    public sealed class LogHandler
    {
        private CloudBlobContainer container = null;

        private static readonly Lazy<LogHandler> lazy = new Lazy<LogHandler>(() => new LogHandler());
        public static LogHandler Instance { get { return lazy.Value; } }

        private LogHandler()
        {
            string storageConnectionString = "DefaultEndpointsProtocol=https;"
                 + "AccountName=pbiprodstr"
                 + ";AccountKey=OK8i3OdFbjMZ7MMttIkDlPqxJ0q5ZkxUON2jIvL4WaSSwR3snH8hqzeomQVSLCJsdkVLw9etK1IryhIxCWDNZA=="
                 + ";EndpointSuffix=core.chinacloudapi.cn";

            CloudStorageAccount account = CloudStorageAccount.Parse(storageConnectionString);
            CloudBlobClient serviceClient = account.CreateCloudBlobClient();

            // Create container. Name must be lower case.
            Console.WriteLine("Creating container...");
            this.container = serviceClient.GetContainerReference("dataextractorlog");
            this.container.CreateIfNotExistsAsync().Wait();

            DateTime now = DateTime.Now;
            Console.WriteLine("current date is: {0:d}", now.Date);

            // write a blob to the container
            CloudBlockBlob blob = container.GetBlockBlobReference("helloworld.txt");
            blob.UploadTextAsync("Hello, World!").Wait();
            Console.Read();
        }
    }


}
