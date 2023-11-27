document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementByID('tweet-button');
    const tweetInput = document.getElementById('tweet-input');

    submitButton.addEventListener('click', function (event) {
        event.preventDefault();

        // ดึงข้อมูลจาก textarea
        const newTweetText = tweetInput.value;

        if (newTweetText) {
            // สร้างอิลิเมนต์ HTML สำหรับโพสต์ใหม่
            const postElement = document.createElement('div');
            postElement.classList.add('post');

            const postContent = document.createElement('div');
            postContent.classList.add('post-content');
            postContent.innerText = newTweetText;

            postElement.appendChild(postContent);

            // เก็บข้อมูลโพสต์ใหม่ใน localStorage
            const posts = JSON.parse(localStorage.getItem('posts')) || [];
            posts.push(newTweetText);
            localStorage.setItem('posts', JSON.stringify(posts));

            // แสดงโพสต์ใหม่
            const tweetsContainer = document.getElementById('tweets-container');
            tweetsContainer.appendChild(postElement);

            // ลบข้อความใน textarea
            tweetInput.value = '';
        }
    });

    // โหลดโพสต์จาก localStorage เมื่อหน้าโหลด
    const savedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    const tweetsContainer = document.getElementById('tweets-container');

    for (const postText of savedPosts) {
        const postElement = document.createElement('div');
        postElement.classList.add('post');

        const postContent = document.createElement('div');
        postContent.classList.add('post-content');
        postContent.innerText = postText;

        postElement.appendChild(postContent);
        tweetsContainer.appendChild(postElement);
    }
});
