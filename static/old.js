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
            // cartArray.push(lastClickedID);

            localStorage.setItem('cart_array', JSON.stringify(cartArray));
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
    location.reload();
});