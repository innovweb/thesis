function getThesesByYear(year, count, offset) {
	$.get("http://dataspace.princeton.edu/jspui/handle/88435/dsp019c67wm88m/browse?type=graduation&order=DESC", 
	  { rpp: count, value: year, offset: offset }
	  ).done(function( data ) {
	    var parsed = $('<div/>').append(data);
	    var titles = parsed.find("table.miscTable > tbody > tr > td > a");
	    var issueDates = parsed.find("td.pageContents > table.miscTable > tbody > tr > td:nth-child(1)");
	    var authors = parsed.find("table > tbody > tr > td > em");

	    for (var i = 0; i < titles.length; i++) {

	    	var thesis = {
	    		title: $(titles[i]).text(),
	    		issueDate: $(issueDates[i]).text(),
	    		author: $(authors[i]).text(),
	    	}
	    	console.log(thesis);
	    }

	  });
}
