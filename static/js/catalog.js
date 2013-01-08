$(document).ready(function() {

    function updateURLParameter(url, param, paramVal){
        var newAdditionalURL = "";
        var tempArray = url.split("?");
        var baseURL = tempArray[0];
        var additionalURL = tempArray[1];
        var temp = "";
        if (additionalURL) {
            tempArray = additionalURL.split("&");
            for (i=0; i<tempArray.length; i++){
                if(tempArray[i].split('=')[0] != param){
                    newAdditionalURL += temp + tempArray[i];
                    temp = "&";
                }
            }
        }

        var rows_txt = '';
        if (paramVal !== 'delete') {
            rows_txt = temp + "" + param + "=" + paramVal;
        }
        return baseURL + "?" + newAdditionalURL + rows_txt;
    }


    $('h2:first').addClass('active');
    $('.toggle_container:not(:first)').hide();

    $('h2.trigger').click(function() {
    	$(this).toggleClass('active').next().slideToggle('slow').siblings("div:visible").slideUp('slow');
    	$(this).siblings('h2').removeClass('active');
    	return false;
    });

    $('.filter_link').on('click', function(e) {
        e.preventDefault();
        var data = $(this).data();
        var newURL = updateURLParameter(window.location.href, data.filterName, data.filterValue);
        newURL = updateURLParameter(newURL, 'page', 'delete');
        window.location = newURL;
    });

    $('#price-form').on('submit', function(e) {
        e.preventDefault();
        var newURL = updateURLParameter(window.location.href, 'price-range', $('#price').val() + ':' + $('#price2').val());
        window.location = newURL;
    });

    $('.pagPage a').on('click', function(e) {
        e.preventDefault();
        var data = $(this).data();
        var newURL = updateURLParameter(window.location.href, 'page', data.page);
        window.location = newURL;
    });

    $('.buy_btn').on('click', function(e) {
        var data = $(this).data();
        e.preventDefault();
        $.post(data.url, {'product_slug' : data.slug}, function(data) {
            window.location = data.url;
        });
    });
});