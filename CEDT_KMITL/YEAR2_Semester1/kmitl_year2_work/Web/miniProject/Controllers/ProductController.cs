using Microsoft.AspNetCore.Mvc;
using miniProject.Models;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

namespace miniProject.Controllers
{
    public class ProductController : Controller
    {
        public IActionResult Index()
        {
            // เส้นทางไฟล์ JSON
            string jsonPath = "C:\\Users\\wattc\\OneDrive\\kmitl_year2_work\\Web\\miniProject\\data.json";

            // อ่านข้อมูลจากไฟล์ JSON
            string json = System.IO.File.ReadAllText(jsonPath);

            // แปลงข้อมูล JSON เป็น List<Item>
            List<Item> items = JsonSerializer.Deserialize<List<Item>>(json);

            // ส่งข้อมูลไปยัง View
            return View(items);
        }
    }
}
