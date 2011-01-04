/* Lightbox code for the show page */

var lightbox_content;
var lightbox_overlay;
var lightbox_navbar;
var lightbox_img;
var lightbox_left;
var lightbox_right;
var lightbox_loading;
var current_img = null;

window.addEvent('domready', function() {
    // Inject the divs
    document.body.innerHTML += '\
        <div id="lightbox_content"> \
          <div id="lightbox_img"> \
            <img src="/images/filler.png" /> \
          </div> \
          <div id="lightbox_navbar"> \
            <a href="javascript:hide_img()" id="lightbox_close"> \
              <img src="/images/lightbox_close.png"/> \
            </a> \
            <span id="lightbox_loading"></span> \
            <div id="lightbox_navbar_inner"> \
              <a href="" id="lightbox_left"></a> \
              <a href="" id="lightbox_right"></a> \
            </div> \
          </div> \
        </div> \
        <div id="lightbox_overlay"></div>';
    lightbox_content = $('lightbox_content');
    lightbox_overlay = $('lightbox_overlay');
    lightbox_navbar = $('lightbox_navbar_inner');
    lightbox_img = $('lightbox_img');
    lightbox_left = $('lightbox_left');
    lightbox_right = $('lightbox_right');
    lightbox_loading = $('lightbox_loading');

    // Add onclick event on overlay
    lightbox_overlay.addEvent('click', hide_img);

    // Remove actual links, replace with function calls,
    // and build list
    $$('.gallery_img_link').each(function(el){
        var img = el.getProperty('href');
        el.setProperties({
            href: 'javascript:show_img("' + img + '")',
            target: '_self'
        });
    });
});

window.addEvent('resize', function() {
    if (current_img != null)
        show_img(current_img);
});

function show_img(imgurl) {
    current_img = imgurl;
    lightbox_position();
    var img = new Element('img',{
        src: imgurl
    });
    
    lightbox_content.setStyle('display', 'block');
    lightbox_overlay.setStyles({
        display: 'block',
        width: document.window.getScrollSize().x + 'px',
        height: document.window.getScrollSize().y + 'px'
    });
    lightbox_loading.set('text', 'loading...');
    img.addEvent('load',function(){
        // Set the visibility
        lightbox_loading.empty();
	lightbox_img.empty();
	lightbox_img.adopt(img);	
        var img_size = img.getSize();
        var win_size = window.getSize();

        if (img_size.x >= win_size.x || img_size.y >= win_size.y) {
            if ((img_size.x / img_size.y) >= (win_size.x / win_size.y)) {
                var img_width = win_size.x - 50;
                var img_height = (win_size.x - 50) * img_size.y / img_size.x;
                img.setProperties({
                    width: img_width,
                    height: img_height
                });
            } else {
                var img_height = win_size.y - 65;
                var img_width = (win_size.y - 65) * img_size.x / img_size.y;
                img.setProperties({
                    height: img_height,
                    width: img_width
                });            
            }
        }
        
        lightbox_position();
                
        // Links
        lightbox_left.innerHTML = "";
        lightbox_right.innerHTML = "";
        lightbox_img.removeEvents('click');
        lightbox_img.setStyle('cursor', 'default');
        for (var i = 0; i < lightbox_imgs.length; i++) {
            if (lightbox_imgs[i] == imgurl)
                break;
        }
        if (i > 0) {
            lightbox_left.setProperty(
                'href', 'javascript:show_img("' + lightbox_imgs[i-1] + '")');
            lightbox_left.innerHTML = '<img src="/images/lightbox_left.png" />';
        }
        if (i < lightbox_imgs.length - 1) {
            lightbox_right.setProperty(
                'href', 'javascript:show_img("' + lightbox_imgs[i+1] + '")');
            lightbox_right.innerHTML = '<img src="/images/lightbox_right.png" />';
            lightbox_img.addEvent('click', function() {
                show_img(lightbox_imgs[i+1]);
            });
            lightbox_img.setStyle('cursor', 'pointer');
        }
    });
}

function lightbox_position() {
    // Style of lightbox
    lightbox_content.setStyle('margin-left', '-' + (
        lightbox_content.getSize().x / 2) + 'px');
    lightbox_content.setStyle('top', (
        window.getScroll().y + (
            (window.getSize().y - lightbox_content.getSize().y) / 2)) + 'px');
}

function hide_img() {
    current_img = null;
    lightbox_content.setStyle('display', 'none');
    lightbox_overlay.setStyle('display', 'none');
    lightbox_img.set('html', '<img src="/images/filler.png />');
}