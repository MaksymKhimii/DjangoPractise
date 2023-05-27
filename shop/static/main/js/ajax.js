message = document.getElementById('description-message');

function hideMessage() {
    document.getElementById('description-message').style.display = 'none';
}

window.addEventListener('load', hideMessage());

function getProductDescription(title) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", `getProductDescription/${title}`, true);
    xhr.send();
    xhr.onreadystatechange = function () {
        let window = "";
        if (this.readyState === 4 && this.status === 200) {
            const description = JSON.parse(this.responseText);
            console.log("description: ", description);
            if( description != null) {
                window += "<div class=\"message_container\">\n" +
                    "            <div class=\"message_body\">\n" +
                    " <form action=\"/catalog\" method=\"get\">\n" +
                    "                    <input type=\"submit\" class=\"close_wind\" style=\"padding: 2.5px 7.5px\" value=\"&#10006\">\n" +
                    "                </form>" +
                    "                " + description + "\n" +
                    "            </div>" +
                    "</div>";
            } else {
                let nullDescriptionMessage = "Опис цього товару відсутній";
                window+="<div class=\"message_container\">\n" +
                    "            <div class=\"message_body\">\n" +
                    " <form action=\"/catalog\" method=\"get\">\n" +
                    "                    <input type=\"submit\" class=\"close_wind\" style=\"padding: 2.5px 7.5px\" value=\"&#10006\">\n" +
                    "                </form>" +
                    "               "+nullDescriptionMessage+" \n" +
                    "            </div>" +
                    "</div>";
            }
        }
        message.innerHTML = window;
    }
    document.getElementById('description-message').style.display = 'block';
}