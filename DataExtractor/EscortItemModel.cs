using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi.Models;
using System.Reflection;

namespace DataExtractor
{
    class EscortItemModel
    {
        string escortName;
        string escortRequestorName;
        string componentImpacted;
        string ownerTeam;
        string assignedTeam;
        DateTime? requestedReleaseDate;
        string clientLibVersion;
        string component;
        string rCAStatus;
        string incidentSeverity;
        string externalMilestone;
        string team;
        string tSGID;
        string source;
        DateTime? startTime;
        DateTime? resolvedTime;
        string effort;
        string keywordSearch;
        string closedBy;
        DateTime? closedDate;
        string resolvedReason;
        string resolvedBy;
        DateTime? resolvedDate;
        string activatedBy;
        DateTime? activatedDate;
        DateTime? stateChangeDate;
        string boardLane;
        string boardColumnDone;
        string boardColumn;
        string tags;
        string relatedLinkCount;
        string history;
        string description;
        string createdBy;
        DateTime? createdDate;
        string workItemType;
        string assignedTo;
        string reason;
        string changedBy;
        string rev;
        string watermark;
        DateTime? authorizedDate;
        string state;
        string title;
        string authorizedAs;
        string areaID;
        public String iD;
        DateTime? changedDate;
        DateTime? revisedDate;
        string areaPath;
        string nodeName;
        string attachedFileCount;
        string hyperlinkCount;
        string teamProject;
        string externalLinkCount;
        string iterationID;
        string iterationPath;
        string fFSMigrationId;
        DateTime? eventTime;
        string kPI_2_Description;
        string kPI_1_Description;
        string icMID;
        string fFSID;
        string purpose;
        string clusterSet;
        string incidentEnvironment;
        public WorkItem tfsObj;
        //Dictionary<String, dynamic> properties;

        //public EscortItemModel(List<WorkItemField> workItemFields)

        public EscortItemModel()
        {
            activatedBy = null;
            activatedDate = null;
            areaID = null;
            areaPath = null;
            assignedTeam = null;
            assignedTo = null;
            attachedFileCount = null;
            authorizedAs = null;
            authorizedDate = null;
            boardColumn = null;
            boardColumnDone = null;
            boardLane = null;
            changedBy = null;
            changedDate = null;
            clientLibVersion = null;
            closedBy = null;
            closedDate = null;
            clusterSet = null;
            component = null;
            componentImpacted = null;
            createdBy = null;
            createdDate = null;
            description = null;
            effort = null;
            escortName = null;
            escortRequestorName = null;
            eventTime = null;
            externalLinkCount = null;
            externalMilestone = null;
            history = null;
            hyperlinkCount = null;
            icMID = null;
            iD = null;
            incidentEnvironment = null;
            incidentSeverity = null;
            iterationID = null;
            iterationPath = null;
            keywordSearch = null;
            kPI_1_Description = null;
            kPI_2_Description = null;
            nodeName = null;
            ownerTeam = null;
            purpose = null;
            rCAStatus = null;
            reason = null;
            relatedLinkCount = null;
            requestedReleaseDate = null;
            resolvedBy = null;
            resolvedDate = null;
            resolvedReason = null;
            resolvedTime = null;
            rev = null;
            revisedDate = null;
            source = null;
            startTime = null;
            state = null;
            stateChangeDate = null;
            tags = null;
            team = null;
            teamProject = null;
            fFSID = null;
            fFSMigrationId = null;
            title = null;
            tSGID = null;
            watermark = null;
            workItemType = null;

            //create a dic holding all fields
            /*
            properties = new Dictionary<string, ref string>();
            properties.Add("activatedBy", ref this.activatedBy);
            properties.Add("activatedDate", this.activatedDate);
            properties.Add("areaID", this.areaID);
            properties.Add("areaPath", this.areaPath);
            properties.Add("assignedTeam", this.assignedTeam);
            properties.Add("assignedTo", this.assignedTo);
            properties.Add("attachedFileCount", this.attachedFileCount);
            properties.Add("authorizedAs", this.authorizedAs);
            properties.Add("authorizedDate", this.authorizedDate);
            properties.Add("boardColumn", this.boardColumn);
            properties.Add("boardColumnDone", this.boardColumnDone);
            properties.Add("boardLane", this.boardLane);
            properties.Add("changedBy", this.changedBy);
            properties.Add("changedDate", this.changedDate);
            properties.Add("clientLibVersion", this.clientLibVersion);
            properties.Add("closedBy", this.closedBy);
            properties.Add("closedDate", this.closedDate);
            properties.Add("clusterSet", this.clusterSet);
            properties.Add("component", this.component);
            properties.Add("componentImpacted", this.componentImpacted);
            properties.Add("createdBy", this.createdBy);
            properties.Add("createdDate", this.createdDate);
            properties.Add("description", this.description);
            properties.Add("effort", this.effort);
            properties.Add("escortName", this.escortName);
            properties.Add("escortRequestorName", this.escortRequestorName);
            properties.Add("eventTime", this.eventTime);
            properties.Add("externalLinkCount", this.externalLinkCount);
            properties.Add("externalMilestone", this.externalMilestone);
            properties.Add("history", this.history);
            properties.Add("hyperlinkCount", this.hyperlinkCount);
            properties.Add("icMID", this.icMID);
            properties.Add("iD", this.iD);
            properties.Add("incidentEnvironment", this.incidentEnvironment);
            properties.Add("incidentSeverity", this.incidentSeverity);
            properties.Add("iterationID", this.iterationID);
            properties.Add("iterationPath", this.iterationPath);
            properties.Add("keywordSearch", this.keywordSearch);
            properties.Add("kPI_1_Description", this.kPI_1_Description);
            properties.Add("kPI_2_Description", this.kPI_2_Description);
            properties.Add("nodeName", this.nodeName);
            properties.Add("ownerTeam", this.ownerTeam);
            properties.Add("purpose", this.purpose);
            properties.Add("rCAStatus", this.rCAStatus);
            properties.Add("reason", this.reason);
            properties.Add("relatedLinkCount", this.relatedLinkCount);
            properties.Add("requestedReleaseDate", this.requestedReleaseDate);
            properties.Add("resolvedBy", this.resolvedBy);
            properties.Add("resolvedDate", this.resolvedDate);
            properties.Add("resolvedReason", this.resolvedReason);
            properties.Add("resolvedTime", this.resolvedTime);
            properties.Add("rev", this.rev);
            properties.Add("revisedDate", this.revisedDate);
            properties.Add("source", this.source);
            properties.Add("startTime", this.startTime);
            properties.Add("state", this.state);
            properties.Add("stateChangeDate", this.stateChangeDate);
            properties.Add("tags", this.tags);
            properties.Add("team", this.team);
            properties.Add("teamProject", this.teamProject);
            properties.Add("fFSID", this.fFSID);
            properties.Add("fFSMigrationId", this.fFSMigrationId);
            properties.Add("title", this.title);
            properties.Add("tSGID", this.tSGID);
            properties.Add("watermark", this.watermark);
            properties.Add("workItemType", this.workItemType);*/
        }

        public EscortItemModel(WorkItem ticket) : this()
        {
            initValues(ticket);
        }
        private void initValues(WorkItem ticket)
        {
            this.iD = ticket.Id.ToString();
            
            Type T = Type.GetType("DataExtractor.EscortItemModel");
            FieldInfo[] fi = T.GetFields(BindingFlags.NonPublic | BindingFlags.Instance);

            foreach (FieldInfo looper in fi)
            {
                string tfsFieldKey = fieldMapper(looper.Name);

                // for non-existing fields, indexing will raise an KeyNotFoundException
                try
                {
                    var temp = ticket.Fields[tfsFieldKey];
                    //set the value according to datetime or string
                    if (temp.GetType() == typeof(DateTime))
                    {
                        looper.SetValue(this, temp);
                    } else
                    {
                        looper.SetValue(this, temp.ToString());
                    }
                }
                catch (KeyNotFoundException e)
                {
                    looper.SetValue(this, null);
                }
            }
        }

        private string fieldMapper(string fieldName)
        {
            string tFSFieldKey = "";

            switch (fieldName)
            {
                case "activatedBy": tFSFieldKey = "Microsoft.VSTS.Common.ActivatedBy"; break;
                case "activatedDate": tFSFieldKey = "Microsoft.VSTS.Common.ActivatedDate"; break;
                case "areaID": tFSFieldKey = "System.AreaId"; break;
                case "areaPath": tFSFieldKey = "System.AreaPath"; break;
                case "assignedTeam": tFSFieldKey = "Microsoft.Azure.Incident.AssignedTeam"; break;
                case "assignedTo": tFSFieldKey = "System.AssignedTo"; break;
                case "attachedFileCount": tFSFieldKey = "System.AttachedFileCount"; break;
                case "authorizedAs": tFSFieldKey = "System.AuthorizedAs"; break;
                case "authorizedDate": tFSFieldKey = "System.AuthorizedDate"; break;
                case "boardColumn": tFSFieldKey = "System.BoardColumn"; break;
                case "boardColumnDone": tFSFieldKey = "System.BoardColumnDone"; break;
                case "boardLane": tFSFieldKey = "System.BoardLane"; break;
                case "changedBy": tFSFieldKey = "System.ChangedBy"; break;
                case "changedDate": tFSFieldKey = "System.ChangedDate"; break;
                case "clientLibVersion": tFSFieldKey = "Microsoft.Azure.ClientLibrary.Version"; break;
                case "closedBy": tFSFieldKey = "Microsoft.VSTS.Common.ClosedBy"; break;
                case "closedDate": tFSFieldKey = "Microsoft.VSTS.Common.ClosedDate"; break;
                case "clusterSet": tFSFieldKey = "Microsoft.Azure.Incident.ClusterSet"; break;
                case "component": tFSFieldKey = "Microsoft.Azure.Deployment.Component"; break;
                case "componentImpacted": tFSFieldKey = "Microsoft.Azure.ComponentImpacted"; break;
                case "createdBy": tFSFieldKey = "System.CreatedBy"; break;
                case "createdDate": tFSFieldKey = "System.CreatedDate"; break;
                case "description": tFSFieldKey = "System.Description"; break;
                case "effort": tFSFieldKey = "Microsoft.Azure.Effort"; break;
                case "escortName": tFSFieldKey = "Microsoft.Azure.EscortName"; break;
                case "escortRequestorName": tFSFieldKey = "Microsoft.Azure.RequestorName"; break;
                case "eventTime": tFSFieldKey = "Microsoft.Azure.Incident.EventTime"; break;
                case "externalLinkCount": tFSFieldKey = "System.ExternalLinkCount"; break;
                case "externalMilestone": tFSFieldKey = "Microsoft.Azure.ExtMilestone"; break;
                case "history": tFSFieldKey = "System.History"; break;
                case "hyperlinkCount": tFSFieldKey = "System.HyperLinkCount"; break;
                case "icMID": tFSFieldKey = "Microsoft.IcM.Id"; break;
                case "iD": tFSFieldKey = "System.Id"; break;
                case "incidentEnvironment": tFSFieldKey = "Microsoft.Azure.Incident.Environment"; break;
                case "incidentSeverity": tFSFieldKey = "Microsoft.Azure.Incident.Severity"; break;
                case "iterationID": tFSFieldKey = "System.IterationId"; break;
                case "iterationPath": tFSFieldKey = "System.IterationPath"; break;
                case "keywordSearch": tFSFieldKey = "Microsoft.RD.KeywordSearch"; break;
                case "kPI_1_Description": tFSFieldKey = "Microsoft.Azure.KPI_1_Description"; break;
                case "kPI_2_Description": tFSFieldKey = "Microsoft.Azure.KPI_2_Description"; break;
                case "nodeName": tFSFieldKey = "System.NodeName"; break;
                case "ownerTeam": tFSFieldKey = "Microsoft.Azure.Incident.OwnerTeam"; break;
                case "purpose": tFSFieldKey = "Microsoft.Azure.Purpose"; break;
                case "rCAStatus": tFSFieldKey = "Microsoft.Azure.RCA.Status"; break;
                case "reason": tFSFieldKey = "System.Reason"; break;
                case "relatedLinkCount": tFSFieldKey = "System.RelatedLinkCount"; break;
                case "requestedReleaseDate": tFSFieldKey = "Microsoft.Azure.RequestedReleaseDate"; break;
                case "resolvedBy": tFSFieldKey = "Microsoft.VSTS.Common.ResolvedBy"; break;
                case "resolvedDate": tFSFieldKey = "Microsoft.VSTS.Common.ResolvedDate"; break;
                case "resolvedReason": tFSFieldKey = "Microsoft.VSTS.Common.ResolvedReason"; break;
                case "resolvedTime": tFSFieldKey = "Microsoft.RD.IncidentResolvedTime"; break;
                case "rev": tFSFieldKey = "System.Rev"; break;
                case "revisedDate": tFSFieldKey = "System.RevisedDate"; break;
                case "source": tFSFieldKey = "Microsoft.VSTS.Common.Source"; break;
                case "startTime": tFSFieldKey = "Microsoft.RD.IncidentStartTime"; break;
                case "state": tFSFieldKey = "System.State"; break;
                case "stateChangeDate": tFSFieldKey = "Microsoft.VSTS.Common.StateChangeDate"; break;
                case "tags": tFSFieldKey = "System.Tags"; break;
                case "team": tFSFieldKey = "Microsoft.Azure.Deployment.Team"; break;
                case "teamProject": tFSFieldKey = "System.TeamProject"; break;
                case "fFSID": tFSFieldKey = "Microsoft.Azure.ID"; break;
                case "fFSMigrationId": tFSFieldKey = "TfsMigrationTool.ReflectedWorkItemId"; break;
                case "title": tFSFieldKey = "System.Title"; break;
                case "tSGID": tFSFieldKey = "Microsoft.SRBucket.TSGID"; break;
                case "watermark": tFSFieldKey = "System.Watermark"; break;
                case "workItemType": tFSFieldKey = "System.WorkItemType"; break;
            }
            return tFSFieldKey;
        }





    }
}