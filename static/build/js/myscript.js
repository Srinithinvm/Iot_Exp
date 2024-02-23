document.getElementById("store_datas").addEventListener("submit",function(e){
    e.preventDefault();
} )


function submit_form() {
    console.log("hii..");

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };

    // Extract form data
    var storeform = document.getElementById("store_datas");
    var Id = storeform['id'].value;
    var Model = storeform['model'].value;
    var HW = storeform['hw'].value;
    var SW = storeform['sw'].value;
    var Device_Name = storeform['device_name'].value;

    // Construct the data string
    var data = "id=" + encodeURIComponent(Id) + "&model=" + encodeURIComponent(Model) + "&hw_version=" + encodeURIComponent(HW) + "&sw_version=" + encodeURIComponent(SW) + "&device_name=" + encodeURIComponent(Device_Name);

    xhttp.open("POST", "/insertdata", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhttp.send(data);

    console.log("hiii....rubu");
    console.log(Id, Model, HW, SW, Device_Name);
    window.location.replace("dash.html");
}

