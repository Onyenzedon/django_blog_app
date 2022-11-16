

// // var comment_btn = document.getElementById(`comment-btn-{{post.id}}`)
var comment_btn = document.getElementsByClassName("comment-button");
var comment_form = document.getElementsByClassName("comment-form");
var section_div = document.getElementById("section-div");
var post_title = document.getElementById("post-title")

console.log(comment_form.length)

// for (i = 0; i < comment_btn.length;) {
    //     comment_btn[i].addEventListener('click', function() {
        //             comment_form[j].classList.toggle("d-none"); // Adding or removing bootstrap class "d-none"
        //             i++;
        //         })
        // } 
        
// window.onload(() => {
//     setInterval(() => {
// console.log(section_div.innerText);
// section_div.classList.toggle("bg-dark")
// }, 2000);
// })

// window.onload = () => {
//     setInterval(()=>{
//         section_div.classList.toggle("bg-dark")
//         section_div.classList.toggle("text-white")
//         post_title.classList.toggle("text-white")
//         post_title.classList.toggle("text-dark")
//     },3000)
}