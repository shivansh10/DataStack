<?php
         $dbhost = 'localhost:3036';
         $dbuser = 'root';
         $dbpass = 'Project@1234';
         $conn = mysql_connect($dbhost, $dbuser, $dbpass);
      
         if(! $conn ) {
            die('Could not connect: ' . mysql_error());
         }
         
         echo 'Connected successfully';
         mysql_close($conn);
      ?>
