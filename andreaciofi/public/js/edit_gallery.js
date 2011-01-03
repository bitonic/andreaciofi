var current_image = null;
var selected_image = null;

// Updates the image list
var images_list_req = new Request.HTML({
    url:images_list_url, 
    onSuccess: function(html) {
        //Clear the text currently inside the results div.
        $('images_delete_list').set('text', '');
        //Inject the new DOM elements into the results div.
        $('images_delete_list').adopt(html);
        // Reinitialize the image order
        images_order();
    },
    //Our request will most likely succeed, but just in case, we'll add an
    //onFailure method which will let the user know what happened.
    onFailure: function() {
        $('images_delete_list').set('text', 'The request failed.');
    }
});

function delete_image(req_url) {
    var req = new Request({
        url:req_url,
        onSuccess: function() {
            images_list_req.send();
        },
    });
    req.send();
}

function photoqueue() {
    // our uploader instance 
    
    var up = new FancyUpload2($('images_status'), $('images_list'), { // options object
	// we console.log infos, remove that in production!!
	verbose: true,
	
	// url is read from the form, so you just have to change one place
	url: images_upload_url,
	
	// path to the SWF file
	path: '/fancyupload/source/Swiff.Uploader.swf',
	
	// remove that line to select all files, or edit it, add more items
	typeFilter: {
	    'Images (*.jpg, *.jpeg, *.gif, *.png)': '*.jpg; *.jpeg; *.gif; *.png'
	},
	
	// this is our browse button, *target* is overlayed with the Flash movie
	target: 'images_browse',
	
	// graceful degradation, onLoad is only called if all went well with Flash
	onLoad: function() {
	    $('images_status').removeClass('hide'); // we show the actual UI
	    
	    // We relay the interactions with the overlayed flash to the link
	    this.target.addEvents({
		click: function() {
		    return false;
		},
		mouseenter: function() {
		    this.addClass('hover');
		},
		mouseleave: function() {
		    this.removeClass('hover');
		    this.blur();
		},
		mousedown: function() {
		    this.focus();
		}
	    });

	    // Interactions for the 2 other buttons
	    
	    $('images_clear').addEvent('click', function() {
		up.remove(); // remove all files
		return false;
	    });

	    $('images_upload').addEvent('click', function() {
		up.start(); // start upload
		return false;
	    });
	},
	
	/**
	 * Is called when files were not added, "files" is an array of invalid File classes.
	 * 
	 * This example creates a list of error elements directly in the file list, which
	 * hide on click.
	 */ 
	onSelectFail: function(files) {
	    files.each(function(file) {
		new Element('li', {
		    'class': 'validation-error',
		    html: file.validationErrorMessage || file.validationError,
		    title: MooTools.lang.get('FancyUpload', 'removeTitle'),
		    events: {
			click: function() {
			    this.destroy();
			}
		    }
		}).inject(this.list, 'top');
	    }, this);
	},
	
	/**
	 * This one was directly in FancyUpload2 before, the event makes it
	 * easier for you, to add your own response handling (you probably want
	 * to send something else than JSON or different items).
	 */
	onFileSuccess: function(file, response) {
	    var json = new Hash(JSON.decode(response, true) || {});
	    
	    if (json.get('status') == '1') {
		file.element.addClass('file-success');
		file.info.set('html', '<strong>Image was uploaded:</strong> ' + json.get('width') + ' x ' + json.get('height') + 'px, <em>' + json.get('mime') + '</em>)');
	    } else {
		file.element.addClass('file-failed');
		file.info.set('html', '<strong>An error occured:</strong> ' + (json.get('error') ? (json.get('error') + ' #' + json.get('code')) : response));
	    }

            // Updates the images list
            images_list_req.send();
	},
	
	/**
	 * onFail is called when the Flash movie got bashed by some browser plugin
	 * like Adblock or Flashblock.
	 */
	onFail: function(error) {
	    switch (error) {
	    case 'hidden': // works after enabling the movie and clicking refresh
		alert('To enable the embedded uploader, unblock it in your browser and refresh (see Adblock).');
		break;
	    case 'blocked': // This no *full* fail, it works after the user clicks the button
		alert('To enable the embedded uploader, enable the blocked Flash movie (see Flashblock).');
		break;
	    case 'empty': // Oh oh, wrong path
		alert('A required file was not found, please be patient and we fix this.');
		break;
	    case 'flash': // no flash 9+ :(
		alert('To enable the embedded uploader, install the latest Adobe Flash plugin.')
	    }
	}
	
    });
}

function images_order() {
    var dragged_image = $('dragged_image');

    // Add the events to all the cells
    $$('.image_cell').each(function(el){
        el.addEvents({
            'mouseenter': function(){
                current_image = el.get('id');
                if (selected_image) {
                    el.setStyle('border-right', '3px solid black');
                }
            },
            'mouseleave': function(){
                current_image = null;
                el.setStyle('border-right', 'none');
            }
        });
        new Drag(el, {
            snap: 0,
            onSnap: function(el, event){
                selected_image = el.get('id');
                dragged_image.set('html', el.get('html'));
            },
            onDrag: function(el, event){
                dragged_image.setStyles({
                    display: 'block',
                    top: (event.page.y + 1) + 'px',
                    left: (event.page.x + 1) + 'px',
                });
            },
            onComplete: function(el, event){
                dragged_image.setStyle('display', 'none');
                if (current_image && (current_image != selected_image)) {
                    // Remove the selected image from the array
                    var i = images_order_list.indexOf(selected_image);
                    images_order_list.splice(i, 1);
                    // Add the selected image at the right position
                    i = images_order_list.indexOf(current_image) + 1;
                    images_order_list = images_order_list.slice(0, i).concat(
                        selected_image, images_order_list.slice(i));
                    selected_image = null;
                    
                    // Send the request
                    var request = new Request({
                        url: images_order_url,
                        onSuccess: function(){
                            images_list_req.send();
                        },
                    });
                    request.post('images_order=' + JSON.encode(images_order_list));
                }
            }
        });
    });
}

window.addEvent('domready', function() { // wait for the content
    photoqueue();
    images_order();
});