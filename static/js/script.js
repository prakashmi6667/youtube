let menuIcon = document.querySelector(".icon");
let sidebar = document.querySelector(".sidebar");
let body = document.querySelector("#mainbody")
menuIcon.onclick = function(){
    sidebar.classList.toggle("large-sidebar");
    body.classList.toggle("main-body-xl")
}


document.getElementById("likeBtn").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default link behavior
    const likeImg = document.getElementById("likeImg");
    const unlikeImg = document.getElementById("unlikeImg");

    // Toggle images for like and unlike
    likeImg.src = (likeImg.src.includes("like.png")) ? "/static/images/liked.png" : "/static/images/like.png";
    unlikeImg.src = "/static/images/unlike.png"; // Reset unlike image if clicked
});

document.getElementById("unlikeBtn").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default link behavior
    const likeImg = document.getElementById("likeImg");
    const unlikeImg = document.getElementById("unlikeImg");

    // Toggle images for like and unlike
    unlikeImg.src = (unlikeImg.src.includes("unlike.png")) ? "/static/images/unliked.png" : "/static/images/unlike.png";
    likeImg.src = "/static/images/like.png"; // Reset like image if clicked
});

async function fn_BindComments(){

   let data =  await fn_GetAsyncCall('/api/comments/');

   console.table(data)

}