console.log("HERE");

$((function(context) {
    
    // utc_epoch comes from index.py
    console.log('Current epoch in UTC is ' + context.utc_epoch);

    return function() {
       
        var containers = $('.product-container');
        
        containers.each(function(i, container) {
           
            var pid = $(container).attr('data-product-id');
           
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            }).done(function(content){
                $(container).html(content);
            });
            console.log(444, pid);
        });
        //this is all so we know what image we will need to pull in

    }
    
})(DMP_CONTEXT.get()));
