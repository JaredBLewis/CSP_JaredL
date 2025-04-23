let images = ["https://images.pexels.com/photos/46148/aircraft-jet-landing-cloud-46148.jpeg", "https://grist.org/wp-content/uploads/2015/12/plane.jpg?quality=75&strip=all", "https://airadvisor.com/Media/images/news/big/334d699ae1a52e2134f005124360ccfd.webp"]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("img").src = images[counter]
        counter +=1
    }else{
        counter = 0
        document.getElementById ("img").src = images [counter]
    }
}

function hello(){
    let name = window.prompt("What is your name?", "User")
    document.getElementById("title").innerHTML = "Hello " +name+ "!"
}
function hover(){
    document.getElementById("img").src = "https://grist.org/wp-content/uploads/2015/12/plane.jpg?quality=75&strip=all"
}
function leave(){
    document.getElementById("img").src = "https://images.pexels.com/photos/46148/aircraft-jet-landing-cloud-46148.jpeg"
}
function hidden(){
    document.getElementById("meme").style.display = "block"
}
function pop(){
    window.alert("Really don't click that!")
}
function show(){
    document.getElementById("lost").style.display = "block"
}