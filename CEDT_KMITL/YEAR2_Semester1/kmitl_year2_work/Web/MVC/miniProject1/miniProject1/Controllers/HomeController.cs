using Microsoft.AspNetCore.Mvc;
using Microsoft.Identity.Client;
using miniProject1.Models;
using System.Diagnostics;
using System.Net;

namespace miniProject1.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Index(string tweet_input)
        {
            FlClass person = new FlClass();
            
                person.Posting = tweet_input;
                person.Address = "ตึก ECC ห้อง 801";
                person.PhoneNumber = "062524xxxx";
                person.PostDateTime = DateTime.Now;
            
            return View(person);    
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}