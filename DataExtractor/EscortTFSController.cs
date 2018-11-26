using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Microsoft.VisualStudio.Services.Common;
using Microsoft.VisualStudio.Services.Client;
using Microsoft.VisualStudio.Services.WebApi;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi.Models;

using System.Reflection;

namespace DataExtractor
{
    class EscortTFSController
    {
        internal VssBasicCredential vssBasic;
        internal Uri uri;
        public EscortTFSController()
        {
            vssBasic = new VssBasicCredential("", "5tgsajh4sbfdvhtjgyvy2i5zs4nw7xxa5h355lwenzyyrkddwdaq");
            uri = new Uri("https://vstfrdext.partners.extranet.microsoft.com:8443/Azure");
        }

        public Dictionary<string, EscortItemModel> Extract()
        {
            Wiql wiql = new Wiql()
            {
                Query = string.Format(@"SELECT * FROM WorkItems WHERE [Team Project] = 'Mooncake' AND [Work Item Type] = 'Escort Request' AND [Created Date] ='2018-11-12'")
            };
            using (WorkItemTrackingHttpClient workItemTrackingHttpClient = new WorkItemTrackingHttpClient(this.uri, this.vssBasic))
            {
                //execute the query to get the list of work items in the results
                WorkItemQueryResult workItemQueryResult = workItemTrackingHttpClient.QueryByWiqlAsync(wiql).Result;

                //create a dic to hold process result
                Dictionary<String, EscortItemModel> results = new Dictionary<string, EscortItemModel>();
                workItemQueryResult.AsOf = DateTime.Now;


                if (workItemQueryResult.WorkItems.Count() != 0)             //get fileds if query result is not empty
                {
                    //need to get the list of our work item ids and put them into an array
                    List<int> list = new List<int>();
                    foreach (var item in workItemQueryResult.WorkItems)
                    {
                        list.Add(item.Id);
                    }
                    
                    int[] arr = list.ToArray();

                    //build a list of the fields we want to see
                    string[] fields = createFieldMapper();
                    
                    //execute
                    var workItems = workItemTrackingHttpClient.GetWorkItemsAsync(arr, fields, workItemQueryResult.AsOf).Result;
                    //Console.WriteLine("Query Results: {0} items found", tickets.Count);

                    //process query data and holdem with object
                    foreach (var workItem in workItems)
                    {
                        EscortItemModel item = new EscortItemModel(workItem);
                        item.tfsObj = workItem;
                        results.Add(item.iD, item);
                    }
                }

                return results;
            }
        }
        private string[] createFieldMapper()
        {
            //get following fields from TFS
            string[] fields = new string[66];
            fields[0] = "Microsoft.VSTS.Common.ActivatedBy";
            fields[1] = "Microsoft.VSTS.Common.ActivatedDate";
            fields[2] = "System.AreaId";
            fields[3] = "System.AreaPath";
            fields[4] = "Microsoft.Azure.Incident.AssignedTeam";
            fields[5] = "System.AssignedTo";
            fields[6] = "System.AttachedFileCount";
            fields[7] = "System.AuthorizedAs";
            fields[8] = "System.AuthorizedDate";
            fields[9] = "System.BoardColumn";
            fields[10] = "System.BoardColumnDone";
            fields[11] = "System.BoardLane";
            fields[12] = "System.ChangedBy";
            fields[13] = "System.ChangedDate";
            fields[14] = "Microsoft.Azure.ClientLibrary.Version";
            fields[15] = "Microsoft.VSTS.Common.ClosedBy";
            fields[16] = "Microsoft.VSTS.Common.ClosedDate";
            fields[17] = "Microsoft.Azure.Incident.ClusterSet";
            fields[18] = "Microsoft.Azure.Deployment.Component";
            fields[19] = "Microsoft.Azure.ComponentImpacted";
            fields[20] = "System.CreatedBy";
            fields[21] = "System.CreatedDate";
            fields[22] = "System.Description";
            fields[23] = "Microsoft.Azure.Effort";
            fields[24] = "Microsoft.Azure.EscortName";
            fields[25] = "Microsoft.Azure.RequestorName";
            fields[26] = "Microsoft.Azure.Incident.EventTime";
            fields[27] = "System.ExternalLinkCount";
            fields[28] = "Microsoft.Azure.ExtMilestone";
            fields[29] = "System.History";
            fields[30] = "System.HyperLinkCount";
            fields[31] = "Microsoft.IcM.Id";
            fields[32] = "System.Id";
            fields[33] = "Microsoft.Azure.Incident.Environment";
            fields[34] = "Microsoft.Azure.Incident.Severity";
            fields[35] = "System.IterationId";
            fields[36] = "System.IterationPath";
            fields[37] = "Microsoft.RD.KeywordSearch";
            fields[38] = "Microsoft.Azure.KPI_1_Description";
            fields[39] = "Microsoft.Azure.KPI_2_Description";
            fields[40] = "System.NodeName";
            fields[41] = "Microsoft.Azure.Incident.OwnerTeam";
            fields[42] = "Microsoft.Azure.Purpose";
            fields[43] = "Microsoft.Azure.RCA.Status";
            fields[44] = "System.Reason";
            fields[45] = "System.RelatedLinkCount";
            fields[46] = "Microsoft.Azure.RequestedReleaseDate";
            fields[47] = "Microsoft.VSTS.Common.ResolvedBy";
            fields[48] = "Microsoft.VSTS.Common.ResolvedDate";
            fields[49] = "Microsoft.VSTS.Common.ResolvedReason";
            fields[50] = "Microsoft.RD.IncidentResolvedTime";
            fields[51] = "System.Rev";
            fields[52] = "System.RevisedDate";
            fields[53] = "Microsoft.VSTS.Common.Source";
            fields[54] = "Microsoft.RD.IncidentStartTime";
            fields[55] = "System.State";
            fields[56] = "Microsoft.VSTS.Common.StateChangeDate";
            fields[57] = "System.Tags";
            fields[58] = "Microsoft.Azure.Deployment.Team";
            fields[59] = "System.TeamProject";
            fields[60] = "Microsoft.Azure.ID";
            fields[61] = "TfsMigrationTool.ReflectedWorkItemId";
            fields[62] = "System.Title";
            fields[63] = "Microsoft.SRBucket.TSGID";
            fields[64] = "System.Watermark";
            fields[65] = "System.WorkItemType";
            return fields;
        }
    }
}
