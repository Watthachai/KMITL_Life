namespace miniProject1.Models
{
    public class ErrorViewModel
    {
        public string? RequestId { get; set; }

        public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);
    }

    public class FlClass
    {
        public string Posting { get; set; }
        public string Address { get; set; }
        public string PhoneNumber { get; set; }
        public DateTime PostDateTime { get; set; }
    }

}