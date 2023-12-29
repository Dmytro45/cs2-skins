function foo() {
    console.log("hello")
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone_number = document.getElementById("phone_number").value;
    var coment = document.getElementById("coment").value;
    console.log(`${name}, ${email}, ${phone_number}, ${coment}`)

    if (name !== "" && email !== "" && phone_number !== ""){
        var btn = document.getElementById("submit_form");
        btn.innerHTML = "Відправлено"
    } 
    else {
        console.log("bad")
    }
}