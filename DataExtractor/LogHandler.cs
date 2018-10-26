using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;

namespace DataExtractor
{
    public sealed class LogHandler
    {
        private CloudBlobContainer container;

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

            // Create container
            Console.WriteLine("Creating container...");
            this.container = serviceClient.GetContainerReference("dataextractorlog");
            this.container.CreateIfNotExistsAsync().Wait();

        }

        public void writeLog(string message)
        {
            // write messag to local file
            DateTime dateLogEntry = DateTime.Now;
            String date = dateLogEntry.ToString("yyyyMMdd");
            String fileName = date + ".txt";

            String log = string.Format("{0} | {1} \r\n", dateLogEntry.ToString("o"), message);

            uploadToBlob(fileName, log);
        }






        private void uploadToBlob(string fileName, string message)
        {
            CloudAppendBlob blob = this.container.GetAppendBlobReference(fileName);
            
            //make sure the file exsits
            if (!blob.Exists())
            {
                blob.CreateOrReplace();
            }
            try {
                blob.AppendText(message);
            }
            catch (StorageException e1)
            {

                //retry after sleep
                System.Threading.Thread.Sleep(10);
                try
                {
                    blob.AppendText(message);
                }
                catch (StorageException e)
                {
                    writeToLocalFile(fileName, message + "\r\n" + e.ToString() + "\r\n");
                }
                
            }
            
        }
        private void writeToLocalFile(String fileName, String message)
        {
            FileStream logFile;
            String logFileName = @".\" + fileName;

            if (File.Exists(logFileName))
            {
                logFile = new FileStream(logFileName, FileMode.Append);
            }
            else
            {
                logFile = new FileStream(logFileName, FileMode.Create);
            }

            byte[] bdata = Encoding.Default.GetBytes(message);
            logFile.Write(bdata, 0, bdata.Length);
            logFile.Close();
        }
    }


}
