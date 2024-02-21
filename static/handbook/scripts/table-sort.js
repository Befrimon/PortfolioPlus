function sortTable(n) { 
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("itemTable");
  switching = true;

  dir = "asc";
 
  while (switching) 
  {
    switching = false;
    rows = table.rows;
    
    for (i = 1; i < (rows.length - 1); i++) 
	{
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("td")[n];
      y = rows[i + 1].getElementsByTagName("td")[n];
      
      if (dir == "asc" && x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) 
	  {
    	shouldSwitch = true;
        break;
      } else if (dir == "desc" && x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) 
	  {
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) 
	{
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount++;
    } else if (switchcount == 0 && dir == "asc") 
	{
      dir = "desc";
      switching = true;
    }
  }
}

function findNames() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.getElementById("itemTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
