var toggle = false;

function hamburger()
{
	if (toggle == true) closeNav();
	else if (toggle == false) openNav();
}

function openNav() 
{
	toggle = true;

	document.getElementById("overlay").style.opacity = ".75";
	document.getElementById("overlay").style.visibility = "visible";

	document.getElementById("navigation").style.left = "0";
	document.getElementById("navigation").style.visibility = "visible";
}
function closeNav() 
{
	toggle = false;

	document.getElementById("overlay").style.opacity = "0";
	document.getElementById("overlay").style.visibility = "hidden";

	document.getElementById("navigation").style.left = "-100vw";
	document.getElementById("navigation").style.visibility = "hidden";
}

