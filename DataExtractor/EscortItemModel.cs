using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi;
using Microsoft.TeamFoundation.WorkItemTracking.WebApi.Models;

namespace DataExtractor
{
    class EscortItemModel
    {
        string escortName;
        string escortRequestorName;
        string componentImpacted;
        string ownerTeam;
        string assignedTeam;
        DateTime requestedReleaseDate;
        string clientLibVersion;
        string component;
        string rCAStatus;
        string incidentSeverity;
        string externalMilestone;
        string team;
        string tSGID;
        string source;
        DateTime startTime;
        DateTime resolvedTime;
        string effort;
        string keywordSearch;
        string closedBy;
        DateTime closedDate;
        string resolvedReason;
        string resolvedBy;
        DateTime resolvedDate;
        string activatedBy;
        DateTime activatedDate;
        DateTime stateChangeDate;
        string boardLane;
        string boardColumnDone;
        string boardColumn;
        string tags;
        string relatedLinkCount;
        string history;
        string description;
        string createdBy;
        DateTime createdDate;
        string workItemType;
        string assignedTo;
        string reason;
        string changedBy;
        string rev;
        string watermark;
        DateTime authorizedDate;
        string state;
        string title;
        string authorizedAs;
        string areaID;
        public String iD;
        DateTime changedDate;
        DateTime revisedDate;
        string areaPath;
        string nodeName;
        string attachedFileCount;
        string hyperlinkCount;
        string teamProject;
        string externalLinkCount;
        string iterationID;
        string iterationPath;
        string fFSMigrationId;
        DateTime eventTime;
        string kPI_2_Description;
        string kPI_1_Description;
        string icMID;
        string fFSID;
        string purpose;
        string clusterSet;
        string incidentEnvironment;
        IDictionary<String, dynamic> properties;

        //public EscortItemModel(List<WorkItemField> workItemFields)
        public EscortItemModel(WorkItem ticket)
        {
            this.iD = ticket.Id.ToString();
            this.escortName = ticket.Fields["Microsoft.Azure.EscortName"].ToString();
            this.activatedBy = ticket.Fields["Microsoft.VSTS.Common.ActivatedBy"].ToString();
            this.activatedDate = (DateTime)ticket.Fields["Microsoft.VSTS.Common.ActivatedDate"];
            this.areaPath = ticket.Fields["System.AreaPath"].ToString();
            this.assignedTeam= ticket.Fields["Microsoft.Azure.Incident.AssignedTeam"].ToString();
            this.assignedTo = ticket.Fields["System.AssignedTo"].ToString();
            this.attachedFileCount = ticket.Fields["System.AttachedFileCount"].ToString();
            this.authorizedAs = ticket.Fields["System.AuthorizedAs"].ToString();
            this.authorizedDate = (DateTime)ticket.Fields["System.AuthorizedDate"];
            this.boardColumn = ticket.Fields["System.BoardColumn"].ToString();
            this.boardColumnDone = ticket.Fields["System.BoardColumnDone"].ToString();
            this.boardLane = ticket.Fields["System.BoardLane"].ToString();
            this.changedBy = ticket.Fields["System.ChangedBy"].ToString();
            this.changedDate = (DateTime)ticket.Fields["System.ChangedDate"];
            this.clientLibVersion = ticket.Fields["Microsoft.Azure.ClientLibrary.Version"].ToString();
            this.closedBy = ticket.Fields["Microsoft.VSTS.Common.ClosedBy"].ToString();
            this.closedDate = (DateTime)ticket.Fields["Microsoft.VSTS.Common.ClosedDate"];
            this.clusterSet = ticket.Fields["Microsoft.Azure.Incident.ClusterSet"].ToString();
            this.component = ticket.Fields["Microsoft.Azure.Deployment.Component"].ToString();
            this.componentImpacted = ticket.Fields["Microsoft.Azure.ComponentImpacted"].ToString();
            this.createdBy = ticket.Fields["System.CreatedBy"].ToString();
            this.createdDate = (DateTime)ticket.Fields["System.CreatedDate"];
            this.description = ticket.Fields["System.Description"].ToString();
            this.effort = ticket.Fields["Microsoft.Azure.Effort"].ToString();
            this.escortName = ticket.Fields["Microsoft.Azure.EscortName"].ToString();
            this.escortRequestorName = ticket.Fields["Microsoft.Azure.RequestorName"].ToString();
            this.eventTime = (DateTime)ticket.Fields["Microsoft.Azure.Incident.EventTime"];
            this.externalLinkCount = ticket.Fields["System.ExternalLinkCount"].ToString();
            this.externalMilestone = ticket.Fields["Microsoft.Azure.ExtMilestone"].ToString();
            this.history = ticket.Fields["System.History"].ToString();
            this.hyperlinkCount = ticket.Fields["System.HyperLinkCount"].ToString();
            this.icMID = ticket.Fields["Microsoft.IcM.Id"].ToString();
            this.iD = ticket.Fields["System.Id"].ToString();
            this.incidentEnvironment = ticket.Fields["Microsoft.Azure.Incident.Environment"].ToString();
            this.incidentSeverity = ticket.Fields["Microsoft.Azure.Incident.Severity"].ToString();
            this.iterationID = ticket.Fields["System.IterationId"].ToString();
            this.iterationPath = ticket.Fields["System.IterationPath"].ToString();
            this.keywordSearch = ticket.Fields["Microsoft.RD.KeywordSearch"].ToString();
            this.kPI_1_Description = ticket.Fields["Microsoft.Azure.KPI_1_Description"].ToString();
            this.kPI_2_Description = ticket.Fields["Microsoft.Azure.KPI_2_Description"].ToString();
            this.nodeName = ticket.Fields["System.NodeName"].ToString();
            this.ownerTeam = ticket.Fields["Microsoft.Azure.Incident.OwnerTeam"].ToString();
            this.purpose = ticket.Fields["Microsoft.Azure.Purpose"].ToString();
            this.rCAStatus = ticket.Fields["Microsoft.Azure.RCA.Status"].ToString();
            this.reason = ticket.Fields["System.Reason"].ToString();
            this.relatedLinkCount = ticket.Fields["System.RelatedLinkCount"].ToString();
            this.requestedReleaseDate = (DateTime)ticket.Fields["Microsoft.Azure.RequestedReleaseDate"];
            this.resolvedBy = ticket.Fields["Microsoft.VSTS.Common.ResolvedBy"].ToString();
            this.resolvedDate = (DateTime)ticket.Fields["Microsoft.VSTS.Common.ResolvedDate"];
            this.resolvedReason = ticket.Fields["Microsoft.VSTS.Common.ResolvedReason"].ToString();
            this.resolvedTime = (DateTime)ticket.Fields["Microsoft.RD.IncidentResolvedTime"];
            this.rev = ticket.Fields["System.Rev"].ToString();
            this.revisedDate = (DateTime)ticket.Fields["System.RevisedDate"];
            this.source = ticket.Fields["Microsoft.VSTS.Common.Source"].ToString();
            this.startTime = (DateTime)ticket.Fields["Microsoft.RD.IncidentStartTime"];
            this.state = ticket.Fields["System.State"].ToString();
            this.stateChangeDate = (DateTime)ticket.Fields["Microsoft.VSTS.Common.StateChangeDate"];
            this.tags = ticket.Fields["System.Tags"].ToString();
            this.team = ticket.Fields["Microsoft.Azure.Deployment.Team"].ToString();
            this.teamProject = ticket.Fields["System.TeamProject"].ToString();
            this.fFSID = ticket.Fields["Microsoft.Azure.ID"].ToString();
            this.fFSMigrationId = ticket.Fields["TfsMigrationTool.ReflectedWorkItemId"].ToString();
            this.title = ticket.Fields["System.Title"].ToString();
            this.tSGID = ticket.Fields["Microsoft.SRBucket.TSGID"].ToString();
            this.watermark = ticket.Fields["System.Watermark"].ToString();
            this.workItemType = ticket.Fields["System.WorkItemType"].ToString();

        }
    }



}
