var checkbox = document.getElementsByClassName('filter-checkbox')

    window.onload = function(){
        for(i = 0; i < checkbox.length ; i++){
            checkbox[i].addEventListener('click',function(){
            var _filterObj = {};
                var _filterVal=this.val();
                var _filterKey=this.data('filter');
                console.log(_filterKey,_filterVal);
            });
        };
    };
