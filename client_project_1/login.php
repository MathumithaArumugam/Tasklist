<?php
$connect = new mysqli("localhost","root","","client_project_1");
function getParam($key)
{
    if(isset($_POST[$key]))
        return($_POST[$key]);
    else if(isset($_GET[$key]))
        return($_GET[$key]);
    else
        return(null);
}
$username=getParam("username");
$password=getParam("password");
if($username!= NULL && $password!=NULL){
    $query="SELECT USER_ID FROM USER_DETAILS WHERE USER_NAME='$username' AND USER_PASSWORD='$password';";
    $result=mysqli_query($connect, $query);
    if($row=mysqli_fetch_assoc($result)){
        echo $row["USER_ID"];
    }

}

?>