/* Scrapes thesis info from Princeton Dataspace
  example usage (with a callback because $.get is async): 

  getThesesByYear(2014, 20, 0, function(data) {
  	// data is an array of objects
	for (var i = 0; i < data.length; i++) {
		console.log(data[i].title + " " + data[i].issueDate + " " + data[i].author);
	}
  });
 */
function getThesesByYear(year, count, offset, callback) {
	$.get("http://dataspace.princeton.edu/jspui/handle/88435/dsp019c67wm88m/browse?type=graduation&order=DESC", 
	  { rpp: count, value: year, offset: offset }
	  ).done(function( data ) {
	    var parsed = $('<div/>').append(data);
	    var titles = parsed.find("table.miscTable > tbody > tr > td > a");
	    var issueDates = parsed.find("td.pageContents > table.miscTable > tbody > tr > td:nth-child(1)");
	    var authors = parsed.find("table > tbody > tr > td > em");

	    var zipped = [];

	    for (var i = 0; i < titles.length; i++) {
	    	var thesis = {
	    		title: $(titles[i]).text(),
	    		issueDate: $(issueDates[i]).text(),
	    		author: $(authors[i]).text(),
	    	}
	    	zipped.push(thesis);
	    }

	    callback(zipped);
	  });
}
