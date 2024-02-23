function del(id) {
    let name = "arigato";
    console.log("hii", id);
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
            refresh();
        }
    };

    xhttp.open("POST", "/deletedata", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhttp.send("_id=" + id + "&Name=" + name);
    console.log("done");
}

function refresh() {
    var xhttp = new XMLHttpRequest();
    var row_div = document.getElementById("row");
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let data = this.response;
            let a = JSON.parse(data);
            var dataHTMLformat = '';
            a.forEach(function(item) {
                dataHTMLformat += '<div class="animated flipIny col-lg-3 col-md-3 col-sm-6 "> <div class="tile-stats" style="height:200px"><div class="icon"><i class="fa fa-caret-square-o-right"></i></div> <div class="count">' + item['device_name'] + '</div> <a href="/form_advanced.html?_id=' + item['_Id'] + '"><span>Click</span></a> <button id="' + item['_Id'] + '" onclick="del(\'' + item['_Id'] + '\')"><span class="desc">delete</span></button> </div> </div>';
            });
            row_div.innerHTML = dataHTMLformat;
        }
    };
    xhttp.open("GET", "/refresh", true);
    xhttp.send();
}
