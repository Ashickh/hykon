!function(e){"use strict";let t=!1;try{const e=Object.defineProperty({},"passive",{get:function(){t=!0}});window.addEventListener("test",null,e)}catch(e){}let n=null;function s(){return"rtl"===(null===n&&(n=getComputedStyle(document.body).direction),n)}e(function(){function n(t,n){t=e(t);let s=null;const i=function(e){const t=e.originalEvent;s=1===t.touches.length?{target:t.currentTarget,touch:t.changedTouches[0],timestamp:(new Date).getTime()}:null},o=function(e){const t=e.originalEvent;if(!s||1!==t.changedTouches.length||t.changedTouches[0].identity!==s.touch.identity)return;const i=(new Date).getTime(),o=t.changedTouches[0],r=Math.abs(Math.sqrt(Math.pow(s.touch.screenX-o.screenX,2)+Math.pow(s.touch.screenY-o.screenY,2)));s.target===t.currentTarget&&i-s.timestamp<500&&r<10&&n(e)};return t.on("touchstart",i),t.on("touchend",o),function(){t.off("touchstart",i),t.off("touchend",o)}}function i(){const e=function(t){t.preventDefault(),document.removeEventListener("click",e)};document.addEventListener("click",e),setTimeout(function(){document.removeEventListener("click",e)},100)}e(".topbar-dropdown__btn").on("click",function(){e(this).closest(".topbar-dropdown").toggleClass("topbar-dropdown--opened")}),document.addEventListener("click",function(t){e(".topbar-dropdown").not(e(t.target).closest(".topbar-dropdown")).removeClass("topbar-dropdown--opened")},!0),n(document,function(t){e(".topbar-dropdown").not(e(t.target).closest(".topbar-dropdown")).removeClass("topbar-dropdown--opened")});const o=e(".mobile-header__search");function r(t){this.element=e(t),this.items=this.element.find(".nav-links__item"),this.currentItem=null,this.element.data("navLinksInstance",this),this.onMouseenter=this.onMouseenter.bind(this),this.onMouseleave=this.onMouseleave.bind(this),this.onGlobalTouchClick=this.onGlobalTouchClick.bind(this),this.onTouchClick=this.onTouchClick.bind(this),this.items.on("mouseenter",this.onMouseenter),this.items.on("mouseleave",this.onMouseleave),n(document,this.onGlobalTouchClick),n(this.items,this.onTouchClick)}function a(t){this.element=e(t),this.container=this.element.find("> .menu__submenus-container"),this.items=this.element.find("> .menu__list > .menu__item"),this.currentItem=null,this.element.data("menuInstance",this),this.onMouseenter=this.onMouseenter.bind(this),this.onMouseleave=this.onMouseleave.bind(this),this.onTouchClick=this.onTouchClick.bind(this),this.items.on("mouseenter",this.onMouseenter),this.element.on("mouseleave",this.onMouseleave),n(this.items,this.onTouchClick)}function h(t){this.element=e(t),this.dropdown=this.element.find(".indicator__dropdown"),this.button=this.element.find(".indicator__button"),this.trigger=null,this.element.data("indicatorInstance",this),this.element.hasClass("indicator--trigger--hover")?this.trigger="hover":this.element.hasClass("indicator--trigger--click")&&(this.trigger="click"),this.onMouseenter=this.onMouseenter.bind(this),this.onMouseleave=this.onMouseleave.bind(this),this.onTransitionend=this.onTransitionend.bind(this),this.onClick=this.onClick.bind(this),this.onGlobalClick=this.onGlobalClick.bind(this),this.element.on("mouseenter",this.onMouseenter),this.element.on("mouseleave",this.onMouseleave),this.dropdown.on("transitionend",this.onTransitionend),this.button.on("click",this.onClick),e(document).on("click",this.onGlobalClick),n(document,this.onGlobalClick),this.element.find(".drop-search__input").on("keydown",function(t){if(27===t.which){const t=e(this).closest(".indicator").data("indicatorInstance");t&&t.close()}})}o.length&&(e(".indicator--mobile-search .indicator__button").on("click",function(){o.is(".mobile-header__search--opened")?o.removeClass("mobile-header__search--opened"):(o.addClass("mobile-header__search--opened"),o.find("input")[0].focus())}),o.find(".mobile-header__search-button--close").on("click",function(){o.removeClass("mobile-header__search--opened")}),document.addEventListener("click",function(t){e(t.target).closest(".indicator--mobile-search, .mobile-header__search").length||o.removeClass("mobile-header__search--opened")},!0)),r.prototype.onGlobalTouchClick=function(t){this.element.not(e(t.target).closest(".nav-links")).length&&this.unsetCurrentItem()},r.prototype.onTouchClick=function(t){if(t.cancelable){const n=e(t.currentTarget);if(this.currentItem&&this.currentItem.is(n))return;this.hasSubmenu(n)&&(t.preventDefault(),this.currentItem&&this.currentItem.trigger("mouseleave"),n.trigger("mouseenter"))}},r.prototype.onMouseenter=function(t){this.setCurrentItem(e(t.currentTarget))},r.prototype.onMouseleave=function(){this.unsetCurrentItem()},r.prototype.setCurrentItem=function(e){this.currentItem=e,this.currentItem.addClass("nav-links__item--hover"),this.openSubmenu(this.currentItem)},r.prototype.unsetCurrentItem=function(){this.currentItem&&(this.closeSubmenu(this.currentItem),this.currentItem.removeClass("nav-links__item--hover"),this.currentItem=null)},r.prototype.hasSubmenu=function(e){return!!e.children(".nav-links__submenu").length},r.prototype.openSubmenu=function(t){const n=t.children(".nav-links__submenu");if(!n.length)return;n.addClass("nav-links__submenu--display");const i=n.offset().top-e(window).scrollTop(),o=window.innerHeight;if(n.css("maxHeight",o-i-20+"px"),n.addClass("nav-links__submenu--open"),n.hasClass("nav-links__submenu--type--megamenu")){const e=n.offsetParent().width(),i=n.width();if(s()){const s=e-(t.position().left+t.width()),o=Math.round(Math.min(s,e-i));n.css("right",o+"px")}else{const s=t.position().left,o=Math.round(Math.min(s,e-i));n.css("left",o+"px")}}},r.prototype.closeSubmenu=function(e){const t=e.children(".nav-links__submenu");if(t.length&&(t.removeClass("nav-links__submenu--display"),t.removeClass("nav-links__submenu--open"),t.css("maxHeight",""),t&&t.is(".nav-links__submenu--type--menu"))){const e=t.find("> .menu").data("menuInstance");e&&e.unsetCurrentItem()}},e(".nav-links").each(function(){new r(this)}),a.prototype.onMouseenter=function(t){const n=e(t.currentTarget);this.currentItem&&n.is(this.currentItem)||(this.unsetCurrentItem(),this.setCurrentItem(n))},a.prototype.onMouseleave=function(){this.unsetCurrentItem()},a.prototype.onTouchClick=function(t){const n=e(t.currentTarget);this.currentItem&&this.currentItem.is(n)||this.hasSubmenu(n)&&(i(),this.unsetCurrentItem(),this.setCurrentItem(n))},a.prototype.setCurrentItem=function(e){this.currentItem=e,this.currentItem.addClass("menu__item--hover"),this.openSubmenu(this.currentItem)},a.prototype.unsetCurrentItem=function(){this.currentItem&&(this.closeSubmenu(this.currentItem),this.currentItem.removeClass("menu__item--hover"),this.currentItem=null)},a.prototype.getSubmenu=function(e){let t=e.find("> .menu__submenu");return t.length&&(this.container.append(t),e.data("submenu",t)),e.data("submenu")},a.prototype.hasSubmenu=function(e){return!!this.getSubmenu(e)},a.prototype.openSubmenu=function(t){const n=this.getSubmenu(t);if(!n)return;n.addClass("menu__submenu--display");const i=this.element.offset().top-e(window).scrollTop(),o=t.find("> .menu__item-submenu-offset").offset().top-e(window).scrollTop(),r=window.innerHeight,a=r-40;n.css("maxHeight",a+"px");const h=n.height(),u=Math.min(Math.max(o-i,0),r-20-h-i);if(n.css("top",u+"px"),n.addClass("menu__submenu--open"),s()){this.element.offset().left-n.width()<0&&n.addClass("menu__submenu--reverse")}else{this.element.offset().left+this.element.width()+n.width()>e("body").innerWidth()&&n.addClass("menu__submenu--reverse")}},a.prototype.closeSubmenu=function(e){const t=this.getSubmenu(e);if(t){t.removeClass("menu__submenu--display"),t.removeClass("menu__submenu--open"),t.removeClass("menu__submenu--reverse");const e=t.find("> .menu").data("menuInstance");e&&e.unsetCurrentItem()}},e(".menu").each(function(){new a(e(this))}),h.prototype.toggle=function(){this.isOpen()?this.close():this.open()},h.prototype.onMouseenter=function(){this.element.addClass("indicator--hover"),"hover"===this.trigger&&this.open()},h.prototype.onMouseleave=function(){this.element.removeClass("indicator--hover"),"hover"===this.trigger&&this.close()},h.prototype.onTransitionend=function(e){this.dropdown.is(e.target)&&"visibility"===e.originalEvent.propertyName&&!this.isOpen()&&this.element.removeClass("indicator--display")},h.prototype.onClick=function(e){"click"===this.trigger&&(e.cancelable&&e.preventDefault(),this.toggle())},h.prototype.onGlobalClick=function(t){this.element.not(e(t.target).closest(".indicator")).length&&this.close()},h.prototype.isOpen=function(){return this.element.is(".indicator--open")},h.prototype.open=function(){this.element.addClass("indicator--display"),this.element.width(),this.element.addClass("indicator--open"),this.element.find(".drop-search__input").focus();const t=this.dropdown.offset().top-e(window).scrollTop(),n=window.innerHeight;this.dropdown.css("maxHeight",n-t-20+"px")},h.prototype.close=function(){this.element.removeClass("indicator--open")},h.prototype.closeImmediately=function(){this.element.removeClass("indicator--open"),this.element.removeClass("indicator--display")},e(".indicator").each(function(){new h(this)}),e(function(){const s=function(t){t.data("departmentsInstance",this),this.element=t,this.container=this.element.find(".departments__submenus-container"),this.linksWrapper=this.element.find(".departments__links-wrapper"),this.body=this.element.find(".departments__body"),this.button=this.element.find(".departments__button"),this.items=this.element.find(".departments__item"),this.mode=this.element.is(".departments--fixed")?"fixed":"normal",this.fixedBy=e(this.element.data("departments-fixed-by")),this.fixedHeight=0,this.currentItem=null,"fixed"===this.mode&&this.fixedBy.length&&(this.fixedHeight=this.fixedBy.offset().top-this.body.offset().top+this.fixedBy.outerHeight(),this.body.css("height",this.fixedHeight+"px")),this.linksWrapper.on("transitionend",function(t){"height"===t.originalEvent.propertyName&&(e(this).css("height",""),e(this).closest(".departments").removeClass("departments--transition"))}),this.onButtonClick=this.onButtonClick.bind(this),this.onGlobalClick=this.onGlobalClick.bind(this),this.onMouseenter=this.onMouseenter.bind(this),this.onMouseleave=this.onMouseleave.bind(this),this.onTouchClick=this.onTouchClick.bind(this),this.button.on("click",this.onButtonClick),document.addEventListener("click",this.onGlobalClick,!0),n(document,this.onGlobalClick),this.items.on("mouseenter",this.onMouseenter),this.linksWrapper.on("mouseleave",this.onMouseleave),n(this.items,this.onTouchClick)};s.prototype.onButtonClick=function(e){e.preventDefault(),this.element.is(".departments--open")?this.close():this.open()},s.prototype.onGlobalClick=function(t){this.element.not(e(t.target).closest(".departments")).length&&this.element.is(".departments--open")&&this.close()},s.prototype.setMode=function(t){this.mode=t,"normal"===this.mode&&(this.element.removeClass("departments--fixed"),this.element.removeClass("departments--open"),this.body.css("height","auto")),"fixed"===this.mode&&(this.element.addClass("departments--fixed"),this.element.addClass("departments--open"),this.body.css("height",this.fixedHeight+"px"),e(".departments__links-wrapper",this.element).css("maxHeight",""))},s.prototype.close=function(){if(this.element.is(".departments--fixed"))return;const e=this.element.find(".departments__links-wrapper"),t=e.height();e.css("height",t+"px"),this.element.addClass("departments--transition").removeClass("departments--open"),e.css("height",""),e.css("maxHeight",""),this.unsetCurrentItem()},s.prototype.closeImmediately=function(){if(this.element.is(".departments--fixed"))return;const e=this.element.find(".departments__links-wrapper");this.element.removeClass("departments--open"),e.css("height",""),e.css("maxHeight",""),this.unsetCurrentItem()},s.prototype.open=function(){const e=this.element.find(".departments__links-wrapper"),t=e.height();this.element.addClass("departments--transition").addClass("departments--open");const n=document.documentElement.clientHeight,s=e[0].getBoundingClientRect(),i=Math.min(e.height(),n-20-s.top);e.css("height",t+"px"),e.css("maxHeight",i+"px"),e.css("height",i+"px")},s.prototype.onMouseenter=function(t){const n=e(t.currentTarget);this.currentItem&&n.is(this.currentItem)||(this.unsetCurrentItem(),this.setCurrentItem(n))},s.prototype.onMouseleave=function(){this.unsetCurrentItem()},s.prototype.onTouchClick=function(t){const n=e(t.currentTarget);this.currentItem&&this.currentItem.is(n)||this.hasSubmenu(n)&&(i(),this.unsetCurrentItem(),this.setCurrentItem(n))},s.prototype.setCurrentItem=function(e){this.unsetCurrentItem(),this.currentItem=e,this.currentItem.addClass("departments__item--hover"),this.openSubmenu(this.currentItem)},s.prototype.unsetCurrentItem=function(){this.currentItem&&(this.closeSubmenu(this.currentItem),this.currentItem.removeClass("departments__item--hover"),this.currentItem=null)},s.prototype.getSubmenu=function(e){let t=e.find("> .departments__submenu");return t.length&&(this.container.append(t),e.data("submenu",t)),e.data("submenu")},s.prototype.hasSubmenu=function(e){return!!this.getSubmenu(e)},s.prototype.openSubmenu=function(t){const n=this.getSubmenu(t);if(n){n.addClass("departments__submenu--open");const t=document.documentElement.clientHeight,s=20;if(n.hasClass("departments__submenu--type--megamenu")){const i=n.offset().top-e(window).scrollTop();n.css("maxHeight",t-i-s+"px")}if(n.hasClass("departments__submenu--type--menu")){n.css("maxHeight",t-s-Math.min(s,this.body.offset().top-e(window).scrollTop())+"px");const i=n.height(),o=this.currentItem.offset().top-e(window).scrollTop(),r=this.container.offset().top-e(window).scrollTop();n.css("top",Math.min(o,t-s-i)-r+"px")}}},s.prototype.closeSubmenu=function(e){const t=e.data("submenu");t&&(t.removeClass("departments__submenu--open"),t.is(".departments__submenu--type--menu")&&t.find("> .menu").data("menuInstance").unsetCurrentItem())};const o=e(".departments"),r=o.length?new s(o):null,a=e(".nav-panel--sticky");if(a.length){const n=a.data("sticky-mode")?a.data("sticky-mode"):"alwaysOnTop",s=matchMedia("(min-width: 992px)"),i=r?r.mode:null;let o=!1,h=!1,u=0,c=0,l=function(){return 0},m=function(){return 0};const d=function(){r&&r.closeImmediately(),e(".nav-links").data("navLinksInstance").unsetCurrentItem(),e(".indicator").each(function(){e(this).data("indicatorInstance").closeImmediately()})},p=function(){const e=window.pageYOffset-c;if(e<0!=u<0&&(u=0),c=window.pageYOffset,u+=e,window.pageYOffset>m()){if(o||(a.addClass("nav-panel--stuck"),a.css("transitionDuration","0s"),"alwaysOnTop"===n&&(a.addClass("nav-panel--show"),h=!0),a.height(),a.css("transitionDuration",""),o=!0,r&&"fixed"===i&&r.setMode("normal"),d()),"pullToShow"===n){const e=25;u<-10&&!a.hasClass("nav-panel--show")&&(a.addClass("nav-panel--show"),h=!0),u>e&&a.hasClass("nav-panel--show")&&(a.removeClass("nav-panel--show"),h=!1,d())}}else window.pageYOffset<=l()&&o&&(a.removeClass("nav-panel--stuck"),a.removeClass("nav-panel--show"),o=!1,h=!1,r&&"fixed"===i&&r.setMode("fixed"),d())},f=function(){if(s.matches){u=0,c=window.pageYOffset;const e=a.offset().top,s=e+a.outerHeight(),o=r?r.body.offset().top+r.body.outerHeight():0;r&&"fixed"===i&&o>s?l=m=function(){return o}:"alwaysOnTop"===n?l=m=function(){return e}:(l=function(){return h?e:s},m=function(){return s}),window.addEventListener("scroll",p,!!t&&{passive:!0}),p()}else o&&(a.removeClass("nav-panel--stuck"),a.removeClass("nav-panel--show"),o=!1,h=!1,r&&"fixed"===i&&r.setMode("fixed"),d()),window.removeEventListener("scroll",p,!!t&&{passive:!0})};s.addEventListener?s.addEventListener("change",f):s.addListener(f),f()}const h=e(".mobile-header--sticky"),u=h.find(".mobile-header__panel");if(h.length){const e=h.data("sticky-mode")?h.data("sticky-mode"):"alwaysOnTop",n=matchMedia("(min-width: 992px)");let s=!1,i=!1,o=0,r=0,a=0,c=0;const l=function(){const t=window.pageYOffset-r;if(t<0!=o<0&&(o=0),r=window.pageYOffset,o+=t,window.pageYOffset>c){if(s||(h.addClass("mobile-header--stuck"),u.css("transitionDuration","0s"),"alwaysOnTop"===e&&(h.addClass("mobile-header--show"),i=!0),h.height(),u.css("transitionDuration",""),s=!0),"pullToShow"===e)if(window.pageYOffset>a){const e=25;o<-10&&!i&&(h.addClass("mobile-header--show"),i=!0),o>e&&i&&(h.removeClass("mobile-header--show"),i=!1)}else i&&(h.removeClass("mobile-header--show"),i=!1)}else window.pageYOffset<=a&&s&&(h.removeClass("mobile-header--stuck"),h.removeClass("mobile-header--show"),s=!1,i=!1)},m=function(){n.matches?(s&&(h.removeClass("mobile-header--stuck"),h.removeClass("mobile-header--show"),s=!1,i=!1),window.removeEventListener("scroll",l,!!t&&{passive:!0})):(o=0,r=window.pageYOffset,a=h.offset().top,c=a+("alwaysOnTop"===e?0:h.outerHeight()),window.addEventListener("scroll",l,!!t&&{passive:!0}),l())};n.addEventListener?n.addEventListener("change",m):n.addListener(m),m()}})})}(jQuery);