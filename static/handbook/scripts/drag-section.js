function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "-drag")) 
  {
    document.getElementById(elmnt.id + "-drag").onmousedown = dragMouseDown;
  } else 
  {
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) 
  {
    e = e || window.event;
    e.preventDefault();
    pos3 = e.clientX;
    pos4 = e.clientY;
	
    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) 
  {
    e = e || window.event;
    e.preventDefault();

    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;

	var newy = (elmnt.offsetTop - pos2) * 100 / document.documentElement.clientHeight;
	var newx = (elmnt.offsetLeft - pos1) * 100 / document.documentElement.clientWidth;
	
	if (newx < 0) newx = 0;
	else if (newx > 70) newx = 70;

	if (newy < 0) newy = 0;
	else if (newy > 90) newy = 90;
	
	// console.log(newx + " " + newy)

    elmnt.style.top = newy + "vh";
    elmnt.style.left = newx + "vw";
  }

  function closeDragElement() 
  {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

dragElement(document.getElementById("info"));
dragElement(document.getElementById("stat"));
