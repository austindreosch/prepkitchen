let cartArray = [];
let lastClickedID = 0;
let serverBaseURL = "http://127.0.0.1:5000";

$(document).ready(function() {
    console.log( "ready!" );
    let appDir = "/cart"

    $('.cartbutton').on('click', function(){
        lastClickedID = $(this).closest('button').attr('id');
        // if its not in array already, add it
        if (cartArray.includes(lastClickedID)){
            console.log(`${lastClickedID} already in cart!`)
        }
        else {
            // check for cart size
            if(cartArray.length === 5){
                console.log(`Cart is full!`);
                alert("Cart is full!");
            }
            else {
                // add to cart array, if not full - and set localstorage variable
                cartArray.push(lastClickedID);
                localStorage.setItem('cart_array', cartArray);
                console.log(`Added meal-${lastClickedID} to cart!`);

                $.ajax({
                    url: serverBaseURL + appDir,
                    method: 'POST',
                    dataType: 'json',
                    data: localStorage.getItem("cart_array"),
                    success: function(response){
                        console.log(response);
                        // use api data here, if needed
                    }   
            
                })
            

            }
        }
    })



}); // end of dom loader