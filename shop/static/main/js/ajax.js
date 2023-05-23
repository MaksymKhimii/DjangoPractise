container = document.getElementById('container');
window.addEventListener('load', getProducts);

function getProducts() {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "getAllProducts", true);
    xhr.send();
    xhr.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            console.log(this.responseText)
            const products = JSON.parse(this.responseText);
            console.log(products[0].title);
            let totalItems = ''
            let i = 0;
            for (let i = 0; i < products.length; i++) {
                console.log(products.title)
                totalItems += ' <div class="item_box">\n' +
                    '            <img src="' + products[i].img + '"\n' +
                    '                 alt="photo">\n' +
                    '            <div class="product-list">\n' +
                    '                <div id="title'+i+'" class="item_title">' + products[i].title + '</div>\n' +
                    '                <span id="price'+i+'" class="item_price">' + products[i].price + '</span>\n' +
                    '                <button onclick="addToBasket('+i+')"\n' +
                    '                        class="add_item" data-id="'+i+'">Додати до кошика\n' +
                    '                </button>\n' +
                    '            </div>\n' +
                    '        </div>'
            }
            container.innerHTML = totalItems;
        }
    }

}