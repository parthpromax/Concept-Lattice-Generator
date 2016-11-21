<?php
	$flag = 0;
	if(isset($_POST['createLattice'])) {
		$data = $_POST['data'];
		$f = fopen("in.txt", "w");
		fwrite($f, $data);
		fclose($f);
		exec("make &");
		$flag = 1;
	}
?>

<html>
	<head>
		<title>Lattice Generator</title>
		<meta http-equiv="cache-control" content="max-age=0" />
		<meta http-equiv="cache-control" content="no-cache" />
		<meta http-equiv="expires" content="0" />
		<meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha.5/css/bootstrap.min.css">
		<style>.big-checkbox {width: 30px; height: 30px;}td{text-align: center}</style>
		<script>
			
			
			var numberOfRows = 2
			var numberOfCols = 3
			
			function insertRowInTable() {
				var tab = document.getElementById("table1")
				var r = tab.insertRow(-1)
				
				r.insertCell(-1).innerHTML = numberOfRows
				r.insertCell(-1).innerHTML = "<input placeholder='Object Name' size='12' class='form-control' id='"+numberOfRows+"xo'>"
				
				for(var i = 1; i < numberOfCols-1; i++) {
					r.insertCell(-1).innerHTML = "<input type='checkbox' class='big-checkbox' id='" + numberOfRows + "x" + i +"'/>"
				}
				numberOfRows++
			}
			
			function insertColumnInTable() {
				var colId = numberOfCols - 1
				var tab = document.getElementById("table1")
				var r = tab.rows[0]
				var c = r.insertCell(-1)
				c.innerHTML = "<input placeholder='Attribute Name' class='form-control' size='12' id='ax"+colId+"'>"
				for(var i = 1; i < numberOfRows; i++) {
					r = tab.rows[i]
					c = r.insertCell(-1)
					c.innerHTML = "<input type='checkbox' class='big-checkbox' id='"+ i + "x" + colId +"'/>"
				}
				numberOfCols++
			}
			
			function createData() {
				var str = "0"
				for( var k = 1; k < numberOfCols-1; k++) {
					var v = document.getElementById("ax"+k).value
					str += " " + v
				}
				
				str += "\n"
				
				for(var i = 1; i < numberOfRows; i++) {
					v = document.getElementById(i+"xo").value
					str += v
					
					for(var j = 1; j < numberOfCols-1; j++) {
						v = document.getElementById(i+"x"+j).checked
						if(v)
							str += " 1"
						else
							str += " 0"
					}
					
					str += "\n"
				}
				document.getElementById("data").value = str
			}
			
			
		</script>
	</head>
	
	<body style="text-align: center;">
		<br/><h1>Concept Lattice Generation from Access Matrix</h1><br/>
		
		<input type="button" value="Insert Row" class="btn btn-success" onclick="insertRowInTable()"/>
		<input type="button" value="Insert Column" class="btn btn-success" onclick="insertColumnInTable()"/>
		<br>
		<br>
		
		<table id="table1" border="1" class="table table-striped">
			<tr>
				<td></td>
				<td></td>
				<td><input placeholder="Attribute Name" class="form-control" size='12' id="ax1"></td>
			</tr>
			<tr>
				<td>1</td>
				<td><input placeholder="Object Name" class="form-control" size='12' id="1xo"></td>
				<td><input type="checkbox" class="big-checkbox" id="1x1"></td>
			</tr>
		</table>
		
		<br><br>
		
		<form method="post" onsubmit="createData()">
			<input type="hidden" name="data" id="data"/>
			<input type="submit" value="Create Lattice" class="btn btn-primary" name="createLattice"/>
		</form>
		
		
	</body>
</html>
<?php
	if($flag == 1) {
		echo "<img src='Lattice.png'>";
		echo '<br/><br/><a href="Lattice.png" download class="btn btn-success">Download Image</a> ';
		echo '<a href="Lattice.pdf" download class="btn btn-success">Download PDF</a><br/><br/>';
	}
?>