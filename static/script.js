
let lastClickedID = 0;
let serverBaseURL = "http://127.0.0.1:5000";

$(document).ready(function() {
    console.log( "ready!" );
    let appDir = "/cart" 
    
    $('.cartbutton').on('click', function(){
        lastClickedID = $(this).closest('button').attr('id');
        let currentLocalStorage = []
        // if localStorage cart exists, assign it to var
        if(localStorage.getItem("cart_array")){
            currentLocalStorage = JSON.parse(localStorage.getItem("cart_array"));
            // currentLocalStorage = localStorage.getItem('cart_array');
            console.log(typeof currentLocalStorage);
        }
        else {
            localStorage.setItem('cart_array', JSON.stringify([]));
        }


        // if clicked ID is already in localStorage
            // alert("already in cart")
        if (currentLocalStorage.includes(lastClickedID)){
            console.log(`${lastClickedID} already in cart!`)
        }
        else { // if clicked ID is not in localStorage
            if(currentLocalStorage.length === 5){
                console.log(`Cart is full!`);
                // alert("Cart is full!");
                location.reload();
            }
            else { 
                //add id to localStorage
                currentLocalStorage.push(lastClickedID);
                console.log(`index0: ${currentLocalStorage[0]}`);
                console.log(`Added meal-${lastClickedID} to cart!`);
                localStorage.setItem('cart_array', JSON.stringify(currentLocalStorage));
                
                // this works
                // localStorage.setItem('cart_array', JSON.stringify([32445,35486]));
                

                //send localstorage cart to flask   
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

                // location.reload();
                setTimeout(() => {
                    location.reload();
                  }, 10)
            }
            
        }
    })

    // on click of clear cart button, clear localstorage variable
    $('.cart-clearbtn').on('click', function(){
        localStorage.setItem('cart_array', JSON.stringify([]));
    })


}); // end of dom loader
                    // data: JSON.parse(localStorage.getItem("cart_array")), 