(function($) {

  new WOW().init();

  jQuery(window).load(function() {
    jQuery("#preloader").delay(100).fadeOut("slow");
    jQuery("#load").delay(100).fadeOut("slow");
  });

// to remove active and add to new one from dropdown -----------KT
$('.dropdown-menu li').click(function () {
    $('li').removeClass('active');
    $(this).addClass("active");
});

  //jQuery to collapse the navbar on scroll
  $(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
      $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
      $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
  });


// to remove active and add to new one from dropdown -----------KT
  $("[data-collapse-group]").on('show.bs.collapse', function () {
    var $this = $(this);
    var thisCollapseAttr = $this.attr('data-collapse-group');
    $("[data-collapse-group='" + thisCollapseAttr + "']").not($this).collapse('hide');
  });

  //jQuery for page scrolling feature - requires jQuery Easing plugin
  $(function() {

    $('.navbar-nav li a').on('click', function(event) {

      if ($(this).is('a:not([href^="#"])') || $(this).attr("href") == '#') {
        return;
      }
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top
      }, 1500, 'easeInOutExpo');
      event.preventDefault();
    });

    $('.page-scroll a').on('click', function(event) {
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top
      }, 1500, 'easeInOutExpo');
      event.preventDefault();
    });

  });

	var navMain = $(".navbar-collapse");
	navMain.on("click", "a:not([data-toggle])", null, function () {
	   navMain.collapse('hide');
	});

})(jQuery);

//get spider pages
function getspider(pk) {
  pk = pk
  $.ajax({
    url: 'spider/' + pk,
    success: function(data) {
      $('#' + pk + 'spider').html(data);
    }
  });
};


//get stats pages
function getstats(pk) {
  pk = pk
  $.ajax({
    url: 'player_stats/' + pk,
    success: function(data) {
      $('#' + pk + 'ps').html(data);
    }
  });
};

//get HH matches
function gethhmatches(pk) {
  pk = pk
  $.ajax({
    url: 'hhmatches/' + pk,
    success: function(data) {
      $('#' + pk + 'hhmatches').html(data);
    }
  });
};

//get Hist Rank
function gethrank(pk) {
  pk = pk
  $.ajax({
    url: 'histrank/' + pk,
    success: function(data) {
      $('#' + pk + 'histrank').html(data);
    }
  });
};

//get last matches  the hidden div needs the matchid and playerid
function getpastmatches(pk, pid) {
  pk = pk
  $.ajax({
    url: 'pastmatches/' + pk + '/' + pid,
    success: function(data) {
      $('#' + pk + pid + 'pastmatches').html(data);
    }
  });
};