using Microsoft.AspNetCore.Mvc;
using MVCProject.Models;
using System.Diagnostics;

namespace MVCProject.Controllers
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

        public IActionResult Form01Handle(string fname, string lname, string email, string eiffelTowerHeight, string tiebreakerAnswer)
        {
            ViewBag.fname = fname;
            ViewBag.lname = lname;
            ViewBag.email = email;
            ViewBag.eiffelTowerHeight = eiffelTowerHeight;
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