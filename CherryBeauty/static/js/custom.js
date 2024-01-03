$(document).ready(function(){
    $("#loadMore").on('click',function(){
        var _currentProducts = $(".product-box").length;
        var _limit = $(this).attr('data-limit');
        var _total = $(this).attr('data-total');

    });

    $("#addToCartBtn").on('click',function(){
        var _qty =$("#productQty").val();
        var _productId =$("#product-id").val();
        var _productTitle =$("#product-title").val();

    });

});