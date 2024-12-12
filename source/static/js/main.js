$(function() {

  'use strict';

  $('.js-menu-toggle').click(function(e) {

  	var $this = $(this);

  	

  	if ( $('body').hasClass('show-sidebar') ) {
  		$('body').removeClass('show-sidebar');
  		$this.removeClass('active');
  	} else {
  		$('body').addClass('show-sidebar');	
  		$this.addClass('active');
  	}

  	e.preventDefault();

  });

  // click outisde offcanvas
	$(document).mouseup(function(e) {
    var container = $(".sidebar");
    if (!container.is(e.target) && container.has(e.target).length === 0) {
      if ( $('body').hasClass('show-sidebar') ) {
				$('body').removeClass('show-sidebar');
				$('body').find('.js-menu-toggle').removeClass('active');
			}
    }
	}); 

    
document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('.form-control');

    inputs.forEach(function(input) {
        input.addEventListener('focus', function () {
            let label = input.nextElementSibling;
            if (label && label.tagName.toLowerCase() === 'label') {
                label.classList.add('active');
            }
        });

        input.addEventListener('blur', function () {
            let label = input.nextElementSibling;
            if (label && label.tagName.toLowerCase() === 'label' && !input.value) {
                label.classList.remove('active');
            }
        });
    });
});
});
