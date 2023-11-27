using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Identity.Client;
using miniProject1.Models;
using System.Diagnostics;
using System.Net;
using System.Xml;
using System.Xml.Linq;
using System.Collections.Generic;

namespace miniProject1.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private static List<DataModel> dataList = new List<DataModel>();
        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View(dataList);
        }

        [HttpPost]
        public IActionResult Index(string PostAddress, string PostName, string PostPhone, string PostDetail)
        {
            DataModel data = new DataModel
            {
                Id = dataList.Count+1,
                Address = PostAddress,
                PostDateTime = DateTime.Now,
                Name = PostName,
                PhoneNumber = PostPhone,
                Info = PostDetail,
                ReplyStatus = false,
            };
            dataList.Add(data);
            return RedirectToAction("Index");
        }

        [HttpPost]
        public IActionResult Comment(int Id, string replyName, string replyPhone, string replyDetail)
        {
            DataModel dataToUpdate = dataList.FirstOrDefault(x => x.Id == Id);

            if (dataToUpdate != null)
            {
                dataToUpdate.ReplyDateTime = DateTime.Now;
                dataToUpdate.ReplyName = replyName;
                dataToUpdate.ReplyPhone = replyPhone;
                dataToUpdate.ReplyDetail = replyDetail;
                dataToUpdate.ReplyStatus = true;
                return RedirectToAction("Index");
            }
            return RedirectToAction("Index");
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new MainViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
