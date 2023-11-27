// ส่วนของการเรียกใช้ตอนติดต่อเรา
var ModalCon = document.getElementById("ModalCon");
var btnCon = document.getElementById("contactUs");

if (btnCon) { // ตรวจสอบว่าอิลิเมนต์มีอยู่หรือไม่
    btnCon.onclick = function() {
        ModalCon.style.display = "block"; 
    }
}

// ส่วนของการเรียกใช้ตอนโพสต์ข้อความฝากซื้อ
var ModalPost = document.getElementById("ModalPost");
var btn = document.getElementById("myTxtbox");

if (btn) { // ตรวจสอบว่าอิลิเมนต์มีอยู่หรือไม่
    btn.onclick = function() {
        ModalPost.style.display = "block"; 
    }
}

// ส่วนของการตอบรับ
var ModalReply = document.getElementById("ModalReply");
var btnConfirm = document.querySelectorAll(".btnConfirm");
var textId = document.getElementById("Id");

btnConfirm.forEach(function (btn) {
    btn.addEventListener("click", function (event) {
        event.preventDefault();
        var id = this.getAttribute("data-id");
        var url = "./?id=" + id;
        ModalReply.style.display = "block";
        textId.value = id;
    });
});

window.onclick = function(event) {
    if (event.target == ModalCon) {
        ModalCon.style.display = "none";
    }
    if (event.target == ModalPost) {
        ModalPost.style.display = "none";
    }
    if (event.target == ModalReply) {
        ModalReply.style.display = "none";
    }
}
