let d = document,
cartCont = d.getElementById('shopping-cart');
let count = 1;
let title, price;
function openWindow(title, price){
//надо изменить этот блок до корректного+ написать функции для увеличения колличества товара ну и дальше уже отправку
let  totalItems = '';/*'<div class="title" style="text-align: center; top: 60px;">\n' +
            '       Товар:\n' +
            '    </div><br><br>';*/
             totalItems += '  ' +
                ' <label for="title" >Найменування товару: </label>'+
                '<input type="text" name="title" style="" id="title" value="' + title + '">  <br> '+
                 ' <label for="price" >Ціна товару: </label><br>'+
                ' <input type="text" name="price" style="" id="price" value="' + price + '"> <br>'+
                'Кількість:<br>  '+
                /*'<button class="plus-btn" type="button onclick="addCount('+count+')" name="button">' +
                 '                <img src="https://designmodo.com/demo/shopping-cart/plus.svg" alt=""/>' +
                '            </button>' + '  ' +*/
                 '<input type="number" name="productCount" style="" id="productCount" value="'+count+'">';
               /*  '<button class="minus-btn" type="button onclick="minusCount(' + title + ')" name="button">' +
                '                <img src="https://designmodo.com/demo/shopping-cart/minus.svg" alt=""/>' +
                '            </button>';*/
                cartCont.innerHTML = totalItems;
}

function addToBasket(id) {
let item_title = document.getElementById('title'+id).innerHTML;
let item_price =document.getElementById("price"+id).innerHTML;
title = item_title;
price = item_price;
    console.log('title'+id+' : '+item_title);
    console.log("price"+id+' : '+ item_price);
openWindow(item_title, item_price);
document.getElementById('message').style.display = 'block';
}

function addCount(count){
count++;
openWindow(title, price);
}

