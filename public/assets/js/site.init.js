document.addEventListener("DOMContentLoaded", function(){
    // make it as accordion for smaller screens
    if (window.innerWidth < 992) {
    
      // close all inner dropdowns when parent is closed
      document.querySelectorAll('.navbar .dropdown').forEach(function(everydropdown){
        everydropdown.addEventListener('hidden.bs.dropdown', function () {
          // after dropdown is hidden, then find all submenus
            this.querySelectorAll('.submenu').forEach(function(everysubmenu){
              // hide every submenu as well
              everysubmenu.style.display = 'none';
            });
        })
      });
    
      document.querySelectorAll('.dropdown-menu a').forEach(function(element){
        element.addEventListener('click', function (e) {
            let nextEl = this.nextElementSibling;
            if(nextEl && nextEl.classList.contains('submenu')) {	
              // prevent opening link if link needs to open dropdown
              e.preventDefault();
              if(nextEl.style.display == 'block'){
                nextEl.style.display = 'none';
              } else {
                nextEl.style.display = 'block';
              }
    
            }
        });
      })
    }
    // end if innerWidth
    }); 
    // DOMContentLoaded  end



      /*
    // mobilemenu
    */
    $(function () {
      const body = $('body');
      const mobilemenu = $('.mobilemenu');

      if (mobilemenu.length) {
          const open = function() {
              const bodyWidth = body.width();
              body.css('overflow', 'hidden');
              body.css('paddingRight', (body.width() - bodyWidth) + 'px');

              mobilemenu.addClass('mobilemenu--open');
          };
          const close = function() {
              body.css('overflow', '');
              body.css('paddingRight', '');

              mobilemenu.removeClass('mobilemenu--open');
          };


          $('.mobile-header__menu-button').on('click', function() {
              open();
          });
          $('.mobilemenu__backdrop, .mobilemenu__close').on('click', function() {
              close();
          });
      }
  });


    /*
    // collapse
    */
    $(function () {
      $('[data-collapse]').each(function (i, element) {
          const collapse = element;

          $('[data-collapse-trigger]', collapse).on('click', function () {
              const openedClass = $(this).closest('[data-collapse-opened-class]').data('collapse-opened-class');
              const item = $(this).closest('[data-collapse-item]');
              const content = item.children('[data-collapse-content]');
              const itemParents = item.parents();

              itemParents.slice(0, itemParents.index(collapse) + 1).filter('[data-collapse-item]').css('height', '');

              if (item.is('.' + openedClass)) {
                  const startHeight = content.height();

                  content.css('height', startHeight + 'px');
                  item.removeClass(openedClass);

                  content.height(); // force reflow
                  content.css('height', '');
              } else {
                  const startHeight = content.height();

                  item.addClass(openedClass);

                  const endHeight = content.height();

                  content.css('height', startHeight + 'px');
                  content.height(); // force reflow
                  content.css('height', endHeight + 'px');
              }
          });

          $('[data-collapse-content]', collapse).on('transitionend', function (event) {
              if (event.originalEvent.propertyName === 'height') {
                  $(this).css('height', '');
              }
          });
      });
  });



  let searchMobileIcon = document.getElementById('searchMobileIcon');
  let mobileSearchHeader = document.getElementById('mobile-search-header');
  let mobileHeaderSearchButtonClose = document.getElementById('mobile-header__search-button--close');
  
if(searchMobileIcon)
{
searchMobileIcon.addEventListener("click" , function(){
    mobileSearchHeader.classList.add('open')

  });
  mobileHeaderSearchButtonClose.addEventListener("click" , function(){
    mobileSearchHeader.classList.remove('open')

  });
}
  
