$(function(){
        var nav = $(".container-fluid .navbar");
        var navtxt = $(".navbar-nav .active>.nav-link, .navbar-nav .nav-link.active,  .navbar-nav .nav-link.show, .navbar-nav .show>.nav-link, .navbar-nav .nav-link");
        var img = $("nav img");
        var toggle = $(".navbar-toggler-icon");
        $(window).scroll(function(){
         var scrollTop =$("html,body").scrollTop();
         if (scrollTop>100) {
          nav.removeClass("bg-transparent","shadowsm");
          nav.addClass("bg-white");
          navtxt.removeClass("text-white");
          navtxt.addClass("text-dark");
          img.removeClass("brightness");
          toggle.addClass("text-dark");
        }else{
          toggle.removeClass("text-dark");
          nav.removeClass("bg-white");
          nav.addClass("bg-transparent","shadowsm");
          navtxt.removeClass("text-dark");
          navtxt.addClass("text-white");
          img.addClass("brightness");
        }
      })
      })