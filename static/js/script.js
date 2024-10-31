let menuIcon = document.querySelector(".icon");
let sidebar = document.querySelector(".sidebar");
let body = document.querySelector("#mainbody")
menuIcon.onclick = function(){
    sidebar.classList.toggle("large-sidebar");
    body.classList.toggle("main-body-xl")
}