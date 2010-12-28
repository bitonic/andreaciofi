/* Lightbox code for the show page */

window.addEvent('domready', function() {
    // Inject the divs
    $('wrapper').innerHTML += '<div id="lightbox_content"><div id="lightbox_img"><a id="lightbox_fullsize" href="javascript:hide_img()"><img src="" id="lightbox_img" /></a></div><div id="lightbox_navbar"><a href="javascript:hide_img()"><img src="/images/lightbox_close.png" /></a><div id="lightbox_navbar_inner"><a href="" id="lightbox_left"></a><a href="" id="lightbox_right"></a></div></div></div>'
    $('wrapper').innerHTML += '<div id="lightbox_overlay"></div>'
    lightbox_content = $('lightbox_content');
    lightbox_overlay = $('lightbox_overlay');
    lightbox_navbar = $('lightbox_navbar_inner');
    lightbox_img = $('lightbox_img');
    lightbox_left = $('lightbox_left');
    lightbox_right = $('lightbox_right');    

    // Remove actual links, replace with function calls,
    // and build list
    lightbox_imgs = []
    $$('.gallery_img_link').each(function(el){
        var img = el.getProperty('href');
        lightbox_imgs.push(img);
        el.setProperties({
            href: 'javascript:show_img("' + img + '")',
            target: '_self',
        });
    });
});

function show_img(imgurl) {
    hide_img();

    lightbox_img.empty();
    var img = new Element('img',{
        src: imgurl
    });
    lightbox_img.adopt(img);
    img.addEvent('load',function(){
        // Set the visibility
        lightbox_content.setStyle('display', 'block');
        lightbox_overlay.setStyle('display', 'block');
        var img_size = img.getSize();
        var win_size = window.getSize();

        if (img_size.x >= win_size.x || img_size.y >= win_size.y) {
            if ((img_size.x / img_size.y) >= (win_size.x / win_size.y)) {
                var img_width = win_size.x - 50;
                var img_height = (win_size.x - 50) * img_size.y / img_size.x;
                img.setProperties({
                    width: img_width,
                    height: img_height,
                });
            } else {
                var img_height = win_size.y - 65;
                var img_width = (win_size.y - 65) * img_size.x / img_size.y;
                img.setProperties({
                    height: img_height,
                    width: img_width,
                });            
            }
        }
        
        // Style of lightbox
        lightbox_content.setStyle('margin-left', '-' + (
            lightbox_content.getSize().x / 2) + 'px');
        lightbox_content.setStyle('top', (
            window.getScroll().y + (
                (win_size.y - lightbox_content.getSize().y) / 2)) + 'px');
        
        // Links
        lightbox_left.innerHTML = "";
        lightbox_right.innerHTML = "";        
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
        }
                
    });
}

function hide_img() {
    lightbox_content.setStyle('display', 'none');
    lightbox_overlay.setStyle('display', 'none');
}
