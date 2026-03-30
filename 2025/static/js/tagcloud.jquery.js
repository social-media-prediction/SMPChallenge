/**
 * jQuery TagCloud plugin
 *
 * @version 1.2.2 (12-MAY-2009)
 * @author Nurul Ferdous <nurul_ferdous@yahoo.com>
 * @requires jQuery v1.4.3 or later Examples and documentation at:
 * http://dynamicguy.com/ Dual licensed under the MIT and GPL
 * licenses: http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 * Revision: $Id$
 */

;( function($) {
	var tags;
	var mathAssets = {
		halfHeight : null,
		halfWidth : null,
		hwratio : null,
		dtr : null,
		diameter : null,
		speedX : null,
		speedY : null,
		tLength : null
	}
	var settings = {
		//height of sphere container
		height : 400,
		//width of sphere container
		width : 400,
		//radius of sphere
		radius : 150,
		//rotation speed
		speed : 3,
		//sphere rotations slower
		slower : 0.9,
		//delay between update position
		timer : 5,
		//dependence of a font size on axis Z
		fontMultiplier : 15,
		//tag css stylies on mouse over
		hoverStyle : {
			border : '1px solid #935C26',
			color : '#935C26'
		},
		//tag css stylies on mouse out
		mouseOutStyle : {
			border : 'none',
			color : 'red'
		}
	}

	var curState = {
		mouseOver : null,
		lastFy : null,
		lastFx : null,
		sy : null,
		cy : null,
		sx : null,
		cx : null,
		mouseX : null,
		mouseY : null
	}
	var options = {};
	jQuery.fn.tagoSphere = function(opt) {
		options = jQuery.extend(settings, opt);
		initContainer(this);
		initTags(this);
		initMaths();
		deployTags();
		setInterval(updateTags, options.timer);
		return this;
	};

	function initMaths() {
		mathAssets.halfHeight = options.height / 2;
		mathAssets.halfWidth = options.width / 2;
		mathAssets.speedX = options.speed / mathAssets.halfWidth;
		mathAssets.speedY = options.speed / mathAssets.halfHeight;
		mathAssets.dtr = Math.PI / 180;
		mathAssets.diameter = options.radius * 2;
		mathAssets.hwratio = options.height / options.width;
		mathAssets.whratio = options.width / options.height;
		mathAssets.tLength = tags.length - 1;
		curState.mouseOver = false;
		curState.lastFx = options.speed;
		curState.lastFy = options.speed;
	}

	function initContainer(tagContainer) {
		tagContainer.height(options.height);
		tagContainer.width(options.width);
		tagContainer.css( {
			'overflow' : 'hidden',
			'position' : 'relative'
		});
		tagContainer.mousemove( function(e) {
			curState.mouseX = e.pageX - this.offsetLeft;
			curState.mouseY = e.pageY - this.offsetTop;
		});
		tagContainer.hover( function() {
			curState.mouseOver = true;
		}, function() {
			curState.mouseOver = false;
		});
	}

	function initTags(tagContainer) {
		tags = tagContainer.children('ul').children();
		tags.css( {
			'position' : 'absolute',
			'list-style-type' : 'none',
			'list-style-position' : 'outside',
			'list-style-image' : 'none'
		});
		for ( var i = 0; i < tags.length; i++) {
			var jTag = jQuery(tags[i]);
			var link = jQuery(jTag.children()[0]);
			tags[i] = jTag;
			jTag.hover( function() {
				jQuery(this).css(options.hoverStyle);
			}, function() {
				jQuery(this).css(options.mouseOutStyle);
			})
		}
	}

	function deployTags() {
		var phi = 0;
		var theta = 0;
		var max = mathAssets.tLength + 1;
		var i = 0;
		while (i++ < max) {
			phi = Math.acos(-1 + (2 * i - 1) / max);
			theta = Math.sqrt(max * Math.PI) * phi;
			tags[i - 1].cx = options.radius * Math.cos(theta) * Math.sin(phi);
			tags[i - 1].cy = options.radius * Math.sin(theta) * Math.sin(phi);
			tags[i - 1].cz = options.radius * Math.cos(phi);
			tags[i - 1].h = jQuery(tags[i - 1]).height() / 4;
			tags[i - 1].w = jQuery(tags[i - 1]).width() / 4;
		}
	}

	function calcRotation(fy, fx) {
		curState.sy = Math.sin(fy * mathAssets.dtr);
		curState.cy = Math.cos(fy * mathAssets.dtr);
		curState.sx = Math.sin(fx * mathAssets.dtr);
		curState.cx = Math.cos(fx * mathAssets.dtr);
	}

	function updateTags() {
		var fy;
		var fx;
		if (curState.mouseOver) {
			fy = options.speed - mathAssets.speedY * curState.mouseY;
			fx = mathAssets.speedX * curState.mouseX - options.speed;
		} else {
			fy = curState.lastFy * options.slower;
			fx = curState.lastFx * options.slower;
		}
		if (curState.lastFy != fy || curState.lastFx != fx) {
			calcRotation(fy, fx);
			curState.lastFy = fy;
			curState.lastFx = fx;
		}
		if (Math.abs(fy) > 0.01 || Math.abs(fx) > 0.01) {
			j = -1;
			while (j++ < mathAssets.tLength) {
				rx1 = tags[j].cx;
				ry1 = tags[j].cy * curState.cy + tags[j].cz * -curState.sy;
				rz1 = tags[j].cy * curState.sy + tags[j].cz * curState.cy;
				tags[j].cx = rx1 * curState.cx + rz1 * curState.sx;
				tags[j].cy = tags[j].cy * curState.cy + tags[j].cz
						* -curState.sy;
				tags[j].cz = rx1 * -curState.sx + rz1 * curState.cx;
				var per = mathAssets.diameter
						/ (mathAssets.diameter + tags[j].cz);
				tags[j].x = tags[j].cx * per;
				tags[j].y = tags[j].cy * per;
				tags[j].alpha = per / 2;
				tags[j]
						.css( {
							'left' : mathAssets.whratio
									* (tags[j].x - tags[j].w * per)
									+ mathAssets.halfWidth,
							'top' : mathAssets.hwratio
									* (tags[j].y - tags[j].h * per)
									+ mathAssets.halfHeight,
							'opacity' : tags[j].alpha,
							'font-size' : options.fontMultiplier
									* tags[j].alpha + 'px',
							'z-index' : Math.round(-tags[j].cz)
						});
			}
		}
	}
})(jQuery);
