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
        static void Main(string[] args)
        {
            string storageConnectionString = "DefaultEndpointsProtocol=https;"
                + "AccountName=pbiprodstr"
                + ";AccountKey=OK8i3OdFbjMZ7MMttIkDlPqxJ0q5ZkxUON2jIvL4WaSSwR3snH8hqzeomQVSLCJsdkVLw9etK1IryhIxCWDNZA=="
                + ";EndpointSuffix=core.chinacloudapi.cn";

            CloudStorageAccount account = CloudStorageAccount.Parse(storageConnectionString);
            CloudBlobClient serviceClient = account.CreateCloudBlobClient();

            // Create container. Name must be lower case.
            Console.WriteLine("Creating container...");
            var container = serviceClient.GetContainerReference("mycontainer");
            container.CreateIfNotExistsAsync().Wait();

            // write a blob to the container
            CloudBlockBlob blob = container.GetBlockBlobReference("helloworld.txt");
            blob.UploadTextAsync("Hello, World!").Wait();
            Console.Read();
        }
    }
}
