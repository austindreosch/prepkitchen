
let lastClickedID = 0;
let serverBaseURL = "https://prepkitchen.onrender.com";

$(document).ready(function() {
    console.log( "ready!" );
    let appDir = "/cart" 
    let currentLocalStorage = []

    // if localStorage cart exists, assign it to var
    if(localStorage.getItem("cart_array")){
        currentLocalStorage = JSON.parse(localStorage.getItem("cart_array"));
    }
    else {
        localStorage.setItem('cart_array', JSON.stringify([]));
    }

    // for each id in shopping cart, add hidden previously chosen meal cards
    for (let id of currentLocalStorage) {
        parsedID = parseInt(id)
        $(`#${parsedID}`).parent().hide();
    }


    // on click - add meal id to shopping cart session, send data to flask, and reload page
    $('.cartbutton').on('click', function(){
        let lastClickedID = $(this).closest('button').attr('id');
        let mealCap = $('.cart-heading').attr('id');

        // if clicked ID is already in localStorage
            // alert("already in cart")

        if(currentLocalStorage.length >= mealCap){
            console.log(`Cart is full!`);
            $('.menu-heading-h1').text('Cart is full !') 
            return
            // location.reload();
        }
        else { 
            //add id to localStorage
            currentLocalStorage.push(lastClickedID);
            console.log(`index0: ${currentLocalStorage[0]}`);
            console.log(`Added meal-${lastClickedID} to cart!`);
            localStorage.setItem('cart_array', JSON.stringify(currentLocalStorage));
            
            

            //send localstorage cart to flask   
            $.ajax({
                url: serverBaseURL + appDir,
                method: 'POST',
                dataType: 'json',
                data: { cart_array: localStorage.getItem("cart_array") },
                success: function(response){
                    console.log(response);
                    // location.reload();
                },
                error: function(error) {
                    console.log(error);
                }   
            })

            // location.reload();
            setTimeout(() => {
                location.reload();
                }, 1000)
        }
        
        // if (currentLocalStorage.includes(lastClickedID)){
        //     console.log(`${lastClickedID} already in cart!`)
        // }
        // else { // if clicked ID is not in localStorage
        //     // 
            
        // }
    })

    // on click of clear cart button, clear localstorage variable
    $('.cart-clearbtn').on('click', function(){
        localStorage.setItem('cart_array', JSON.stringify([]));
        // also clears session data based on flask /clear route.
    })


}); // end of dom loader

// data: JSON.parse(localStorage.getItem("cart_array"))
// localStorage.setItem('cart_array', JSON.stringify([32445,35486]))