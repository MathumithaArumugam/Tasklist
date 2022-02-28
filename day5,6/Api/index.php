<?php
$connect = new mysqli("localhost","root","","mathu");
function getParam($key)
{
    if(isset($_POST[$key]))
        return($_POST[$key]);
    else if(isset($_GET[$key]))
        return($_GET[$key]);
    else
        return(null);
}
if(isset($_POST["operation"]) || isset($_GET["operation"]))
{
    $operation=getParam("operation");
    $dataid=getParam("id");

    $sname=getParam("sname");
    $rollno=getParam("rollno");
    $grade=getParam("grade");
    $phoneno=getParam("phoneno");
    $fname=getParam("fname");
    $mname=getParam("mname");
    $address=getParam("address");
    if($operation=="PUT")
    {
        $result=mysqli_query($connect,"INSERT INTO STUDENT (STUDENTNAME, ROLLNUMBER, PHONENUMBER, GRADE,FATHERNAME, MOTHERNAME, ADDRESS) VALUES('$sname','$rollno','$phoneno','$grade','$fname','$mname','$address');");
        if($result)
        {
            echo "OK ".mysqli_insert_id($connect);
        }
    }
    else if($operation=="POST")
    {
        $result=mysqli_query($connect,"UPDATE STUDENT SET STUDENTNAME='$sname',ROLLNUMBER='$rollno',PHONENUMBER='$phoneno',GRADE='$grade',FATHERNAME='$fname',MOTHERNAME='$mname',ADDRESS='$address' WHERE ID=$dataid;");
        echo "UPDATE STUDENT SET STUDENTNAME='$sname',ROLLNUMBER='$rollno',PHONENUMBER='$phoneno',GRADE='$grade',FATHERNAME='$fname',MOTHERNAME='$mname',ADDRESS='$address' WHERE ID=$dataid;";
        if($result)
        {
            echo "OK";
        }
    }
    else if($operation=="DELETE")
    {
        $result=mysqli_query($connect,"DELETE FROM STUDENT WHERE ID=$dataid;");
        if($result)
        {
            echo "OK";
        }
    }
    else if($operation=="GET")
    {
        header('Content-Type: application/json');
        $qry="SELECT ID,STUDENTNAME, ROLLNUMBER, PHONENUMBER, GRADE,FATHERNAME, MOTHERNAME, ADDRESS FROM STUDENT;";
        if($dataid!=null)
            $qry="SELECT ID,STUDENTNAME, ROLLNUMBER, PHONENUMBER, GRADE,FATHERNAME, MOTHERNAME, ADDRESS FROM STUDENT WHERE ID=$dataid;";
        $result=mysqli_query($connect,$qry);
        echo "[";
        while($row=mysqli_fetch_assoc($result))
        {
            echo "{";
            echo "'ID' : '".$row["ID"]."',";
            echo "'StudentName' : '".$row["STUDENTNAME"]."',";
            echo "'RollNumber' : '".$row["ROLLNUMBER"]."',";
            echo "'PhoneNumber' : '".$row["PHONENUMBER"]."',";
            echo "'Grade' : '".$row["GRADE"]."',";
            echo "'FatherName' : '".$row["FATHERNAME"]."',";
            echo "'MotherName' : '".$row["MOTHERNAME"]."',";
            echo "'Addresss' : '".$row["ADDRESS"]."'";
            echo "},";
        }
        echo "]";

    }




}



?>