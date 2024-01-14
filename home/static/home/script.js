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

        var formData = new FormData();
        formData.append("name", name);
        formData.append("email", email);
        formData.append("phone_number", phone_number);
        formData.append("coment", coment);

        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.status == 200) {
                console.log("Дані форми були успішно відправлені.")
            }                
        }
        xmlHttp.open("POST", "/order-form", true);
        xmlHttp.send(formData);

    } 
    else {
        console.log("bad")
    }
}