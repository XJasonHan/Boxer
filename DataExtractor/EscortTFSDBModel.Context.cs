﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace DataExtractor
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class AzureSREOperationEntities : DbContext
    {
        public AzureSREOperationEntities()
            : base("name=AzureSREOperationEntities")
        {
        }
    
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public virtual DbSet<EscortTFSTicketTable_Prod> EscortTFSTicketTable_Prod { get; set; }
        public virtual DbSet<EscortTFSTicketTable_staging> EscortTFSTicketTable_staging { get; set; }
    }
}