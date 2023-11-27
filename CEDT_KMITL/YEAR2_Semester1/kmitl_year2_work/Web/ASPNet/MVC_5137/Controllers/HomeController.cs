using Microsoft.AspNetCore.Mvc;
using MVC_5137.Models;
using System.Diagnostics;

namespace MVC_5137.Controllers
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

        public IActionResult Privacy()
        {
            return View();
        }

        public IActionResult FormHandle(string fname, string lname, string email, string eifel_height, string tiebreakerAnswer)
        {
            ViewBag.fname = fname;
            ViewBag.lname = lname;
            ViewBag.email = email;
            ViewBag.eifel_height = ": Anster = " + eifel_height + " ft";
            ViewBag.tiebreakerAnswer = tiebreakerAnswer;
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}