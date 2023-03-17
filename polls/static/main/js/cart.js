let d = document,
    itemBox = d.querySelectorAll('.item_box'),
    cartCont = d.getElementById('shopping-cart');

function addEvent(elem, type, handler) {
    if (elem.addEventListener) {
        elem.addEventListener(type, handler, false);
    } else {
        elem.attachEvent('on' + type, function () {
            handler.call(elem);
        });
    }
    return false;
}

function getCartData() {
    return JSON.parse(localStorage.getItem('cart'));
}

function setCartData(o) {
    localStorage.setItem('cart', JSON.stringify(o));
    return false;
}

function addToCart() {
    this.disabled = true;
    let cartData = getCartData() || {},
        itemId = this.getAttribute('data-id');
    if (cartData.hasOwnProperty(itemId)) {
        cartData[itemId][2] += 1;
    } else {
        parentBox = this.parentNode;
        itemTitle = parentBox.querySelector('.item_title').innerHTML;
        itemPrice = parentBox.querySelector('.item_price').innerHTML;
        cartData[itemId] = [itemTitle, itemPrice, 1];
    }
    if (!setCartData(cartData)) {
        this.disabled = false;
    }
    return false;
}

for (let i = 0; i < itemBox.length; i++) {
    addEvent(itemBox[i].querySelector('.add_item'), 'click', addToCart);
}

function openCart() {
    var cartData = getCartData(),
        totalItems = '';
    if (cartData !== null) {
        totalItems = '<div class="title" style="text-align: center; top: 60px;">\n' +
            '        Товари у кошику:\n' +
            '    </div><br><br>';
        for (let items in cartData) {
            let title = cartData[items][0];
            totalItems += cartData[items][0] + '  ' +
                '              <button class="plus-btn" type="button" data-id="' + items + '" onclick="addCount(' + items + ')" name="button">' +
                '                <img src="https://designmodo.com/demo/shopping-cart/plus.svg" alt=""/>' +
                '            </button>' + ' <input type="text" name="name" style="" id="count1" value="' + cartData[items][2] + '">   '
                + '<button class="minus-btn" type="button" data-id="' + items + '" onclick="minusCount(' + items + ')" name="button">' +
                '                <img src="https://designmodo.com/demo/shopping-cart/minus.svg" alt=""/>' +
                '            </button>' + '  ' + cartData[items][1] + '$  ' +
                '<button class="delete-btn1" type="button" data-id="' + items[0] + '" onclick="deleteItem(this)" name="button"></button><br>';
        }
        totalItems += 'Загальна сума:  ' + recalculate() + '$<br>';
        cartCont.innerHTML = totalItems;
    } else {
        cartCont.innerHTML = 'Кошик порожній!';
    }
    return false;
}

addEvent(d.getElementById('clear_cart'), 'click', function (e) {
    localStorage.removeItem('cart');
    cartCont.innerHTML = 'Кошик порожній!';
});

for (let i = 0; i < itemBox.length; i++) {
    addEvent(itemBox[i].querySelector('.add_item'), 'click', function () {
        openCart();
        document.getElementById('message').style.display = 'block';
    });
}

function deleteItemCount(itemId) {
    let cartData = getCartData();
    delete cartData[itemId];
    setCartData(cartData);
}

function deleteItem(e) {
    let itemId = e.getAttribute('data-id');
    deleteItemCount(itemId);
    openCart();
    document.getElementById('message').style.display = 'block';
}


function plusCountItem(i) {
    this.disabled = true;
    let cartData = getCartData();
    if (cartData.hasOwnProperty(i)) {
        cartData[i][2] += 1;
    }
    if (!setCartData(cartData)) {
        this.disabled = false;
    }
    return false;
}

function minusCountItem(i) {
    this.disabled = true;
    let cartData = getCartData();
    if (cartData.hasOwnProperty(i)) {
        if (cartData[i][2] > 1) {
            cartData[i][2] -= 1;
        }
    }
    if (!setCartData(cartData)) {
        this.disabled = false;
    }
    return false;
}

function addCount(i) {
    plusCountItem(i);
    openCart();
    document.getElementById('message').style.display = 'block';
}

function minusCount(i) {
    minusCountItem(i);
    openCart();
    document.getElementById('message').style.display = 'block';
}

addEvent(d.querySelector('.close_wind'), 'click', function () {
    document.getElementById('message').style.display = 'none';
});


function recalculate() {
    let cartData = getCartData();
    let sum = 0;
    for (let item in cartData) {
        sum += cartData[item][1] * cartData[item][2];
    }
    console.log(sum);
    return sum;
}