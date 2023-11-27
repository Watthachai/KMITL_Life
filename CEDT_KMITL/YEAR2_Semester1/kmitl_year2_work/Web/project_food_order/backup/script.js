const postButton = document.getElementById("post-button");
const postText = document.getElementById("post-text");
const postContainer = document.getElementById("post-container");

postButton.addEventListener("click", function() {
    const text = postText.value;
    if (text.trim() !== "") {
        const post = document.createElement("div");
        post.className = "post";
        post.textContent = text;
        postContainer.appendChild(post);
        postText.value = "";
    }
});
