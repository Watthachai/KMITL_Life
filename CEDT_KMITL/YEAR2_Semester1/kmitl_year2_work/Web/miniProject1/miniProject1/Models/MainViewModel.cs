using System.Net;

namespace miniProject1.Models
{
    public class MainViewModel
    {
        public string? RequestId { get; set; }

        public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);
    }

    public class DataModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime PostDateTime { get; set; }
        public string Address { get; set; }
        public string PhoneNumber { get; set; }
        public string Info { get; set; }
        public Boolean ReplyStatus { get; set; }
        public DateTime ReplyDateTime { get; set; }
        public string ReplyDetail { get; set; }
        public string ReplyName { get; set; }
        public string ReplyPhone { get; set; }
    }
}